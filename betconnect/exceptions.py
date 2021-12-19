from typing import Optional
from betconnect import enums
from betconnect import config


class BetConnectException(Exception):

    """
    base exception class

    """

    pass


class InValidPersonalisedProductionURL(BetConnectException):
    def __init__(self, url: str):
        """
        Raise when the supplied personalised betconnect url does not match the required pattern
        :param url: The supplied URL
        """
        super(InValidPersonalisedProductionURL, self).__init__(url)
        self.url = url

    def __str__(self) -> str:
        return (
            f"The personalised url supplied ({self.url}), "
            f"is not in the correct format. Expected ending in .betconnect.com/"
        )


class UnknownBetConnectEnvironment(BetConnectException):
    def __init__(self, environment: enums.Environment):
        """
        Raise when the environment supplied is not recognised as one available to end users. STAGING OR PRODUCTION.
        :param environment: The supplied environment value
        """
        super(UnknownBetConnectEnvironment, self).__init__(environment)
        self.environment = environment

    def __str__(self) -> str:
        return f"Expect environment in [{enums.Environment.PRODUCTION},{enums.Environment.STAGING}], got {self.environment}"


class LoginMissingTokenInResponse(BetConnectException):
    """
    Raise when the login response contains no login token.
    """

    def __str__(self) -> str:
        return f"Missing login token in response data"


class FailedLogin(BetConnectException):
    def __init__(self, username: str):
        """
        Raised when the user supplies the incorrect username and password
        :param username: the client supplied username
        """
        super(FailedLogin, self).__init__(username)
        self.username = username

    def __str__(self) -> str:
        return f"Failed Login for the username {self.username}. Please check both your username and password."


class UnexpectedResponseStatusCode(BetConnectException):
    def __init__(self, status_code: int, url: str):
        """
        Raised when an unexpected status code is returned from a response
        :param status_code: the response status code
        :param url: the request url
        """
        super(UnexpectedResponseStatusCode, self).__init__(status_code, url)
        self.url = url
        self.status_code = status_code

    def __str__(self) -> str:
        return f"Unexpected status code ({self.status_code}) returned for request: {self.url} "


class GamStopException(BetConnectException):
    """
    Account perferences has highlighted that you have a Gamstop against your username.
    API Access is forbidden for any user with a Gamstop ban against their username.
    If this is incorrect please contact your account manager.
    """

    def __str__(self) -> str:
        return "API access if strictly forbidden for users with a Gamstop ban against their account."


class MissingUserPerferences(BetConnectException):
    """
    Called when trying to access user_id property for my_bets but the account_preferences are unavailable.
    """

    def __str__(self) -> str:
        return "Unable to get user_id via get_user_preferences. Please supply a value or speak to your account manager"


class MinOddException(BetConnectException):
    """
    Exception raised when min odds requirements not met
    """

    def __init__(self, min_odds: float):
        """
        Raised when the user supplies an odd less than the site minimum
        :param min_odds:
        """
        super(MinOddException, self).__init__(min_odds)
        self.min_odds = min_odds

    def __repr__(self) -> str:
        return f"The supplied odds {self.min_odds} is less then the site minimum {config.BET_REQUEST_MIN_ODDS} "


class BetRequestIDFormatException(BetConnectException):
    """
    Exception raised when the format does not match a valid UUID format.
    i.e. 'c9bf9e57-1685-4c89-bafb-ff5af830be8a'
    """

    def __init__(self, bet_request_id: str):
        super(BetRequestIDFormatException, self).__init__(bet_request_id)
        self.bet_request_id = bet_request_id

    def __str__(self) -> str:
        return f"bet_request_id ({self.bet_request_id}) should be of length 36 and be a UUID"


class BetRequestIDStakeSizeException(BetConnectException):
    """
    raised when an invalid stake size is used. Should be an integer and multiples of £5.0
    """

    def __init__(self, stake_size: int):
        super(BetRequestIDStakeSizeException, self).__init__(stake_size)
        self.stake_size = stake_size

    def __str__(self) -> str:
        return (
            f"Supplied stake size {self.stake_size} is not a multiple of {config.SITE_STAKE_SIZE_MULTIPLE_REQUIREMENT} "
            f"greater than the site minimum of {config.SITE_MINIMUM_STAKE_SIZE}"
        )


class BetRequestInvalidCustomerOrderRefFormatException(BetConnectException):
    """
    raised when customer order ref is not between 1-36 character in length
    """

    def __init__(self, customer_order_ref: str):
        super(BetRequestInvalidCustomerOrderRefFormatException, self).__init__(
            customer_order_ref
        )
        self.customer_order_ref = customer_order_ref

    def __str__(self) -> str:
        return f"The supplied customer_order_ref doesnt meet the required length of {config.MIN_CUSTOMER_ORDER_REF_LENGTH}->{config.MAX_CUSTOMER_ORDER_REF_LENGTH}"


class BetRequestInvalidCustomerStrategyRefFormatException(BetConnectException):
    """
    raised when customer order ref is not between 1-15 character in length
    """

    def __init__(self, customer_strategy_ref: str):
        super(BetRequestInvalidCustomerStrategyRefFormatException, self).__init__(
            customer_strategy_ref
        )
        self.customer_strategy_ref = customer_strategy_ref

    def __str__(self) -> str:
        return f"The supplied customer_strategy_ref does not match the required length of {config.MIN_CUSTOMER_STRATEGY_REF_LENGTH}->{config.MAX_CUSTOMER_STRATEGY_REF_LENGTH}"


class APIError(BetConnectException):
    """
    Exception raised if error is found.
    """

    def __init__(
        self,
        response: Optional[dict],
        uri: str = None,
        params: dict = None,
        exception: Exception = None,
    ):
        if response:
            error_data = response.get("error")
            message = (
                "%s \nParams: %s \nException: %s \nError: %s \nFull Response: %s"
                % (uri, params, exception, error_data, response)
            )
        else:
            message = "%s \nParams: %s \nException: %s" % (uri, params, exception)
        super(APIError, self).__init__(message)
