from __future__ import annotations
from typing import TYPE_CHECKING, Union, List, Type, Tuple
from datetime import datetime, timedelta
from betconnect.resources.baseresource import BaseResource
import requests
import json
import logging
import time
from requests import Response
from betconnect import resources
from betconnect.exceptions import APIError
from uuid import UUID
from betconnect import config

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from betconnect.apiclient import APIClient


class BaseEndpoint:
    _read_timeout = config.CLIENT_READOUT_TIME_SECS

    def __init__(self, client: APIClient):
        self.client = client

    @property
    def session(self) -> requests.Session:
        return self.client.session

    @property
    def today(self):
        return datetime.utcnow()

    @property
    def api_version(self) -> str:
        return self.client.api_version

    @property
    def tomorrow(self):
        return datetime.utcnow() + timedelta(days=1)

    def _request(
        self, method_uri: str, params: dict = None, authenticated: bool = False
    ) -> Tuple[requests.Response, dict, float]:
        """
        :param str method_uri: uri to be used, defined by each function.
        :param dict params: Query Params to be used in request
        :param bool authenticated: If the request requires the user to be logged in
        :return: tuple of the Response, dict (json_dict), float (elapsed time)
        """
        params = params if params else {}

        uri = self.client.uri + method_uri
        time_sent = time.time()

        logger.debug(f"Requesting the data for {uri}")

        if authenticated and self.client.logged_in is False:
            logger.info(
                f"Need to be logged in before accessing{uri}. Attempting login with supplied credentials"
            )
            self.client.account.login()

        try:
            response = self.session.get(uri, timeout=self._read_timeout, params=params)
        except requests.ConnectionError as e:
            raise APIError(None, uri, params, e)
        except Exception as e:
            raise APIError(None, uri, params, e)
        elapsed_time = time.time() - time_sent

        response_json = self.load_json_content(response)

        return response, response_json, elapsed_time

    def _post(
        self, method_uri: str, data: dict, authenticated: bool = True
    ) -> Tuple[requests.Response, dict, float]:
        """
        :param str method_uri: uri to be used, defined by each function.
        :param dict data: body of data
        :param bool authenticated: If the request requires the user to be logged in
        :return: tuple of the Response, dict (json_dict), float (elapsed time)
        """
        uri = self.client.uri + method_uri
        time_sent = time.time()
        logger.debug(f"posting the data for {uri}")

        if authenticated and self.client.logged_in is False:
            logger.info(
                f"Need to be logged in before accessing{uri}. Attempting login with supplied credentials"
            )
            self.client.account.login()

        try:
            response = self.session.post(uri, timeout=self._read_timeout, json=data)
        except requests.ConnectionError as e:
            raise APIError(None, uri, data, e)
        except Exception as e:
            raise APIError(None, uri, data, e)
        elapsed_time = time.time() - time_sent

        response_json = self.load_json_content(response)

        return response, response_json, elapsed_time

    def _patch(
        self, method_uri: str, data: dict
    ) -> Tuple[requests.Response, dict, float]:
        """
        :param str method_uri: uri to be used, defined by each function.
        :param dict data: body of data
        :return: tuple of the Response, dict (json_dict), float (elapsed time)
        """
        uri = self.client.uri + method_uri
        time_sent = time.time()
        logger.debug(f"patching the data for {uri}")

        if self.client.logged_in is False:
            logger.info(
                f"Need to be logged in before accessing{uri}. Attempting login with supplied credentials"
            )
            self.client.account.login()

        try:
            response = self.session.patch(uri, timeout=self._read_timeout, json=data)
        except requests.ConnectionError as e:
            raise APIError(None, uri, data, e)
        except Exception as e:
            raise APIError(None, uri, data, e)
        elapsed_time = time.time() - time_sent

        response_json = self.load_json_content(response)

        return response, response_json, elapsed_time

    @staticmethod
    def process_request_exception(
        response: requests.Response, response_json: dict
    ) -> resources.BaseRequestException:
        logger.exception(
            f"Issue with request for: {response.url}, message: {response_json.get('message')}"
        )
        return resources.BaseRequestException(
            message=response_json.get("message"),
            request_url=response.url,
            status_code=response.status_code,
        )

    @staticmethod
    def check_bet_request_id(bet_request_id: UUID):
        if isinstance(bet_request_id, UUID) is False:
            raise Exception(f"Incorrect UUID supplied for the bet_request_id")

    @staticmethod
    def load_json_content(response: requests.Response):
        if response.headers["content-type"] in [
            "application/json",
            "application/json; charset=utf-8",
        ]:
            return json.loads(response.content.decode("utf-8"))
        else:
            logger.exception("Unrecognised content encoding type")

    def process_response(
        self,
        response: requests.Response,
        response_json: Union[dict, list],
        resource: Type[BaseResource],
        elapsed_time: float,
    ) -> Union[BaseResource, dict, list, resources.BaseRequestException]:
        """
        Process the endpoint function responses from betconnect, parsing the data to the relevant resources
        :param response: The request response
        :param response_json: The json data from the response
        :param resource: The resource to parse to the data too
        :param elapsed_time: The time taken to make the request
        :return: A resource for the response data or a BaseRequestException if BetConnect has detected an issue with
        the request.
        """

        if self.check_status_code(response):
            if "data" in response_json:
                data = response_json["data"]

                logger.debug(
                    f"It took {elapsed_time} s to request the data for url {response.url}"
                )

                if isinstance(data, dict):
                    return resource.create_from_dict(data)
                elif isinstance(data, list):
                    if len(data) == 0:
                        logger.info(f"No data could be found for {response.url}")
                    return [resource.create_from_dict(r) for r in data]
                else:
                    raise Exception(
                        "Unkown response data type"
                    )  # TODO add specific Exception Here
            elif "message" in response_json:
                return resources.ResponseMessage(
                    message=response_json.get("message"),
                    status_code=response.status_code,
                    request_url=response.url,
                )
            else:
                raise Exception("Expected response json to contain data key")

        else:
            return self.process_request_exception(response, response_json)

    def _put(
        self, method_uri: str, data: dict, authenticated: bool = True
    ) -> Tuple[requests.Response, dict, float]:
        """
        :param str method_uri: uri to be used, defined by each function.
        :param dict data: body of data
        :param bool authenticated: If the request requires the user to be logged in
        :return: tuple of the Response, dict (json_dict), float (elapsed time)
        """
        uri = self.client.uri + method_uri
        time_sent = time.time()
        logger.debug(f"putting the data for {uri}")

        if authenticated and self.client.logged_in is False:
            logger.info(
                f"Need to be logged in before accessing{uri}. Attempting login with supplied credentials"
            )
            self.client.account.login()

        try:
            response = self.session.put(uri, timeout=self._read_timeout, json=data)
        except requests.ConnectionError as e:
            raise APIError(None, uri, data, e)
        except Exception as e:
            raise APIError(None, uri, data, e)
        elapsed_time = time.time() - time_sent

        response_json = self.load_json_content(response)

        return response, response_json, elapsed_time

    @staticmethod
    def check_status_code(response: Response, codes: List[int] = None) -> bool:
        """
        Checks the reponse for valid status codes. Valid status codes {200} + supplied codes
        :param response: A response resource (from the request)
        :param codes: A list of accepted codes
        :return: A bool validating the code
        """
        codes = codes if codes else []
        return (
            True
            if (response.status_code in codes) or (response.status_code == 200)
            else False
        )
