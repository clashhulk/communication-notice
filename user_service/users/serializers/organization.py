from rest_framework import serializers
from ..models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

    def validate_name(self, value):
        if Organization.objects.filter(name=value).exists():
            raise serializers.ValidationError(
                "An organization with this name already exists.")
        return value
