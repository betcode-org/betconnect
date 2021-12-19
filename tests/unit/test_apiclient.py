from betconnect.apiclient import APIClient
from betconnect import endpoints


class TestAPIClient:
    def test___init__(self):
        client = APIClient(
            username="test",
            password="123",
            api_key="456",
            personalised_production_url="https://jimbob.betconnect.com/",
        )
        assert client._username == "test"
        assert client._password == "123"
        assert client._api_key == "456"
        assert client._personalised_production_url == "https://jimbob.betconnect.com/"
        assert isinstance(client.account, endpoints.Account)
        assert isinstance(client.betting, endpoints.Betting)
