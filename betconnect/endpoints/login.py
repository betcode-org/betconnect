from .baseendpoint import BaseEndpoint
from betconnect import resources
import time
import logging
import requests
from typing import Union, List
from betconnect.exceptions import APIError

logger = logging.getLogger(__name__)



class Login(BaseEndpoint):
    _METHOD_URIS = {
        'login': 'api/v2/login',
        'logout': 'api/v2/logout',
        'status': 'api/v2/status'
    }

    def login(self) -> resources.Login:
        """
        Logs the user in withhe username and password supplied to the client
        :return: Login resource
        """
        method_uri = self._METHOD_URIS['login']

        (response, response_json, elapsed_time) = self.post(method_uri=method_uri)

        data = response_json.get('data')

        if data:
            if 'token' in data:
                self.client.process_login(data['token'])
                return resources.Login(**response_json)
            else:
                raise Exception('Missing login token')
        else:
            raise Exception(f"Unable to login with the supplied username and passweord")

    def logout(self) -> None:
        """
        Logs the client out, removes all tokens.
        :return: None
        """
        method_uri = self._METHOD_URIS['logout']

        (response, response_json, elapsed_time) = self.post(method_uri=method_uri)

        if response.status_code == 200:
            self.client.process_logout()

    def status(self) -> Union[resources.Login, None]:
        """
        Provides a refresh token for authentication
        :return: None
        """
        method_uri = self._METHOD_URIS['status']

        (response, response_json, elapsed_time) = self.post(method_uri=method_uri)

        data = response_json.get('data')

        if data:
            if 'refresh_token' in data:
                self.client.process_login(data['refresh_token'])
                return resources.Login(**{'data':{'token':data['refresh_token']}, 'message':response_json.get('message')})

    def post(
            self,
            method_uri: str,
            params: dict = None
    ) -> (dict, float):
        """
        :param str uri: uri to be used, defined by each function.
        :param dict params: Query Params to be used in request

        """

        uri = self.client.uri + method_uri
        time_sent = time.time()

        try:
            logger.debug(f"requesting the data for f{uri}")

            response = self.session.post(uri, timeout=self._read_timeout)

        except requests.ConnectionError as e:
            raise APIError(None, uri, params, e)
        except Exception as e:
            raise APIError(None, uri, params, e)

        elapsed_time = time.time() - time_sent

        try:
            response_json = self._load_content(response)
        except Exception as e:
            raise Exception(f"Issue loading content {response.text}")

        if self._check_status_code(response) is False:
            raise Exception(f"Unexpected status code {response.status_code}")

        return response, response_json, elapsed_time

    def _process_request_exception(self, response: requests.Response, response_json: dict):
        raise Exception(f"Issue with {response.url}, {response_json}")

    def __call__(self, *args, **kwargs):
        return self.login()
