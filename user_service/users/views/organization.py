from rest_framework import generics, permissions
from ..models import Organization
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..serializers.organization import OrganizationSerializer
from ..serializers.api_responses import StandardApiResponse
from ..utils import standardized_response


class OrganizationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return standardized_response(data=serializer.data)

    @swagger_auto_schema(
        request_body=OrganizationSerializer,
        responses={
            201: openapi.Response(description="Organization created", schema=StandardApiResponse())
        }
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return standardized_response(data=serializer.data, status=201)
        else:
            return standardized_response(errors=serializer.errors, status=400)


class OrganizationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return standardized_response(data=serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return standardized_response(data=serializer.data)
        else:
            return standardized_response(errors=serializer.errors, status=400)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return standardized_response(data={'message': 'Organization deleted'}, status=204)
