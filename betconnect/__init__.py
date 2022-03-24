from .__version__ import __title__, __version__, __author__
from .exceptions import (
    InValidPersonalisedProductionURL,
    UnknownBetConnectEnvironment,
    LoginMissingTokenInResponse,
    FailedLogin,
    MinOddException,
    UnexpectedResponseStatusCode,
    GamStopException,
    MissingUserPerferences,
    APIError,
    BetRequestIDFormatException,
    BetRequestIDStakeSizeException,
    BetRequestInvalidCustomerOrderRefFormatException,
    BetRequestInvalidCustomerStrategyRefFormatException,
)

from .enums import (
    Environment,
    BetStatus,
    BetSide,
    BetRequestStatus,
    MarketStatus,
    TradingStatus,
)

from .apiclient import APIClient
