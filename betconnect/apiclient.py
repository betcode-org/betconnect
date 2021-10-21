from .baseclient import BaseClient
from requests.sessions import Session
from betconnect import endpoints
from betconnect.enums import Envirnoment

class APIClient(BaseClient):

    def __init__(self,
                 username: str ,
                 password: str,
                 api_key: str,
                 environment: Envirnoment = Envirnoment.PRODUCTION,
                 session: Session = None
                 ):
        """
        APIClient is used to make request to the betconnect API
        :param username: your betconnect username (string)
        :param password: your betconnect password (string)
        :param api_key: your betconnect api key (string)
        :param environment: the environment endpoint you want to send requests to (enum Environent)
        :param session: Session object used in request default None. Session created if None with auth and headers handled.
        """
        self.betting = endpoints.Betting(self)
        self.configuration = endpoints.Configuration(self)
        self.login = endpoints.Login(self)
        self.account = endpoints.Account(self)
        super(APIClient, self).__init__(username=username, password=password,session=session,environment=environment,api_key=api_key)

