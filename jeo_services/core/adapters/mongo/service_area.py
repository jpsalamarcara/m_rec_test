import uuid
from typing import List

import h3
from injector import inject

from jeo_services.core.adapters.mongo.models.service_area import ServiceAreaCollection
from jeo_services.core.domain.service_area import ServiceArea
from jeo_services.core.ports.service_area import ServiceAreaPort


def compute_polygon_hash(coordinates: list):
    for resolution in range(10, -1, -1):
        hashes = set(map(lambda x: h3.geo_to_h3(x[0], x[1], resolution), coordinates[0]))
        if len(hashes) == 1:
            return list(hashes)[0]
    return None


class MongoServiceAreaAdapter(ServiceAreaPort):

    @inject
    def __init__(self):
        self.storage = ServiceAreaCollection

    def add(self, row: ServiceArea) -> uuid.UUID:
        data = row.dict(exclude={'row_id', 'created_at'})
        data['h_three_geo_hash'] = compute_polygon_hash(data.get('polygon').get('coordinates'))
        to_store = self.storage(**data)
        to_store.save()
        return to_store.row_id

    def get(self, row_id: str, name: str, price: str, limit: int, offset: int) -> List[ServiceArea]:
        pass

    def get_by_lat_long(self, lat: float, long: float, limit: int, offset: int) -> List[ServiceArea]:
        hashes = set(map(lambda x: h3.geo_to_h3(lat, long, x), range(0, 16)))
        pass

    def update(self, row: ServiceArea):
        pass

    def delete(self, row_id: str):
        pass
