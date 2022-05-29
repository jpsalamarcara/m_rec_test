from typing import List

from fastapi import APIRouter

from jeo_services.core.domain.provider import Provider

router = APIRouter()


@router.get('/', response_model=List[Provider])
def get_providers():
    return []
