from rest_framework import serializers
from ..models import User, Organization
from .organization import OrganizationSerializer


class RegisterSerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(write_only=True)
    organization_address = serializers.CharField(
        write_only=True, required=False, allow_blank=True, default="")
    organization_phone = serializers.CharField(
        write_only=True, required=False, allow_blank=True, default="")

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "phone",
            "role",
            "organization_name",
            "organization_address",
            "organization_phone",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {"required": True},
            "email": {"required": True},
        }

    def validate(self, attrs):
        if not attrs.get("organization_name"):
            raise serializers.ValidationError(
                {"organization_name": "This field is required."})
        return attrs

    def create(self, validated_data):
        org_name = validated_data.pop("organization_name")
        org_address = validated_data.pop("organization_address", "")
        org_phone = validated_data.pop("organization_phone", "")

        organization, created = Organization.objects.get_or_create(
            name=org_name,
            defaults={"address": org_address, "phone": org_phone},
        )

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            phone=validated_data.get("phone", None),
            role=validated_data.get("role", "user"),
            organization=organization,
        )
        return user

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "A user with this email already exists.")
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                "A user with this username already exists.")
        return value

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response.pop("password", None)
        return response


class UserSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(read_only=True)
    organization_id = serializers.PrimaryKeyRelatedField(
        queryset=Organization.objects.all(), source='organization', write_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name',
                  'phone', 'role', 'organization', 'organization_id')
