from betconnect.endpoints.login import Login
from pytest_mock import mocker
from typing import Tuple, Dict, Any
from requests import Response
from datetime import datetime
from betconnect import resources
import pytest


class TestLogin:

    def test_login(self, mocker, mock_login_endpoint: Login, mock_login_response: Tuple[
        Response, Dict[str, Any], float], mock_login_failure_response: Tuple[
        Response, Dict[str, Any], float]):
        login_request = mocker.patch('betconnect.endpoints.login.Login.post', return_value=mock_login_response)
        login = mock_login_endpoint.login()
        assert isinstance(login, resources.Login)
        login_request.assert_called_with(method_uri='api/v2/login')
        assert isinstance(mock_login_endpoint.client.login_date, datetime)
        assert isinstance(mock_login_endpoint.client.login_expiry_check, datetime)
        assert isinstance(mock_login_endpoint.client.login_status_check, datetime)
        assert mock_login_endpoint.client._token == 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySUQiOiJhNmExZWI5MS02MjE3LTRlMGMtYjc1OS1mYmNhYTJiN2E4YWMiLCJsYXN0X3JlZnJlc2giOjE2MzQwMjE3NzQuNzY0MjU2LCJleHAiOjE2MzQwNTA1NzR9.WStmcYzGb5P6hu8pECYkbZB8ToHfOa4QFzZDJVrYJgI'
        assert mock_login_endpoint.client.session.headers[
                   "X-AUTH-TOKEN"] == 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySUQiOiJhNmExZWI5MS02MjE3LTRlMGMtYjc1OS1mYmNhYTJiN2E4YWMiLCJsYXN0X3JlZnJlc2giOjE2MzQwMjE3NzQuNzY0MjU2LCJleHAiOjE2MzQwNTA1NzR9.WStmcYzGb5P6hu8pECYkbZB8ToHfOa4QFzZDJVrYJgI'
        login_request = mocker.patch('betconnect.endpoints.login.Login.post', return_value=mock_login_failure_response)
        with pytest.raises(Exception) as e:
            mock_login_endpoint.login()

    def test_logout(self, mocker, mock_login_endpoint: Login, mock_login_response: Tuple[
        Response, Dict[str, Any], float], mock_logout_response: Tuple[
        Response, Dict[str, Any], float], mock_logout_failure_response: Tuple[
        Response, Dict[str, Any], float]):
        login_request = mocker.patch('betconnect.endpoints.login.Login.post', return_value=mock_login_response)
        mock_login_endpoint.login()
        logout_request = mocker.patch('betconnect.endpoints.login.Login.post', return_value=mock_logout_response)
        mock_login_endpoint.logout()
        assert mock_login_endpoint.client.login_date is None
        assert mock_login_endpoint.client.login_expiry_check is None
        assert mock_login_endpoint.client.login_status_check is None
        assert mock_login_endpoint.client._token is None
        assert "X-AUTH-TOKEN" not in mock_login_endpoint.client.session.headers


    def test_status(self, mock_login_endpoint: Login):
        raise Exception('Return to ')