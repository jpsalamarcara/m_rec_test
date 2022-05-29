import pytest

from jeo_services.core.adapters.mongo.models.provider import ProviderCollection
from jeo_services.core.adapters.mongo.provider import MongoProviderAdapter
from jeo_services.core.domain.provider import Provider
from jeo_services.dependency_injection import factory


@pytest.fixture(scope='module')
def clean_provider_db():
    for row in ProviderCollection.objects:
        row.delete()


@pytest.fixture(scope='module')
def instance(clean_provider_db):
    return factory.get(MongoProviderAdapter)


test_data = [
    (dict(name='juan', email='jsalamanca@mimail.com', phone_number='+57 60 320 312 9973')),
    (dict(name='juan', email='jsalamanca@mimail.co', phone_number='+57 60 320 312 9973')),
    (dict(name='juanito', email='juan123@mimail.com', phone_number='+57 60 320 312 9973')),
    (dict(name='jhon', email='jsalamanca@mimail.es', phone_number='+57 60 320 312 9973')),
    (dict(name='jp', email='jsalamanca@mimail.us', phone_number='+57 60 320 312 9973')),
]


@pytest.mark.parametrize('case', test_data)
def test_add(instance, case):
    row = Provider(**case)
    instance.add(row)


@pytest.mark.parametrize('case', test_data)
def test_get(instance, case):
    output = instance.get(**case)
    assert len(output) == 1
    assert output[0].row_id is not None


@pytest.mark.parametrize('case', test_data)
def test_update(instance, case):
    output = instance.get(**case)
    prev = output[0]
    prev.lang = 'es'
    instance.update(prev)
    output = instance.get(**case)
    assert output[0].lang == 'es'


@pytest.mark.parametrize('case', test_data)
def test_delete(instance, case):
    output = instance.get(**case)
    prev = output[0]
    instance.delete(prev.row_id)
    output = instance.get(**case)
    assert len(output) == 0
