from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAdminUser
from .serializers import CustomTokenObtainPairSerializer
from rest_framework import generics, permissions
from .models import Organization, User
from .serializers import (
    RegisterSerializer,
    UserSerializer,
    OrganizationSerializer
)
from rest_framework.views import APIView
from .permissions import IsAdmin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination


class OrganizationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [AllowAny]
# class OrganizationListCreateAPIView(generics.ListCreateAPIView):
#     permission_classes = [IsAdminUser]


class OrganizationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegisterUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class UserPagination(PageNumberPagination):
    page_size = 10  # Number of users per page


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = UserPagination


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsAdmin]  # Admin-only access


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class TokenValidationAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user  # Get the authenticated user
        return Response({
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
        })
