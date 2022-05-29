import pytest

from jeo_services.core.adapters.mongo.service_area import compute_polygon_hash


@pytest.fixture
def coordinates():
    return [[
        [17.60083012593064, 78.18557739257812],
        [17.16834652544664, 78.19381713867188],
        [17.17490690610013, 78.739013671875],
        [17.613919673106714, 78.73489379882812],
        [17.60083012593064, 78.18557739257812]
    ]]


def test_compute_polygon_hash(coordinates):
    hash = compute_polygon_hash(coordinates)
    assert hash == '8160bffffffffff'
