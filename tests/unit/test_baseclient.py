from datetime import datetime
from requests import Session
from betconnect.baseclient import BaseClient
from betconnect.enums import Environment
from betconnect import config


class TestBaseClient:
    def test___init__(self):
        client = BaseClient(
            username="test",
            password="123",
            api_key="456",
            environment=Environment.STAGING,
            personalised_production_url="https://jimbob.betconnect.com/",
        )
        assert isinstance(client.session, Session)
        assert client._username == "test"
        assert client._password == "123"
        assert client._api_key == "456"
        assert client._environment == Environment.STAGING
        assert client.session.headers["X-API-KEY"] == "456"
        assert isinstance(client.uri, str)
        assert client.logged_in is False
        assert client.login_date is None
        assert client.login_expiry_check is None
        assert client._token is None
        assert client.session_timeout == 28800

    def test__update_client_session(self, mock_base_client):
        mock_base_client._update_client_session()
        assert isinstance(mock_base_client.session, Session)
        assert mock_base_client.session.headers["X-API-KEY"] == "456"
        assert isinstance(mock_base_client.login_expiry_check, datetime)
        assert mock_base_client.session.auth == (
            mock_base_client._username,
            mock_base_client._password,
        )

        new_session = Session()
        new_session.auth = ("new_user", "new_password")
        mock_base_client._update_client_session(new_session)
        assert mock_base_client.session.auth == ("new_user", "new_password")

    def test__set_endpoint_uris(self, mock_base_client):
        mock_base_client._set_endpoint_uris(environment=Environment.STAGING)
        assert mock_base_client.uri == config.DEFAULT_STAGING_URL
        mock_base_client._set_endpoint_uris(environment=Environment.PRODUCTION)
        assert mock_base_client.uri == mock_base_client._personalised_production_url

    def test_process_login(self, mock_base_client):
        mock_base_client.process_login(token="test_token")
        assert isinstance(mock_base_client.login_date, datetime)
        assert isinstance(mock_base_client.login_expiry_check, datetime)
        assert mock_base_client._token == "test_token"
        assert mock_base_client.session.headers["X-AUTH-TOKEN"] == "test_token"
