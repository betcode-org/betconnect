from datetime import datetime
from typing import Tuple, Dict, Any
import pytest
from pytest_mock import MockerFixture
from requests import Response
from betconnect import resources
from betconnect.endpoints import Account
from betconnect import exceptions


class TestAccount:
    def test_get_user_preferences(
        self,
        mocker: MockerFixture,
        mock_account_endpoint: Account,
        mock_get_user_preferences_response_response: Tuple[
            Response, Dict[str, Any], float
        ],
    ):
        get_user_preferences = mocker.patch(
            "betconnect.endpoints.account.Account._request",
            return_value=mock_get_user_preferences_response_response,
        )
        preferences = mock_account_endpoint.get_user_preferences()

        assert isinstance(preferences, resources.AccountPreferences)
        assert mock_account_endpoint.client.account_preferences == preferences
        get_user_preferences.assert_called()

    def test_get_balance(
        self,
        mocker: MockerFixture,
        mock_account_endpoint: Account,
        mock_get_balance_response: Tuple[Response, Dict[str, Any], float],
    ):
        get_balance = mocker.patch(
            "betconnect.endpoints.account.Account._request",
            return_value=mock_get_balance_response,
        )
        balance = mock_account_endpoint.get_balance()
        assert isinstance(balance, resources.Balance)
        assert mock_account_endpoint.client.account_balance == balance
        get_balance.assert_called()

    # noinspection SpellCheckingInspection
    def test_login(
        self,
        mocker: MockerFixture,
        mock_account_endpoint: Account,
        mock_login_response: Tuple[Response, Dict[str, Any], float],
        mock_login_failure_response: Tuple[Response, Dict[str, Any], float],
        mock_account_preferences_resource,
        mock_balance_resource,
    ):
        login_request = mocker.patch(
            "betconnect.endpoints.account.Account._post",
            return_value=mock_login_response,
        )
        get_user_preferences = mocker.patch(
            "betconnect.endpoints.account.Account.get_user_preferences",
            return_value=mock_account_preferences_resource,
        )
        get_balance = mocker.patch(
            "betconnect.endpoints.account.Account.get_balance",
            return_value=mock_balance_resource,
        )

        login = mock_account_endpoint.login()
        assert isinstance(login, resources.Login)
        login_request.assert_called_with(method_uri="api/v2/login")
        assert isinstance(mock_account_endpoint.client.login_date, datetime)
        assert isinstance(mock_account_endpoint.client.login_expiry_check, datetime)
        assert isinstance(mock_account_endpoint.client.next_refresh_time, datetime)
        assert (
            mock_account_endpoint.client._token
            == "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySUQiOiJhNmExZWI5MS02MjE3LTRlMGMtYjc1OS1mYmNhYTJiN2E4YWMiLCJsYXN0X3JlZnJlc2giOjE2Mzk4NDk2NzguODAzODYzLCJleHAiOjE2Mzk4Nzg0Nzh9.SiH-iupnvhMXqFjIQuhnXS-YcbxKFXTwowRfytdlrBw"
        )
        assert (
            mock_account_endpoint.client.session.headers["X-AUTH-TOKEN"]
            == "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySUQiOiJhNmExZWI5MS02MjE3LTRlMGMtYjc1OS1mYmNhYTJiN2E4YWMiLCJsYXN0X3JlZnJlc2giOjE2Mzk4NDk2NzguODAzODYzLCJleHAiOjE2Mzk4Nzg0Nzh9.SiH-iupnvhMXqFjIQuhnXS-YcbxKFXTwowRfytdlrBw"
        )

        assert isinstance(
            mock_account_endpoint.client.account_preferences,
            resources.AccountPreferences,
        )
        assert isinstance(
            mock_account_endpoint.client.account_balance, resources.Balance
        )

        login_request.assert_called()
        get_user_preferences.assert_called()
        get_balance.assert_called()

        login_request_failure = mocker.patch(
            "betconnect.endpoints.account.Account._post",
            return_value=mock_login_failure_response,
        )
        with pytest.raises(exceptions.FailedLogin):
            mock_account_endpoint.login()

        login_request_failure.assert_called()

    def test_logout(
        self,
        mocker: MockerFixture,
        mock_account_endpoint: Account,
        mock_login_response: Tuple[Response, Dict[str, Any], float],
        mock_logout_response: Tuple[Response, Dict[str, Any], float],
    ):
        login_request = mocker.patch(
            "betconnect.endpoints.account.Account._post",
            return_value=mock_login_response,
        )
        mock_account_endpoint.login()
        logout_request = mocker.patch(
            "betconnect.endpoints.account.Account._post",
            return_value=mock_logout_response,
        )
        mock_account_endpoint.logout()
        assert mock_account_endpoint.client.login_date is None
        assert mock_account_endpoint.client.login_expiry_check is None
        assert mock_account_endpoint.client.next_refresh_time is None
        assert mock_account_endpoint.client._token is None
        assert "X-AUTH-TOKEN" not in mock_account_endpoint.client.session.headers
        login_request.assert_called()
        logout_request.assert_called()

    def test_refresh_session_token(
        self,
        mocker: MockerFixture,
        mock_account_endpoint: Account,
        mock_refresh_session_token_response: Tuple[Response, Dict[str, Any], float],
    ):
        login_request = mocker.patch(
            "betconnect.endpoints.account.Account._post",
            return_value=mock_refresh_session_token_response,
        )
        status = mock_account_endpoint.refresh_session_token()
        assert isinstance(status, resources.Login)
        login_request.assert_called()

    def test__post(
        self,
        mocker: MockerFixture,
        mock_account_endpoint: Account,
        mock_login_response: Tuple[Response, Dict[str, Any], float],
    ):
        post = mocker.patch(
            "requests.sessions.Session.post", return_value=mock_login_response[0]
        )
        mock_account_endpoint._post(method_uri="test")
        post.assert_called()

    def test___call__(self, mocker: MockerFixture, mock_account_endpoint: Account):
        login = mocker.patch("betconnect.endpoints.account.Account.login")
        mock_account_endpoint()
        login.assert_called()
