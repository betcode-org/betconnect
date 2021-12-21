from betconnect.apiclient import APIClient
from betconnect import resources
from decouple import config
from betconnect.enums import Environment
import logging
from betconnect import enums
import uuid

logger = logging.getLogger(__name__)

"""
This script is an example workflow for betting on a horse racing market.
PLEASE MAKE SURE YOU ARE ONLY PRACTICING ORDERS AGAINST STAGING ENVIRONMENTS IF YOU HAVE NOT FULLY TESTED YOUR APP!
"""

# Strategy name max length = 15, no spaces. If you require longer use hashing function in utils.
STRATEGY_NAME = "horse_racing"

# Create a trading client instance
client = APIClient(
    username=config("STAGING_BETCONNECT_USERNAME"),
    password=config("STAGING_BETCONNECT_PASSWORD"),
    api_key=config("STAGING_BETCONNECT_API_KEY"),
    environment=Environment.STAGING,
    personalised_production_url=config("PRODUCTION_URI"),
)

assert client.environment == Environment.STAGING


# Login
login = client.account.login()

# Get account balance
balance = client.account.get_balance()

# Check there is available account balance
assert balance.balance > 0

# Get settled bets
my_back_bets = client.betting.my_bets(
    side=enums.BetSide.BACK, status=enums.BetRequestStatus.SETTLED
)

# Get active bets
my_active_back_bets = client.betting.my_bets(
    side=enums.BetSide.BACK, status=enums.BetRequestStatus.ACTIVE
)


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

# Active fixtures
active_fixtures = client.betting.active_fixtures(
    sport_id=horse_racing.sport_id, region_id=active_region.region_id
)

# Get active market type
market_types = client.betting.active_market_types(horse_racing.sport_id)

try:
    win_market_type = [t for t in market_types if t.name == "WIN"][0]
except IndexError:
    raise Exception("Cannot find the the market type WIN for the horse racing sport")


# Get active selections and prices for active fixture
for fixture in active_fixtures[-1:]:

    # get active markets
    active_markets = client.betting.active_markets(fixture_id=fixture.fixture_id)

    if active_markets:
        try:
            win_bet_type = active_markets[0].bet_types[0]
        except IndexError:
            raise Exception(f"Cannot find any win types for the active market")

        # get the selections and prices for a given market
        fixture_selection_prices = client.betting.selections_for_market(
            fixture_id=fixture.fixture_id,
            market_type_id=win_market_type.market_type_id,
            top_price_only=False,
        )

        # get the top priced selections and prices for a given market
        top_price_fixture_selection_prices = client.betting.selections_for_market(
            fixture_id=fixture.fixture_id,
            market_type_id=win_market_type.market_type_id,
            top_price_only=True,
        )
        if fixture_selection_prices:
            # select the first selection/competitor with a price and that is active
            try:
                selection = [
                    c
                    for c in fixture_selection_prices
                    if (c.trading_status == "Trading") and c.prices
                ][0]
            except IndexError as e:
                raise Exception(
                    "No competitors in the fixture are active and have prices available"
                )

            try:
                best_price = [p for p in selection.prices][0]
            except IndexError as e:
                raise Exception(
                    f"No price was available for selection {selection.name}"
                )

            # Create a BACK order against the first runner in the market
            bet_create_response = client.betting.bet_request_create(
                request_filter=resources.filters.CreateBetRequestFilter(
                    fixture_id=fixture.fixture_id,
                    market_type_id=win_market_type.market_type_id,
                    competitor=selection.competitor_id,
                    price=best_price.price,
                    stake=500,
                    bet_type=win_bet_type,
                    customer_strategy_ref=resources.CustomerStrategyRef.create_customer_strategy_ref(
                        STRATEGY_NAME
                    ),
                    customer_order_ref=resources.CustomerOrderRef.create_customer_order_ref(
                        str(uuid.uuid4())
                    ),
                )
            )
            if isinstance(bet_create_response, resources.BetRequestCreate):
                logger.info(f"Bet request was created!")

                # get the previously created bet request
                bet_request_get = client.betting.bet_request_get(
                    request_filter=resources.GetBetRequestFilter(
                        bet_request_id=bet_create_response.bet_request_id
                    )
                )

                # Retrieve my bets
                active_bet_request = client.betting.get_active_bet_requests()

                # Get active bets
                my_active_back_bets = client.betting.my_bets(
                    side=enums.BetSide.BACK, status=enums.BetRequestStatus.ACTIVE
                )

            else:
                logger.exception(f"Issue creating bet request with the supplied params")

        else:
            raise Exception(f"Could not find prices for fixture {fixture.fixture_id}")
    else:
        logger.info("No active markets could be found!")
