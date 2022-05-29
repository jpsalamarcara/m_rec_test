import datetime
import uuid

from pydantic import BaseModel


class Provider(BaseModel):
    row_id: uuid.UUID = None
    name: str
    email: str
    phone_number: str
    lang: str = 'en'
    currency: str = 'usd'
    created_at: datetime.datetime = None
