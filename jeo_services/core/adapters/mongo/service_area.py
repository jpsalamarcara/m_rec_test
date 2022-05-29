import uuid
from typing import List

import h3
from injector import inject

from jeo_services.core.adapters.mongo.models.service_area import ServiceAreaCollection
from jeo_services.core.domain.service_area import ServiceArea
from jeo_services.core.ports.service_area import ServiceAreaPort


def compute_polygon_hash(coordinates: list):
    for resolution in range(10, -1, -1):
        hashes = set(map(lambda x: h3.geo_to_h3(x[0], x[1], resolution), coordinates))
        if len(hashes) == 1:
            return list(hashes)[0]
    return None


class MongoServiceAreaAdapter(ServiceAreaPort):

    @inject
    def __init__(self):
        self.storage = ServiceAreaCollection

    def add(self, row: ServiceArea) -> uuid.UUID:
        data = row.dict(exclude={'row_id', 'created_at'})
        data['h_three_geo_hash'] = compute_polygon_hash(data.get('polygon').get('coordinates')[0])
        to_store = self.storage(**data)
        to_store.save()
        return to_store.row_id

    def get(self, row_id: str = None,
            name: str = None,
            price: str = None,
            limit: int = 100,
            offset: int = 0) -> List[ServiceArea]:
        pass

    def get_by_lat_long(self, lat: float,
                        long: float,
                        limit: int = 100,
                        offset: int = 0) -> List[ServiceArea]:
        hashes = list(set(map(lambda x: h3.geo_to_h3(lat, long, x), range(0, 11))))
        cursor = self.storage.objects(h_three_geo_hash__in=hashes, polygon={
            "$geoIntersects": {
                "$geometry": {
                    "type": "Point",
                    "coordinates": [lat, long]
                }
            }
        })
        raw = (x.to_mongo() for x in cursor[offset * limit: (offset + 1) * limit])
        output = []
        for row in raw:
            row['row_id'] = row.get('_id')
            output.append(ServiceArea(**row))
        return output

    def update(self, row: ServiceArea):
        data = row.dict()
        row_id = data.pop('row_id')
        self.storage.objects(row_id=row_id).update(**data)

    def delete(self, row_id: uuid.UUID):
        row = self.storage.objects(row_id=row_id).first()
        if row:
            row.delete()
