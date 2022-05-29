import uuid

import pytest

from jeo_services.core.adapters.mongo.models.service_area import ServiceAreaCollection
from jeo_services.core.adapters.mongo.service_area import MongoServiceAreaAdapter
from jeo_services.core.domain.service_area import ServiceArea
from jeo_services.dependency_injection import factory


@pytest.fixture(scope='module')
def clean_service_area_db():
    for row in ServiceAreaCollection.objects:
        row.delete()


@pytest.fixture(scope='module')
def instance(clean_service_area_db):
    return factory.get(MongoServiceAreaAdapter)


@pytest.fixture(scope='module')
def service_row():
    row = ServiceArea(name='Somewhere',
                      price=1000.52,
                      provider_id=f'{uuid.uuid4()}',
                      polygon={
                          "type": "Polygon",
                          "coordinates": [[
                              [17.60083012593064, 78.18557739257812],
                              [17.16834652544664, 78.19381713867188],
                              [17.17490690610013, 78.739013671875],
                              [17.613919673106714, 78.73489379882812],
                              [17.60083012593064, 78.18557739257812]
                          ]]
                      })
    return row


def test_add(instance: MongoServiceAreaAdapter, service_row):
    instance.add(service_row)


def test_get(instance: MongoServiceAreaAdapter):
    lat, long = 17.3734, 78.4738
    output = instance.get_by_lat_long(lat, long, limit=10, offset=0)
    assert len(output) == 1
    lat, long = 4.640252, -74.115580
    output = instance.get_by_lat_long(lat, long, limit=10, offset=0)
    assert len(output) == 0
