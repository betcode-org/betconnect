from betconnect.endpoints import Configuration

class TestConfiguration:

    def test___init__(self, mock_api_client):
        configuration = Configuration(mock_api_client)
        assert configuration.client == mock_api_client

    def test_active_bookmakers(self, mock_configuration_endpoint):
        #TODO requires authentication
        mock_configuration_endpoint.active_bookmakers()
