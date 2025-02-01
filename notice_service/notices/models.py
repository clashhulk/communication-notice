from django.db import models
from uuid import uuid4


class NoticeType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    org_id = models.UUIDField()
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    dynamic_schema = models.JSONField()  # Defines structure of notices for this type
    created_at = models.DateTimeField(auto_now_add=True)


class Template(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    notice_type = models.ForeignKey(NoticeType, on_delete=models.CASCADE)
    channel = models.CharField(
        max_length=50,
        choices=[('email', 'Email'), ('whatsapp', 'WhatsApp'),
                 ('sms', 'SMS'), ('rpad', 'RPAD')],
    )
    template_content = models.TextField()  # Stores message format with placeholders
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Notice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    notice_type = models.ForeignKey(NoticeType, on_delete=models.CASCADE)
    created_by = models.UUIDField()
    status = models.CharField(max_length=50, default='active', db_index=True)
    priority = models.CharField(max_length=50, default='medium')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    dynamic_data = models.JSONField()  # Stores data specific to this notice
