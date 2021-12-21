from betconnect.apiclient import APIClient
from decouple import config
from betconnect.enums import Environment

import logging

logger = logging.getLogger(__name__)

"""
This file contains examples of simple data requests to BetConnect
"""

# Create a trading client instance
client = APIClient(
    username=config("STAGING_BETCONNECT_USERNAME"),
    password=config("STAGING_BETCONNECT_PASSWORD"),
    api_key=config("STAGING_BETCONNECT_API_KEY"),
    environment=Environment.STAGING,
    personalised_production_url=config("PRODUCTION_URI"),
)

client.account.login()


# Active sports
active_sports = client.betting.active_sports()

try:
    horse_racing = [s for s in active_sports if s.display_name == "Horse Racing"][0]
except IndexError as e:
    raise Exception("Cannot find horse racing as an active sport!")

# Active bookmakers
active_bookmakers = client.betting.active_bookmakers()

# Active regions
active_regions = client.betting.active_regions(sport_id=horse_racing.sport_id)

try:
    active_region = [r for r in active_regions if r.name == "England"][0]
except IndexError:
    raise Exception("Cannot find the England region for horse racing!")

# Get active market type
market_types = client.betting.active_market_types(horse_racing.sport_id)

try:
    win_market_type = [t for t in market_types if t.name == "WIN"][0]
except IndexError:
    raise Exception("Cannot find the the market type WIN for the horse racing sport")


# Active fixtures
active_fixtures = client.betting.active_fixtures(
    sport_id=horse_racing.sport_id, region_id=active_region.region_id
)

for fixture in active_fixtures:
    active_selections = client.betting.active_selections(
        fixture_id=fixture.fixture_id, market_type_id=win_market_type.market_type_id
    )
    handicap_active_selections = client.betting.active_selections(
        fixture_id=fixture.fixture_id,
        market_type_id=win_market_type.market_type_id,
        handicap=1,
    )
