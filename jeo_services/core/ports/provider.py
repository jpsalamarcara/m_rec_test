import abc
import uuid
from typing import List

from jeo_services.core.domain.provider import Provider


class ProviderPort(abc.ABC):

    @abc.abstractmethod
    def add(self, row: Provider) -> uuid.UUID:
        pass

    @abc.abstractmethod
    def get(self, row_id: str = None,
            name: str = None,
            email: str = None,
            phone_number: str = None,
            lang: str = None,
            currency: str = None,
            limit: int = 100,
            offset: int = 0
            ) -> List[Provider]:
        pass

    @abc.abstractmethod
    def update(self, row: Provider):
        pass

    @abc.abstractmethod
    def delete(self, row_id: str):
        pass
