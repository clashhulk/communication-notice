from django.contrib.auth.models import AbstractUser
from django.db import models
from .organization import Organization


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('user', 'User'),
    )
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True, blank=True, null=True)
    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default='user')
    organization = models.ForeignKey(
        Organization, on_delete=models.SET_NULL, null=True, blank=True
    )

    REQUIRED_FIELDS = ['email', 'phone']