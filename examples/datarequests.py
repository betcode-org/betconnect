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

# login
client.account.login()


# get active book makers
active_bookmakers = client.betting.active_bookmakers()

# get active sports
active_sports = client.betting.active_sports()

# get the horse racing sport
try:
    horse_racing = [s for s in active_sports if s.name == "Horse Racing"][0]
except IndexError as e:
    raise Exception(f"No active sports could be found!")

# get active regions
active_regions = client.betting.active_regions(sport_id=horse_racing.sport_id)

# get the England region
try:
    england_region = [r for r in active_regions if r.name == "England"][0]
except IndexError as e:
    raise Exception(f"No England could be found. Poor England!")

# Get active market types for horse racing
active_market_types = client.betting.active_market_types(sport_id=horse_racing.sport_id)

try:
    win_market_type = [mt for mt in active_market_types if mt.name == "WIN"][0]
except IndexError as e:
    raise Exception("Could not find the WIN market type for horse racing")

# get active competitions for horse racing
active_competitions = client.betting.active_competitions(
    sport_id=horse_racing.sport_id, region_id=england_region.region_id
)

# get active horse racing fixtures
try:
    active_fixtures = client.betting.active_fixtures(
        sport_id=horse_racing.sport_id,
        region_id=england_region.region_id,
        competition_id=active_competitions[0].competition_id,
    )
except IndexError as e:
    raise Exception(
        f"Could not find any currently active horse racing competition. Check on the site they are currently available during the current hours."
    )


# get active markets for an active horse racing fixture
try:
    active_markets = client.betting.active_markets(
        fixture_id=active_fixtures[0].fixture_id
    )
    grouped_active_markets = client.betting.active_markets(
        fixture_id=active_fixtures[0].fixture_id, grouped=True
    )
except IndexError as e:
    raise Exception(f"Could not find any active fixtures for horse racing")

# get active selections for an active market
active_selections = client.betting.active_selections(
    fixture_id=active_fixtures[-1].fixture_id,
    market_type_id=win_market_type.market_type_id,
)

# get selections and prices for an active market
selections_for_market = client.betting.selections_for_market(
    fixture_id=active_fixtures[-1].fixture_id,
    market_type_id=win_market_type.market_type_id,
)

# Get prices
prices = client.betting.prices(
    fixture_id=active_fixtures[-1].fixture_id,
    market_type_id=win_market_type.market_type_id,
    competitor=selections_for_market[-1].competitor_id,
)
