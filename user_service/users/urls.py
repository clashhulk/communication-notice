from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    OrganizationListCreateAPIView,
    OrganizationDetailAPIView,
    RegisterUserAPIView,
    UserListAPIView,
    UserDetailAPIView
)

urlpatterns = [
    # JWT Auth
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # User Registration
    path('register/', RegisterUserAPIView.as_view(), name='user_register'),

    # User APIs
    path('users/', UserListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user_detail'),

    # Organization APIs
    path('organizations/', OrganizationListCreateAPIView.as_view(),
         name='organization_list_create'),
    path('organizations/<int:pk>/', OrganizationDetailAPIView.as_view(),
         name='organization_detail'),
]
