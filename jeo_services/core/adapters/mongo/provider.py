import uuid
from typing import List

from injector import inject

from jeo_services.core.adapters.mongo.models.provider import ProviderCollection
from jeo_services.core.domain.provider import Provider
from jeo_services.core.ports.provider import ProviderPort


class MongoProviderAdapter(ProviderPort):

    @inject
    def __init__(self):
        self.storage = ProviderCollection

    def add(self, row: Provider) -> uuid.UUID:
        data = row.dict(exclude={'row_id', 'created_at'})
        to_store = self.storage(**data)
        to_store.save()
        return to_store.row_id

    def get(self, row_id: str = None,
            name: str = None,
            email: str = None,
            phone_number: str = None,
            lang: str = None,
            currency: str = None,
            limit: int = 100,
            offset: int = 0) -> List[Provider]:
        query = dict()
        if row_id:
            query['row_id'] = uuid.UUID(hex=row_id)
        if name:
            query['name'] = name
        if email:
            query['email'] = email
        if phone_number:
            query['phone_number'] = phone_number
        if lang:
            query['lang'] = lang
        if currency:
            query['currency'] = currency
        cursor = self.storage.objects(**query)
        raw = (x.to_mongo() for x in cursor[offset * limit: (offset + 1) * limit])
        output = []
        for row in raw:
            row['row_id'] = row.get('_id')
            output.append(Provider(**row))
        return output

    def update(self, row: Provider):
        data = row.dict()
        row_id = data.pop('row_id')
        self.storage.objects(row_id=row_id).update(**data)

    def delete(self, row_id: uuid.UUID):
        row = self.storage.objects(row_id=row_id).first()
        if row:
            row.delete()
