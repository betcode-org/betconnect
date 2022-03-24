from requests.sessions import Session
from datetime import datetime, timedelta
from .enums import Environment
from typing import Union, Optional
from betconnect import resources
from betconnect import config
from betconnect import exceptions
import logging

logger = logging.getLogger(__name__)


class BaseClient:
    def __init__(
        self,
        username: str,
        password: str,
        api_key: str,
        personalised_production_url: str,
        environment: Environment = Environment.PRODUCTION,
        session: Session = None,
    ):
        """
        :param username: your betconnect username (string)
        :param password: your betconnect password (string)
        :param api_key: your betconnect api key (string)
        :param personalised_production_url: A production user supplied url. (account manager will supply this)
        :param environment: the environment endpoint you want to send requests to (enum Environment)
        :param session: Session object used in request default None.Session created if None with auth and headers handled.
        """
        self._username = username
        self._password = password
        self._api_key = api_key
        self._environment = environment
        self._update_client_session(session)
        self._personalised_production_url = personalised_production_url
        self._set_endpoint_uris(environment)
        self.login_date: Optional[datetime] = None
        self.login_expiry_check: Optional[datetime] = None
        self.next_refresh_time: Optional[datetime] = None
        self.session_timeout: int = 8 * 60 * 60
        self._token: Optional[resources.Token] = None
        self._account_preferences: Optional[resources.AccountPreferences] = None
        self._account_balance: Optional[resources.Balance] = None
        self._last_balance_update_time: Optional[datetime] = None
        self._api_version = config.API_VERSION
        self._page_start_value = config.PAGE_START_VALUE
        self._minimum_limit_value = config.MINIMUM_LIMIT_VALUE

    @property
    def username(self) -> str:
        return self._username

    @property
    def api_version(self) -> str:
        return self._api_version

    @property
    def page_start_value(self) -> int:
        return self._page_start_value

    @property
    def minimum_limit_value(self) -> int:
        return self._minimum_limit_value

    @property
    def account_preferences(self) -> Optional[resources.AccountPreferences]:
        return self._account_preferences

    @property
    def environment(self) -> Environment:
        return self._environment

    @property
    def user_id(self) -> Optional[str]:
        return self.account_preferences.user_id if self.account_preferences else None

    @property
    def account_balance(self) -> Optional[resources.Balance]:
        return self._account_balance

    @property
    def last_balance_update_time(self) -> Optional[datetime]:
        return self._last_balance_update_time

    @property
    def logged_in(self) -> bool:
        try:
            return True if datetime.utcnow() < self.login_expiry_check else False
        except TypeError:
            return False

    def set_account_balance(self, account_balance: resources.Balance) -> None:
        """
        Sets the account balance for easy access on the client. This is only accurate upto the last time it was updated.
        :param account_balance: The account Balance resource
        :return: None
        """
        self._account_balance = account_balance
        self._last_balance_update_time = datetime.utcnow()
        logger.info(f"Updated user account balance")

    def set_account_preferences(
        self, account_preferences: resources.AccountPreferences
    ) -> None:
        """
        Sets the users account perferences to the client for easy access. User to determined user_id.
        :param account_preferences: An AccountPreferences resource. Contains user account data like user_id.
        :return: None
        """
        self._account_preferences = account_preferences
        if self.account_preferences.gamstop_result == "Y":
            raise exceptions.GamStopException()
        logger.info(f"Account preferences updated")

    def _update_client_session(self, session: Union[None, Session] = None) -> None:
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

        logger.debug(f"Account session updated")

    def _set_endpoint_uris(self, environment: Environment):
        """
        Sets the uri for which requests are sent to
        :param environment: enum Environment {STAGING,PRODUCTION}
        :return: None
        """
        if environment == Environment.PRODUCTION:
            try:
                assert self._personalised_production_url[-16:] == ".betconnect.com/"
                self.uri = self._personalised_production_url
            except KeyError:
                raise exceptions.InValidPersonalisedProductionURL(
                    url=self._personalised_production_url
                )
        elif environment == Environment.STAGING:
            self.uri = config.DEFAULT_STAGING_URL
        else:
            raise exceptions.UnknownBetConnectEnvironment(environment=environment)

    def process_login(self, token: str):
        """
        Processes the login, adding the token to the session header and setting login datetimes
        :param token: string token value supplied by BetConnect on login / token refresh
        :return: None
        """
        self.login_date = datetime.utcnow()
        self.login_expiry_check = datetime.utcnow() + timedelta(
            hours=config.LOGIN_FREQUENCY_CHECK_SECS
        )
        self.next_refresh_time = datetime.utcnow() + timedelta(
            minutes=config.CLIENT_TOKEN_REFRESH_FREQUENCY
        )
        self._token = token
        self.session.headers.update({"X-AUTH-TOKEN": token})
        logger.info(f"Account login successful")

    def process_logout(self):
        """
        Processes the logout, removing the token to the session header and setting login datetimes
        :return: None
        """
        self.login_date = None
        self.login_expiry_check = None
        self.next_refresh_time = None
        self._token = None
        try:
            self.session.headers.pop("X-AUTH-TOKEN")
        except KeyError:
            pass

        logger.info(f"Account logout successful")
