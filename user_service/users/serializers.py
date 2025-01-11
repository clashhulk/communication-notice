from rest_framework import serializers, generics, permissions
from .models import User, Organization
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

    def validate_name(self, value):
        if Organization.objects.filter(name=value).exists():
            raise serializers.ValidationError(
                "An organization with this name already exists.")
        return value


class OrganizationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegisterSerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(write_only=True)
    organization_address = serializers.CharField(
        write_only=True, required=False)
    organization_phone = serializers.CharField(write_only=True, required=False)

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

    def create(self, validated_data): from rest_framework import serializers


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

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response.pop("password", None)
        return response

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
            phone=validated_data.get("phone", ""),
            role=validated_data.get("role", "user"),
            organization=organization,
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(read_only=True)
    organization_id = serializers.PrimaryKeyRelatedField(
        queryset=Organization.objects.all(), source='organization', write_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name',
                  'phone', 'role', 'organization', 'organization_id')


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user
        data["user"] = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "phone": user.phone,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": user.role,
        }

        if user.organization:
            data["organization"] = {
                "id": user.organization.id,
                "name": user.organization.name,
                "address": user.organization.address,
                "phone": user.organization.phone,
            }
        else:
            data["organization"] = None

        return data
