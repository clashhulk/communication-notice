from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from ..models import User
from ..serializers.user import RegisterSerializer, UserSerializer
from ..permissions import IsAdmin


class RegisterUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class UserPagination(PageNumberPagination):
    page_size = 10


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = UserPagination


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]
