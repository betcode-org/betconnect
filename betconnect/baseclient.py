from requests.sessions import Session
from datetime import datetime, timedelta
from .enums import Envirnoment
from .config import PRODUCTION_URI, STAGING_URI
from typing import Union


class BaseClient:

    def __init__(self,
                 username: str,
                 password: str,
                 api_key: str,
                 environment: Envirnoment = Envirnoment.PRODUCTION,
                 session: Session = None
                 ):
        """
        :param username: your betconnect username (string)
        :param password: your betconnect password (string)
        :param api_key: your betconnect api key (string)
        :param environment: the environment endpoint you want to send requests to (enum Environent)
        :param session: Session object used in request default None. Session created if None with auth and headers handled.
        """
        self._username = username
        self._password = password
        self._api_key = api_key
        self._environment = environment
        self._update_client_session(session)
        self._set_endpoint_uris(environment)
        self.login_date = None
        self.login_expiry_check = None
        self.login_status_check = None
        self._token = None

    @property
    def logged_in(self):
        try:
            return True if datetime.utcnow() < self.login_expiry_check else False
        except TypeError as e:
            return False

    def _update_client_session(self, session: Union[None, Session] = None):
        """
        Updates the client session with auth details
        :param session: a request Session
        :return: None
        """
        if session:
            self.session = session
            if session.auth is None:
                self.session.auth = (self._username, self._password)
        else:
            self.session = Session()
            self.session.auth = (self._username, self._password)
        self.session.headers.update({"X-API-KEY": self._api_key})
        self.login_expiry_check = datetime.utcnow()

    def _set_endpoint_uris(self, environment: Envirnoment):
        """
        Sets the uri for which requests are sent to
        :param environment: enum Environment
        :return: None
        """
        if environment == Envirnoment.PRODUCTION:
            self.uri = PRODUCTION_URI
        elif environment == Envirnoment.STAGING:
            self.uri = STAGING_URI
        else:
            raise Exception(f"Environment {environment} not recognised")

    def process_login(self, token: str):
        """
        Processes the login, adding the token to the session header and setting login datetimes
        :param token:
        :return: None
        """
        self.login_date = datetime.utcnow()
        self.login_expiry_check = datetime.utcnow() + timedelta(hours=2)
        self.login_status_check = datetime.utcnow() + timedelta(minutes=15)
        self._token = token
        self.session.headers.update({"X-AUTH-TOKEN": token})

    def process_logout(self):
        """
        Processes the logout, removing the token to the session header and setting login datetimes
        :return: None
        """
        self.login_date = None
        self.login_expiry_check = None
        self.login_status_check = None
        self._token = None
        try:
            self.session.headers.pop("X-AUTH-TOKEN")
        except KeyError as e:
            pass

