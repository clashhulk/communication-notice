from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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
