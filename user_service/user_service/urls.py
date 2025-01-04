from django.urls import path
from users.views import UserListCreateView
from users.views import OrganizationListCreateView
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/users/', UserListCreateView.as_view(), name='user-list-create'),
    
    path('api/organizations/', OrganizationListCreateView.as_view(), name='organization-create'),
]
