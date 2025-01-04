from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField(null=True, blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('client', 'Client')])
    email = models.EmailField(null=True, blank=True)
    org = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
