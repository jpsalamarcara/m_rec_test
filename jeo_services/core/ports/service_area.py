import abc
import uuid
from typing import List

from jeo_services.core.domain.service_area import ServiceArea


class ServiceAreaPort(abc.ABC):

    @abc.abstractmethod
    def add(self, row: ServiceArea) -> uuid.UUID:
        pass

    @abc.abstractmethod
    def get(self, row_id: str = None,
            name: str = None,
            price: str = None,
            limit: int = 100,
            offset: int = 0) -> List[ServiceArea]:
        pass

    @abc.abstractmethod
    def get_by_lat_long(self, lat: float,
                        long: float,
                        limit: int,
                        offset: int) -> List[ServiceArea]:
        pass

    @abc.abstractmethod
    def update(self, row: ServiceArea):
        pass

    @abc.abstractmethod
    def delete(self, row_id: str):
        pass
