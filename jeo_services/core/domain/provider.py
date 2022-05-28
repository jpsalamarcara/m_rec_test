import uuid

from pydantic import BaseModel


class Provider(BaseModel):
    id: uuid.UUID
    name: str
    email: str
    phone_number: str
    lang: str
    currency: str
