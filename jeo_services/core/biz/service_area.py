import uuid

from injector import inject

from jeo_services.core.domain.service_area import ServiceArea
from jeo_services.core.ports.provider import ProviderPort
from jeo_services.core.ports.service_area import ServiceAreaPort


class ServiceAreaService(object):

    @inject
    def __init__(self, provider_port: ProviderPort,
                 service_area_port: ServiceAreaPort):
        self.provider_port = provider_port
        self.service_area_port = service_area_port

    def add_service_area(self, row: ServiceArea) -> uuid.UUID:
        assert self.provider_port.exists(row.provider_id), 'provider not found!'
        return self.service_area_port.add(row)

    def update_service_area(self, row: ServiceArea):
        assert self.provider_port.exists(row.provider_id), 'provider not found!'
        self.service_area_port.update(row)
