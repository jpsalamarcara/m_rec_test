import pytest as pytest
from fastapi.testclient import TestClient

from jeo_services.transport.rest.entrypoint import app


@pytest.fixture(scope='package')
def api_client():
    return TestClient(app)
