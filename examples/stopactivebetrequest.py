import logging
from decouple import config
from betconnect import enums
from betconnect import resources
from betconnect.apiclient import APIClient
from betconnect.enums import Environment
from datetime import datetime

logger = logging.getLogger(__name__)

"""
This script is an example workflow for stopping an active betrequest.
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

assert client.environment == Environment.STAGING

# Get active bets
my_active_back_bets = client.betting.my_bets(
    side=enums.BetSide.BACK, status=enums.BetRequestStatus.ACTIVE
)

cancellation_responses = []

if len(my_active_back_bets.bets) > 0:
    for bet in my_active_back_bets.bets[::-1]:  # type: resources.MyActiveBet
        if bet.fixture_start_date:
            if bet.fixture_start_date > datetime.utcnow():
                bet_stop_response = client.betting.bet_request_stop(
                    bet_request_id=bet.bet_request_id,
                    stop_bet_reason="The bet was too good!",
                )
                cancellation_responses.append(bet_stop_response)
