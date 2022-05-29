import uuid
from typing import List

from fastapi import APIRouter, Depends

from jeo_services.core.domain.provider import Provider
from jeo_services.core.ports.provider import ProviderPort
from jeo_services.dependency_injection import factory

router = APIRouter()


def get_provider_adapter():
    return factory.get(ProviderPort)


@router.get('/', response_model=List[Provider], status_code=200)
def get_providers(row_id: str = None, name: str = None, email: str = None, phone_number: str = None, lang: str = None,
                  currency: str = None, limit: int = 100,
                  offset: int = 0, adapter: ProviderPort = Depends(get_provider_adapter)):
    output = adapter.get(row_id, name, email, phone_number, lang, currency, limit, offset)
    return output


@router.post('/', response_model=uuid.UUID, status_code=201)
def add_provider(row: Provider, adapter: ProviderPort = Depends(get_provider_adapter)):
    output = adapter.add(row)
    return output


@router.put('/{row_id}', status_code=201)
def update_provider(
        row_id: uuid.UUID,
        row: Provider,
        adapter: ProviderPort = Depends(get_provider_adapter)):
    row.row_id = row_id
    adapter.update(row)
    return 'OK'


@router.delete('/{row_id}', status_code=204)
def delete_provider(
        row_id: uuid.UUID,
        adapter: ProviderPort = Depends(get_provider_adapter)):
    adapter.delete(row_id)
    return 'OK'
