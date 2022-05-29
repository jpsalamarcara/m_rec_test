import uuid

import pytest

from jeo_services.core.adapters.mongo.models.provider import ProviderCollection


@pytest.fixture(scope='module')
def clean_db():
    for row in ProviderCollection.objects:
        row.delete()


@pytest.fixture(scope='module')
def post_new_provider(api_client, clean_db):
    row = dict(name='juan', email='jsalamanca@mimail.com', phone_number='+57 60 320 312 9973')
    response = api_client.post('/v1/providers/', json=row)
    return response


def test_post_provider(post_new_provider):
    assert post_new_provider.status_code == 201
    assert post_new_provider.content is not None
    content = post_new_provider.json()
    assert uuid.UUID(hex=content) is not None


def test_get_provider(api_client, post_new_provider):
    assert post_new_provider.status_code == 201
    response = api_client.get('/v1/providers/')
    assert response.status_code == 200
    content = response.json()
    for prov in content:
        assert type(prov) == dict


def test_put_provider(api_client, post_new_provider):
    assert post_new_provider.status_code == 201
    response = api_client.get('/v1/providers/')
    assert response.status_code == 200
    content = response.json()
    assert len(content) == 1
    provider = content[0]
    provider['lang'] = 'es'
    response = api_client.put(f'/v1/providers/{provider.pop("row_id")}', json=provider)
    assert response.status_code == 201


def test_delete_provider(api_client, post_new_provider):
    assert post_new_provider.status_code == 201
    row_id = post_new_provider.json()
    response = api_client.delete(f'/v1/providers/{row_id}')
    assert response.status_code == 204
