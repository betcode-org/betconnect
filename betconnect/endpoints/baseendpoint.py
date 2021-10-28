from __future__ import annotations
from typing import TYPE_CHECKING, Union, List, Type
from datetime import datetime, timedelta
from betconnect.resources.baseresource import BaseResource
import requests
import json
import logging
import time
from requests import Response
from betconnect import resources
from betconnect.exceptions import APIError

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from betconnect.baseclient import BaseClient


class BaseEndpoint:
    _read_timeout = 100

    def __init__(self,
                 client: BaseClient):
        self.client = client

    @property
    def session(self):
        return self.client.session

    @property
    def today(self):
        return datetime.utcnow()

    @property
    def tomorrow(self):
        return datetime.utcnow() + timedelta(days=1)

    def request(
            self,
            method_uri: str,
            params: dict = None,
            authenticated: bool = False
    ) -> (dict, float):
        """
        :param str uri: uri to be used, defined by each function.
        :param dict params: Query Params to be used in request

        """

        uri = self.client.uri + method_uri
        time_sent = time.time()
        logger.info(f"Requesting the data for {uri}")

        if authenticated and self.client.logged_in is False:
            logger.info(f"Need to be logged in before accessing{uri}. Attemping login with supplied credentials")
            self.client.login()

        try:
            response = self.session.get(uri, timeout=self._read_timeout, params=params)
        except requests.ConnectionError as e:
            raise APIError(None, uri, params, e)
        except Exception as e:
            raise APIError(None, uri, params, e)
        elapsed_time = time.time() - time_sent

        response_json = self._load_content(response)

        return response, response_json, elapsed_time

    def post(
            self,
            method_uri: str,
            data: dict,
            authenticated: bool = True
    ) -> (dict, float):
        """
        :param str uri: uri to be used, defined by each function.
        :param dict data: body of data

        """
        uri = self.client.uri + method_uri
        time_sent = time.time()
        logger.info(f"posting the data for {uri}")

        if authenticated and self.client.logged_in is False:
            logger.info(f"Need to be logged in before accessing{uri}. Attemping login with supplied credentials")
            self.client.login()

        try:
            response = self.session.post(uri, timeout=self._read_timeout, json=data)
        except requests.ConnectionError as e:
            raise APIError(None, uri, data, e)
        except Exception as e:
            raise APIError(None, uri, data, e)
        elapsed_time = time.time() - time_sent

        response_json = self._load_content(response)

        return response, response_json, elapsed_time

    def patch(
            self,
            method_uri: str,
            data: dict
    ) -> (dict, float):
        """
        :param str uri: uri to be used, defined by each function.
        :param dict data: body of data

        """
        uri = self.client.uri + method_uri
        time_sent = time.time()
        logger.info(f"posting the data for {uri}")

        if self.client.logged_in is False:
            logger.info(f"Need to be logged in before accessing{uri}. Attemping login with supplied credentials")
            self.client.login()

        try:
            response = self.session.patch(uri, timeout=self._read_timeout, json=data)
        except requests.ConnectionError as e:
            raise APIError(None, uri, data, e)
        except Exception as e:
            raise APIError(None, uri, data, e)
        elapsed_time = time.time() - time_sent

        response_json = self._load_content(response)

        return response, response_json, elapsed_time

    def _process_request_exception(self, response: requests.Response,
                                   response_json: dict) -> resources.BaseRequestException:
        logger.exception(f"Issue with request for: {response.url}, message: {response_json.get('message')}")
        return resources.BaseRequestException(
            message = response_json.get('message'),
            request_url = response.url,
            status_code = response.status_code
        )

    def _load_content(self, response: requests.Response):
        if response.headers['content-type'] in ['application/json', 'application/json; charset=utf-8']:
            return json.loads(response.content.decode("utf-8"))
        else:
            logger.error('Unregonised content encoding type')

    def process_response(
            self,
            response: requests.Response,
            response_json: Union[dict, list],
            resource: Type[BaseResource],
            elapsed_time: float
    ) -> Union[BaseResource, dict, list]:

        if self._check_status_code(response):
            if 'data' in response_json:
                data = response_json['data']

                logger.debug('It took {} s to request the data for url {}'.format(elapsed_time, response.url))

                if isinstance(data, dict):
                    return resource.create_from_dict(data)
                elif isinstance(data, list):
                    return [resource(**r) for r in data]
                else:
                    raise Exception('unkown response data type')
            elif 'message' in response_json:
                return resources.ResponseMessage(message=response_json.get('message'), status_code=response.status_code, request_url=response.url)
            else:
                raise Exception('Expected response json to contain data key')

        else:
            return self._process_request_exception(response, response_json)

    def _check_status_code(self, response: Response, codes: List[int] = []):
        """
        valid status codes {200, 400, 404}
        """
        return True if (response.status_code in codes) or (response.status_code == 200) else False
