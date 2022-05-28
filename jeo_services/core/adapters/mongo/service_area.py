from typing import List

from jeo_services.core.domain.service_area import ServiceArea
from jeo_services.core.ports.service_area import ServiceAreaPort


class MongoServiceAreaAdapter(ServiceAreaPort):

    def add(self, row: ServiceArea):
        pass

    def get(self, row_id: str, name: str, price: str, limit: int, offset: int) -> List[ServiceArea]:
        pass

    def get_by_lat_long(self, lat: float, long: float, limit: int, offset: int) -> List[ServiceArea]:
        pass

    def update(self, row: ServiceArea):
        pass

    def delete(self, row_id: str):
        pass
