from betconnect.apiclient import APIClient
from betconnect import endpoints
class TestAPIClient:

    def test___init__(self):
        client = APIClient(username='test', password='123', api_key='456')
        assert client._username == 'test'
        assert client._password == '123'
        assert client._api_key == '456'
        assert isinstance(client.login, endpoints.Login)
        assert isinstance(client.configuration,endpoints.Configuration)
        assert isinstance(client.betting, endpoints.Betting)



