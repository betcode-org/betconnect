from betconnect.apiclient import APIClient
from decouple import config
from betconnect.enums import Environment
from betconnect import resources
from betconnect import enums
from betconnect import utils

import logging

logger = logging.getLogger(__name__)

"""
This file contains examples of simple requests to BetConnect retrieve account data and betting history
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


# Get active bet requests
active_bet_requests = client.betting.get_active_bet_requests()

# Get my bets
my_bets = client.betting.my_bets(
    side=enums.BetSide.BACK,
    user_id=client.user_id,
    status=enums.BetRequestStatus.SETTLED,
    limit=100,
    page=0,
    get_all="get_all",
)


# Retrieve my bets
active_bet_request = client.betting.get_active_bet_requests()

# retrieves strategy based bets
for bets in active_bet_requests.bets:
    # Get my bets
    strategy_bet_requests = client.betting.my_bets(
        side=enums.BetSide.BACK,
        status=enums.BetRequestStatus.SETTLED,
        limit=100,
        page=0,
        get_all="get_all",
        customer_strategy_ref=bets.customer_strategy_ref,
    )

# Get historical bets
historical_bets = client.betting.bet_history(
    side=enums.BetSide.BACK, status=enums.BetRequestStatus.SETTLED
)
