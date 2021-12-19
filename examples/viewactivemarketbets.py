import logging
from decouple import config
from betconnect import resources
from betconnect.resources import filters
from betconnect.apiclient import APIClient
from betconnect.enums import Environment

logger = logging.getLogger(__name__)

"""
This script is an example workflow for viewing active betrequest request in the market.
PLEASE MAKE SURE YOU ARE ONLY PRACTICING ORDERS AGAINST STAGING ENVIRONMENTS IF YOU HAVE NOT FULLY TESTED YOUR APP!
"""

# Create a trading client instance
client = APIClient(
    username=config("STAGING_BETCONNECT_USERNAME"),
    password=config("STAGING_BETCONNECT_PASSWORD"),
    api_key=config("STAGING_BETCONNECT_API_KEY"),
    environment=Environment.STAGING,
    personalised_production_url=config("PRODUCTION_URI"),
)

# login
client.account.login()

# Get active sports with bets
active_sports = client.betting.active_sports(with_bets=True)

market_bet_request = []

for active_sport in active_sports:
    if active_sport.bets_available > 0:

        bet_request_get = client.betting.bet_request_get(
            request_filter=filters.GetBetRequestFilter(sport_id=active_sport.sport_id)
        )
        if isinstance(bet_request_get, resources.BetRequest):
            market_bet_request.append(bet_request_get)
