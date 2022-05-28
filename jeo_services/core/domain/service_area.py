import uuid

from pydantic import BaseModel


class ServiceArea(BaseModel):
    id: uuid.UUID
    name: str
    price: float
    geo_json: dict
