import datetime
import uuid

from pydantic import BaseModel, validator


class ServiceArea(BaseModel):
    row_id: uuid.UUID = None
    name: str
    price: float
    polygon: dict
    provider_id: uuid.UUID
    created_at: datetime.datetime = None

    @validator('polygon')
    def geo_json_valid(cls, value):
        assert 'type' in value.keys(), 'type must have a value'
        assert value.get('type') == 'Polygon', 'type must be Polygon'
        assert 'coordinates' in value.keys(), 'coordinates must have a value'
        assert len(value.get('coordinates')) > 0, 'coordinates must have values'
        for coord in value.get('coordinates')[0]:
            assert len(coord) == 2, 'all coordinates must have two values'
        return value




