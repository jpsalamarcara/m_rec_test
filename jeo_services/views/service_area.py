from rest_framework import viewsets

from jeo_services.core.ports.service_area import ServiceAreaPort
from jeo_services.dependency_injection import factory


class ServiceAreaViewSet(viewsets.ViewSet):

    def __init__(self, *args, **kwargs):
        super(ServiceAreaViewSet, self).__init__(*args, **kwargs)
        self.service = factory.get(ServiceAreaPort)

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
