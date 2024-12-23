from django.contrib import admin
from .models import Notice

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')  # Columns in the admin list view
    search_fields = ('title', )  # Search box for title
    list_filter = ('created_at', )  # Filter sidebar by created_at

admin.site.register(Notice, NoticeAdmin)
