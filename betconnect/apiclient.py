from .baseclient import BaseClient
from requests.sessions import Session
from betconnect import endpoints
from betconnect.enums import Environment
from typing import Optional


class APIClient(BaseClient):
    def __init__(
        self,
        username: str,
        password: str,
        api_key: str,
        personalised_production_url: str,
        environment: Environment = Environment.PRODUCTION,
        session: Optional[Session] = None,
    ):
        """
        APIClient is used to make request to the betconnect API
        :param username: your betconnect username (string)
        :param password: your betconnect password (string)
        :param api_key: your betconnect api key (string)
        :param personalised_production_url: A production user supplied url. (account manager will supply this)
        :param environment: the environment endpoint you want to send requests to (enum Environment)
        :param session: Session object used in request default None. Session created if None with auth and headers handled.
        """
        self.betting = endpoints.Betting(self)
        self.account = endpoints.Account(self)
        super(APIClient, self).__init__(
            username=username,
            password=password,
            session=session,
            environment=environment,
            api_key=api_key,
            personalised_production_url=personalised_production_url,
        )
