import abc
from typing import List

from jeo_services.core.domain.provider import Provider


class ProviderPort(abc.ABC):

    @abc.abstractmethod
    def add(self, row: Provider):
        pass

    @abc.abstractmethod
    def get(self, row_id: str,
            name: str,
            email: str,
            phone_number: str,
            lang: str,
            currency: str,
            limit: int,
            offset: int
            ) -> List[Provider]:
        pass

    @abc.abstractmethod
    def update(self, row: Provider):
        pass

    @abc.abstractmethod
    def delete(self, row_id: str):
        pass
