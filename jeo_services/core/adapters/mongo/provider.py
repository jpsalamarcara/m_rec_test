from typing import List

from jeo_services.core.domain.provider import Provider
from jeo_services.core.ports.provider import ProviderPort


class MongoProviderAdapter(ProviderPort):

    def add(self, row: Provider):
        pass

    def get(self, row_id: str, name: str, email: str, phone_number: str, lang: str, currency: str, limit: int,
            offset: int) -> List[Provider]:
        pass

    def update(self, row: Provider):
        pass

    def delete(self, row_id: str):
        pass