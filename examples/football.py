from decouple import config
from betconnect.apiclient import APIClient
from betconnect.enums import Environment

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

# get active sports
active_sports = client.betting.active_sports()

try:
    football = [s for s in active_sports if s.name == "Football"][0]
except IndexError:
    raise Exception("Cannot football as an active sport.")

# find active regions
active_regions = client.betting.active_regions(sport_id=football.sport_id)

# get the england region
try:
    active_region = [r for r in active_regions if r.name == "England"][0]
except IndexError:
    raise Exception("Cannot find the England region for football!")

# get active competitions
active_competitions = client.betting.active_competitions(
    sport_id=football.sport_id, region_id=active_region.region_id
)

# get market types
market_types = client.betting.active_market_types(sport_id=football.sport_id)

# get the Match result type
try:
    match_result_market_type = [t for t in market_types if t.name == "Match Result"][0]
except IndexError:
    raise Exception("Cannot find Match Result as a match type for football!")

for competition in active_competitions:
    # get active fixtures
    active_fixtures = client.betting.active_fixtures(
        sport_id=football.sport_id,
        competition_id=competition.competition_id,
        region_id=active_region.region_id,
    )

    for active_fixture in active_fixtures:

        # active markets
        active_markets = client.betting.active_markets(
            fixture_id=active_fixture.fixture_id
        )

        for active_market in active_markets:

            # get selections and prices for active market
            selections_for_market = client.betting.selections_for_market(
                fixture_id=active_fixture.fixture_id,
                market_type_id=active_market.market_type_id,
            )

# get a football line market
try:
    over_under_goals = [
        t for t in market_types if t.name == "Total Goals Over / Under"
    ][0]
except IndexError:
    raise Exception(
        "Cannot find Total Goals Over / Under as a match type for football!"
    )

for competition in active_competitions:
    # get active fixtures
    active_fixtures = client.betting.active_fixtures(
        sport_id=football.sport_id,
        competition_id=competition.competition_id,
        region_id=active_region.region_id,
    )

    for active_fixture in active_fixtures:
        # get active markets
        active_markets = client.betting.active_markets(
            fixture_id=active_fixture.fixture_id
        )

        for active_market in [
            m
            for m in active_markets
            if m.market_type_id == over_under_goals.market_type_id
        ]:
            # get selections for the line market
            selections_for_market = client.betting.selections_for_market(
                fixture_id=active_fixture.fixture_id,
                market_type_id=active_market.market_type_id,
            )

            # get a handicap market and active selections
            try:
                handicap_market = [
                    m for m in active_markets if m.is_handicap == "True"
                ][0]
                handicap_active_selections = client.betting.active_selections(
                    fixture_id=active_fixture.fixture_id,
                    market_type_id=active_market.market_type_id,
                    handicap=handicap_market.handicap,
                )
                # get individual prices
                for selection in handicap_active_selections:
                    selection_price = client.betting.prices(
                        fixture_id=active_fixture.fixture_id,
                        market_type_id=active_market.market_type_id,
                        competitor=selection.competitor,
                        handicap=handicap_market.handicap,
                    )

            except IndexError as e:
                raise Exception("Cannot find a handicap market.")
