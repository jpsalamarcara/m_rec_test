import uuid

import pytest

from jeo_services.core.adapters.mongo.models.service_area import ServiceAreaCollection


@pytest.fixture(scope='module')
def clean_db():
    for row in ServiceAreaCollection.objects:
        row.delete()


@pytest.fixture(scope='module')
def post_new_service_area(api_client, clean_db):
    row = dict(name='Somewhere',
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
                   ]],
               })
    response = api_client.post('/v1/service_areas/', json=row)
    return response


def test_post_service_area(post_new_service_area):
    assert post_new_service_area.status_code == 201
    assert post_new_service_area.content is not None
    content = post_new_service_area.json()
    assert uuid.UUID(hex=content) is not None


def test_get_service_area(api_client, post_new_service_area):
    assert post_new_service_area.status_code == 201
    response = api_client.get('/v1/service_areas/')
    assert response.status_code == 200
    content = response.json()
    for service in content:
        assert type(service) == dict


def test_put_service_area(api_client, post_new_service_area):
    assert post_new_service_area.status_code == 201
    response = api_client.get('/v1/service_areas/')
    assert response.status_code == 200
    content = response.json()
    assert len(content) == 1
    service = content[0]
    service['name'] = 'Somewhere in india'
    response = api_client.put(f'/v1/service_areas/{service.pop("row_id")}', json=service)
    assert response.status_code == 201


def test_delete_service_area(api_client, post_new_service_area):
    assert post_new_service_area.status_code == 201
    row_id = post_new_service_area.json()
    response = api_client.delete(f'/v1/service_areas/{row_id}')
    assert response.status_code == 204
