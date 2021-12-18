import logging
import time
from typing import Union, Tuple, Optional
import requests
from betconnect import resources
from .baseendpoint import BaseEndpoint
from betconnect import exceptions
import json

logger = logging.getLogger(__name__)

from tests.utils import save_data_to_pickle_file, save_json_to_file


class Account(BaseEndpoint):
    def get_user_preferences(
        self,
    ) -> Union[resources.AccountPreferences, resources.BaseRequestException]:
        """
        Retrieves user preferences for the current account
        :return: Account preference resource or the request exception resource
        """

        (response, response_json, elapsed_time) = self._request(
            method_uri=f"{self.api_version}/get_user_preferences", authenticated=True
        )

        account_preferences = self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.AccountPreferences,
            elapsed_time=elapsed_time,
        )
        if isinstance(account_preferences, resources.AccountPreferences):
            self.client.set_account_preferences(account_preferences=account_preferences)
        elif isinstance(account_preferences, resources.BaseRequestException):
            logger.warning(
                f"Issue trying to update the account balance. Request message: {account_preferences.message}"
            )
        return account_preferences

    def get_balance(self) -> Union[resources.Balance, resources.BaseRequestException]:
        """
        Gets the account balance
        :return: The balance resource or the request exception resource
        """

        (response, response_json, elapsed_time) = self._request(
            method_uri=f"{self.api_version}/get_balance", authenticated=True
        )


        balance = self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.Balance,
            elapsed_time=elapsed_time,
        )
        if isinstance(balance, resources.Balance):
            self.client.set_account_balance(account_balance=balance)
        elif isinstance(balance, resources.BaseRequestException):
            logger.warning(
                f"Issue trying to update the account balance. Request message: {balance.message}"
            )
        return balance

    def login(self) -> resources.Login:
        """
        Logs the user in with the username and password supplied to the client
        :return: Login resource
        """

        (response, response_json, elapsed_time) = self._post(
            method_uri=f"{self.api_version}/login"
        )

        data = response_json.get("data")

        if data:
            if "token" in data:
                self.client.process_login(data["token"])
                login_resource = resources.Login(**response_json)

                if self.client.account_preferences is None:
                    # try and get account preferences as well
                    account_preferences: Union[
                        resources.AccountPreferences, resources.BaseRequestException
                    ] = self.get_user_preferences()

                    if isinstance(account_preferences, resources.AccountPreferences):
                        self.client.set_account_preferences(
                            account_preferences=account_preferences
                        )
                    elif isinstance(
                        account_preferences, resources.BaseRequestException
                    ):
                        logger.warning(
                            f"Issue trying to update the account balance. Request message: {account_preferences.message}"
                        )

                if self.client.account_balance is None:
                    balance: Union[
                        resources.Balance, resources.BaseRequestException
                    ] = self.get_balance()

                    if isinstance(balance, resources.Balance):
                        self.client.set_account_balance(account_balance=balance)
                    elif isinstance(balance, resources.BaseRequestException):
                        logger.warning(
                            f"Issue trying to update the account balance. Request message: {balance.message}"
                        )

                return login_resource

            else:
                raise exceptions.LoginMissingTokenInResponse()
        else:
            raise exceptions.FailedLogin(username=self.client.username)

    def logout(self) -> None:
        """
        Logs the client out, removes all tokens.
        :return:
        """

        (response, response_json, elapsed_time) = self._post(
            method_uri=f"{self.api_version}/logout"
        )

        if response.status_code == 200:
            self.client.process_logout()
        else:
            logger.warning(f"There may have been an issue logging out. Expected status code 200, got status code {response.status_code}")

    def refresh_session_token(self) -> Optional[resources.Login]:
        """
        Provides a refresh token for authentication
        :return: returns Login resource
        """

        (response, response_json, elapsed_time) = self._post(
            method_uri=f"{self.api_version}/status"
        )

        data = response_json.get("data")

        if data:
            if "refresh_token" in data:
                self.client.process_login(data["refresh_token"])
                return resources.Login(
                    **{
                        "data": {"token": data["refresh_token"]},
                        "message": response_json.get("message"),
                    }
                )
            else:
                logger.debug("No refresh token supplied")


    # noinspection PyProtectedMember
    def _post(
        self, method_uri: str, params: dict = None, authenticated: bool = True
    ) -> Tuple[requests.Response, dict, float]:
        """
        Post method
        :param str method_uri: uri to be used, defined by each function.
        :param dict params: Query Params to be used in request
        :return Tuple[dict, float]: re
        """
        params = params if params else {}

        uri = self.client.uri + method_uri
        time_sent = time.time()

        try:
            logger.debug(f"requesting the data for f{uri}")

            response = self.session.post(uri, timeout=self._read_timeout)

        except requests.ConnectionError as e:
            raise exceptions.APIError(None, uri, params, e)
        except Exception as e:
            raise exceptions.APIError(None, uri, params, e)

        elapsed_time = time.time() - time_sent

        response_json = self._load_content(response)


        if self._check_status_code(response) is False:
            raise exceptions.UnexpectedResponseStatusCode(status_code=response.status_code,url=response.url)

        return response, response_json, elapsed_time

    def __call__(self, *args, **kwargs):
        return self.login()
