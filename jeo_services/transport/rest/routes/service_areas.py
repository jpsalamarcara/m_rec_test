import uuid
from typing import List

from fastapi import APIRouter, Depends

from jeo_services.core.domain.service_area import ServiceArea
from jeo_services.core.ports.service_area import ServiceAreaPort
from jeo_services.dependency_injection import factory

router = APIRouter()


def get_service_area_adapter():
    return factory.get(ServiceAreaPort)


@router.get('/', response_model=List[ServiceArea], status_code=200)
def get_areas(row_id: str = None,
              name: str = None,
              price: float = None,
              provider_id: str = None,
              limit: int = 100,
              offset: int = 0,
              adapter: ServiceAreaPort = Depends(get_service_area_adapter)):
    output = adapter.get(row_id=row_id, name=name, provider_id=provider_id, price=price, limit=limit, offset=offset)
    return output


@router.post('/', response_model=uuid.UUID, status_code=201)
def add_service_area(row: ServiceArea, adapter: ServiceAreaPort = Depends(get_service_area_adapter)):
    output = adapter.add(row)
    return output


@router.put('/{row_id}', status_code=201)
def update_service_area(
        row_id: uuid.UUID,
        row: ServiceArea,
        adapter: ServiceAreaPort = Depends(get_service_area_adapter)):
    row.row_id = row_id
    adapter.update(row)
    return 'OK'


@router.delete('/{row_id}', status_code=204)
def delete_service_area(
        row_id: uuid.UUID,
        adapter: ServiceAreaPort = Depends(get_service_area_adapter)):
    adapter.delete(row_id)
    return 'OK'
