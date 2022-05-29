

def test_get_provider(api_client):
    response = api_client.get('/v1/providers/')
    assert response.status_code == 200
