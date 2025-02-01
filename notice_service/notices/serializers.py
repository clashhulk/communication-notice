from rest_framework import serializers
from .models import NoticeType, Template, Notice
import json


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'


class NoticeTypeSerializer(serializers.ModelSerializer):
    templates = TemplateSerializer(
        many=True, read_only=True)  # Nested Templates

    class Meta:
        model = NoticeType
        fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):
    notice_type = serializers.PrimaryKeyRelatedField(
        queryset=NoticeType.objects.all())
    dynamic_data = serializers.JSONField()

    class Meta:
        model = Notice
        fields = '__all__'

    def validate_dynamic_data(self, value):
        """
        Validate that dynamic_data matches the schema in NoticeType.
        """
        notice_type = self.instance.notice_type if self.instance else self.initial_data.get(
            'notice_type')
        if not notice_type:
            raise serializers.ValidationError("Notice Type is required.")

        # Ensure notice_type is an object, not an ID
        if isinstance(notice_type, int):
            notice_type = NoticeType.objects.get(id=notice_type)

        schema = notice_type.dynamic_schema.get('fields', {})

        # Check required fields
        for field, field_type in schema.items():
            if field not in value:
                raise serializers.ValidationError(
                    f"Missing required field: {field}")
            if not isinstance(value[field], self.get_python_type(field_type)):
                raise serializers.ValidationError(f"Invalid type for field '{
                                                  field}', expected {field_type}")

        return value

    def get_python_type(self, field_type):
        """
        Map JSON schema field types to Python types.
        """
        mapping = {
            "string": str,
            "integer": int,
            "float": float,
            "boolean": bool,
            "date": str,  # Dates should be handled separately
        }
        return mapping.get(field_type, str)  # Default to string
