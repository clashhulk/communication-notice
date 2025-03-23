from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..serializers.authentication import CustomTokenObtainPairSerializer
from ..utils import standardized_response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..serializers.api_responses import StandardApiResponse


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="Authentication token response",
                schema=StandardApiResponse(),
                examples={
                    'application/json': {
                        'success': True,
                        'data': {
                            'access': 'token',
                            'refresh': 'token'
                        },
                        'errors': {},
                        'meta': {}
                    }
                }
            )
        },
        operation_description="Login endpoint that provides JWT authentication tokens."
    )
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            return standardized_response(data=response.data)
        else:
            return standardized_response(errors=response.data, status=response.status_code)


class TokenValidationAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role,
            "organization": {
                "id": user.organization.id if user.organization else None,
                "name": user.organization.name if user.organization else None,
                "address": user.organization.address if user.organization else None,
                "phone": user.organization.phone if user.organization else None,
            } if user.organization else None,
        }
        return standardized_response(data=user_data)
