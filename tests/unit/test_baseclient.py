from betconnect.baseclient import BaseClient
from betconnect.enums import Envirnoment
from requests import Session
from datetime import datetime
from betconnect.config import STAGING_URI,PRODUCTION_URI

class TestBaseClient:

    def test___init__(self):
        client = BaseClient(username='test',
                            password='123',
                            api_key="456",
                            environment=Envirnoment.STAGING
                            )
        assert isinstance(client.session, Session)
        client._username == 'test'
        client._password == '123'
        client._api_key == '456'
        client._environment == Envirnoment.STAGING
        assert client.session.headers["X-API-KEY"] == '456'
        assert isinstance(client.uri, str)
        assert client.logged_in is False
        assert client.login_date is None
        assert client.login_expiry_check is None
        assert client._token is None

    def test__update_client_session(self, mock_base_client):
        mock_base_client._update_client_session()
        assert isinstance(mock_base_client.session, Session)
        assert mock_base_client.session.headers["X-API-KEY"] == '456'
        assert isinstance(mock_base_client.login_expiry_check, datetime)
        assert mock_base_client.session.auth == ( mock_base_client._username,  mock_base_client._password)


        new_session = Session()
        new_session.auth = ('new_user','new_password')
        mock_base_client._update_client_session(new_session)
        assert mock_base_client.session.auth == ( 'new_user', 'new_password')

    def test__set_endpoint_uris(self, mock_base_client):
        mock_base_client._set_endpoint_uris(environment=Envirnoment.STAGING)
        assert mock_base_client.uri == STAGING_URI
        mock_base_client._set_endpoint_uris(environment=Envirnoment.PRODUCTION)
        assert mock_base_client.uri == PRODUCTION_URI

    def test_process_login(self, mock_base_client):
        mock_base_client.process_login(token='test_token')
        assert isinstance(mock_base_client.login_date, datetime)
        assert isinstance(mock_base_client.login_expiry_check, datetime)
        assert mock_base_client._token == 'test_token'
        assert mock_base_client.session.headers["X-AUTH-TOKEN"] == 'test_token'