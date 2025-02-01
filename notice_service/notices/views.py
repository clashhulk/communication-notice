from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import NoticeType, Template, Notice
from .serializers import NoticeTypeSerializer, TemplateSerializer, NoticeSerializer


class NoticeTypeViewSet(viewsets.ModelViewSet):
    queryset = NoticeType.objects.all()
    serializer_class = NoticeTypeSerializer


class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['created_at', 'priority']
    search_fields = ['status', 'priority']

    def get_queryset(self):
        queryset = super().get_queryset()
        notice_type = self.request.query_params.get('notice_type')
        status = self.request.query_params.get('status')

        if notice_type:
            queryset = queryset.filter(notice_type=notice_type)
        if status:
            queryset = queryset.filter(status=status)

        return queryset

    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        notice = get_object_or_404(Notice, pk=pk)
        new_status = request.data.get('status', None)

        if new_status:
            notice.status = new_status
            notice.save()
            return Response({'message': 'Status updated', 'new_status': new_status}, status=status.HTTP_200_OK)
        return Response({'error': 'Status field required'}, status=status.HTTP_400_BAD_REQUEST)
