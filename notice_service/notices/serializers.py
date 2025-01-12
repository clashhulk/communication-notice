from rest_framework import serializers
from .models import NoticeType, Notice


class NoticeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeType
        fields = ['id', 'org_id', 'name', 'description',
                  'dynamic_schema', 'created_at']

    def validate_dynamic_schema(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError(
                "Dynamic schema must be a valid JSON object.")
        return value


class NoticeSerializer(serializers.ModelSerializer):
    notice_type = serializers.PrimaryKeyRelatedField(
        queryset=NoticeType.objects.all())

    class Meta:
        model = Notice
        fields = [
            'id',
            'notice_type',
            'created_by',
            'status',
            'priority',
            'created_at',
            'updated_at',
            'dynamic_data',
        ]

    def validate_dynamic_data(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError(
                "Dynamic data must be a valid JSON object.")
        return value

    def validate(self, attrs):
        notice_type = attrs.get('notice_type')
        dynamic_data = attrs.get('dynamic_data')

        if notice_type and dynamic_data:
            schema_keys = set(notice_type.dynamic_schema.keys())
            data_keys = set(dynamic_data.keys())

            if schema_keys != data_keys:
                raise serializers.ValidationError(
                    "Dynamic data keys must match the dynamic schema keys of the notice type."
                )
        return attrs
