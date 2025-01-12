from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    OrganizationListCreateAPIView,
    OrganizationDetailAPIView,
    RegisterUserAPIView,
    UserListAPIView,
    UserDetailAPIView,
    CustomTokenObtainPairView,
    TokenValidationAPIView,
)

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/validate/', TokenValidationAPIView.as_view(), name='token_validate'),
    path('register/', RegisterUserAPIView.as_view(), name='user_register'),
    path('users/', UserListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user_detail'),
    path('organizations/', OrganizationListCreateAPIView.as_view(),
         name='organization_list_create'),
    path('organizations/<int:pk>/', OrganizationDetailAPIView.as_view(),
         name='organization_detail'),
]
