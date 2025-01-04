from django.db import models

class NoticeType(models.Model):
    org_id = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    dynamic_schema = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

class Notice(models.Model):
    notice_type = models.ForeignKey(NoticeType, on_delete=models.CASCADE)
    created_by = models.IntegerField()
    status = models.CharField(max_length=50, default='active')
    priority = models.CharField(max_length=50, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dynamic_data = models.JSONField()
