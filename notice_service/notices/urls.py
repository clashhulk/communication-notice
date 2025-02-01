from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoticeTypeViewSet, TemplateViewSet, NoticeViewSet

router = DefaultRouter()
router.register(r'notice-types', NoticeTypeViewSet, basename='notice-type')
router.register(r'templates', TemplateViewSet, basename='template')
router.register(r'notices', NoticeViewSet, basename='notice')

urlpatterns = [
    path('', include(router.urls)),
]
