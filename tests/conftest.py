from betconnect import endpoints
import pytest
from betconnect import resources
from betconnect.apiclient import APIClient
from betconnect.baseclient import BaseClient
from betconnect.enums import Environment
from decouple import config
from requests import Response
from typing import Tuple, Dict, Any
from tests.utils import build_path, load_pickle, load_json
from pytest_mock import mocker


@pytest.fixture
def mock_base_client() -> BaseClient:
    return BaseClient(
        username="test",
        password="123",
        api_key="456",
        environment=Environment.STAGING,
        personalised_production_url=config("PRODUCTION_URI"),
    )


@pytest.fixture
def mock_api_client() -> APIClient:
    return APIClient(
        username="test",
        password="123",
        api_key="456",
        environment=Environment.STAGING,
        personalised_production_url=config("PRODUCTION_URI"),
    )


@pytest.fixture
def staging_api_client() -> APIClient:
    return APIClient(
        username=config("STAGING_BETCONNECT_USERNAME"),
        password=config("STAGING_BETCONNECT_PASSWORD"),
        api_key=config("STAGING_BETCONNECT_API_KEY"),
        environment=Environment.STAGING,
        personalised_production_url=config("PRODUCTION_URI"),
    )


@pytest.fixture
def staging_lay_api_client() -> APIClient:
    return APIClient(
        username=config("STAGING_BETCONNECT_LAY_USERNAME"),
        password=config("STAGING_BETCONNECT_LAY_PASSWORD"),
        api_key=config("STAGING_BETCONNECT_LAY_API_KEY"),
        environment=Environment.STAGING,
        personalised_production_url=config("PRODUCTION_URI"),
    )


@pytest.fixture
def mock_betting_endpoint(staging_api_client) -> endpoints.Betting:
    return endpoints.Betting(staging_api_client)


@pytest.fixture
def mock_account_endpoint(staging_api_client) -> endpoints.Account:
    return endpoints.Account(staging_api_client)


@pytest.fixture()
def mock_login_response_pkl() -> Response:
    return load_pickle(
        build_path(
            "resources/endpoints/account/mock_account_login_response_success.pkl"
        )
    )


@pytest.fixture()
def mock_login_response_json() -> Dict[str, Any]:
    return load_json(
        build_path(
            "resources/endpoints/account/mock_account_login_response_success.json"
        )
    )


@pytest.fixture()
def mock_login_response(
    mock_login_response_pkl: Response, mock_login_response_json: Dict[str, Any]
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_login_response_pkl, mock_login_response_json, 1.0


@pytest.fixture()
def mock_login_response_failure_pkl() -> Response:
    return load_pickle(
        build_path(
            "resources/endpoints/account/mock_account_login_response_failure.pkl"
        )
    )


@pytest.fixture()
def mock_login_response_failure_json() -> Dict[str, Any]:
    return load_json(
        build_path(
            "resources/endpoints/account/mock_account_login_response_failure.json"
        )
    )


@pytest.fixture()
def mock_login_failure_response(
    mock_login_response_failure_pkl: Response,
    mock_login_response_failure_json: Dict[str, Any],
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_login_response_failure_pkl, mock_login_response_failure_json, 1.0


@pytest.fixture()
def mock_logout_response_pkl() -> Response:
    return load_pickle(
        build_path("resources/endpoints/account/mock_account_logout_response.pkl")
    )


@pytest.fixture()
def mock_logout_response_json() -> Dict[str, Any]:
    return load_json(
        build_path("resources/endpoints/account/mock_account_logout_response.json")
    )


@pytest.fixture()
def mock_logout_response(
    mock_logout_response_pkl: Response, mock_logout_response_json: Dict[str, Any]
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_logout_response_pkl, mock_logout_response_json, 1.0


@pytest.fixture()
def mock_active_bookmakers_pkl() -> Response:
    return load_pickle(
        build_path("resources/endpoints/betting/active_bookmakers_response.pkl")
    )


@pytest.fixture()
def mock_active_bookmakers_json() -> Dict[str, Any]:
    return load_json(
        build_path("resources/endpoints/betting/active_bookmakers_response.json")
    )


@pytest.fixture()
def mock_active_bookmakers_response(
    mock_active_bookmakers_pkl: Response, mock_active_bookmakers_json: Dict[str, Any]
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_active_bookmakers_pkl, mock_active_bookmakers_json, 1.0


@pytest.fixture()
def mock_active_sports_pkl() -> Response:
    return load_pickle(
        build_path("resources/endpoints/betting/active_sports_response.pkl")
    )


@pytest.fixture()
def mock_active_sports_json() -> Dict[str, Any]:
    return load_json(
        build_path("resources/endpoints/betting/active_sports_response.json")
    )


@pytest.fixture()
def mock_active_sports_response(
    mock_active_sports_pkl: Response, mock_active_sports_json: Dict[str, Any]
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_active_sports_pkl, mock_active_sports_json, 1.0


@pytest.fixture()
def mock_active_regions_pkl() -> Response:
    return load_pickle(
        build_path("resources/endpoints/betting/active_regions_response.pkl")
    )


@pytest.fixture()
def mock_active_regions_json() -> Dict[str, Any]:
    return load_json(
        build_path("resources/endpoints/betting/active_regions_response.json")
    )


@pytest.fixture()
def mock_active_regions_response(
    mock_active_regions_pkl: Response, mock_active_regions_json: Dict[str, Any]
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_active_regions_pkl, mock_active_regions_json, 1.0


@pytest.fixture()
def mock_active_competitions_pkl() -> Response:
    return load_pickle(
        build_path("resources/endpoints/betting/active_competitions_response.pkl")
    )


@pytest.fixture()
def mock_active_competitions_json() -> Dict[str, Any]:
    return load_json(
        build_path("resources/endpoints/betting/active_competitions_response.json")
    )


@pytest.fixture()
def mock_active_competitions_response(
    mock_active_competitions_pkl: Response,
    mock_active_competitions_json: Dict[str, Any],
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_active_competitions_pkl, mock_active_competitions_json, 1.0


@pytest.fixture()
def mock_active_fixtures_pkl() -> Response:
    return load_pickle(
        build_path("resources/endpoints/betting/active_fixtures_response.pkl")
    )


@pytest.fixture()
def mock_active_fixtures_json() -> Dict[str, Any]:
    return load_json(
        build_path("resources/endpoints/betting/active_fixtures_response.json")
    )


@pytest.fixture()
def mock_active_fixtures_response(
    mock_active_fixtures_pkl: Response, mock_active_fixtures_json: Dict[str, Any]
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_active_fixtures_pkl, mock_active_fixtures_json, 1.0


@pytest.fixture()
def mock_active_market_types_pkl() -> Response:
    return load_pickle(
        build_path("resources/endpoints/betting/active_market_types_response.pkl")
    )


@pytest.fixture()
def mock_active_market_types_json() -> Dict[str, Any]:
    return load_json(
        build_path("resources/endpoints/betting/active_market_types_response.json")
    )


@pytest.fixture()
def mock_active_market_types_response(
    mock_active_market_types_pkl: Response,
    mock_active_market_types_json: Dict[str, Any],
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_active_market_types_pkl, mock_active_market_types_json, 1.0


@pytest.fixture()
def mock_active_markets_pkl() -> Response:
    return load_pickle(
        build_path("resources/endpoints/betting/active_markets_response.pkl")
    )


@pytest.fixture()
def mock_active_markets_json() -> Dict[str, Any]:
    return load_json(
        build_path("resources/endpoints/betting/active_markets_response.json")
    )


@pytest.fixture()
def mock_active_markets_response(
    mock_active_markets_pkl: Response, mock_active_markets_json: Dict[str, Any]
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_active_markets_pkl, mock_active_markets_json, 1.0


@pytest.fixture()
def mock_active_selections_pkl() -> Response:
    return load_pickle(
        build_path("resources/endpoints/betting/active_selections_response.pkl")
    )


@pytest.fixture()
def mock_active_selections_json() -> Dict[str, Any]:
    return load_json(
        build_path("resources/endpoints/betting/active_selections_response.json")
    )


@pytest.fixture()
def mock_active_selections_response(
    mock_active_selections_pkl: Response, mock_active_selections_json: Dict[str, Any]
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_active_selections_pkl, mock_active_selections_json, 1.0


@pytest.fixture()
def mock_bet_history_pkl() -> Response:
    return load_pickle(
        build_path("resources/endpoints/betting/bet_history_response.pkl")
    )


@pytest.fixture()
def mock_bet_history_json() -> Dict[str, Any]:
    return load_json(
        build_path("resources/endpoints/betting/bet_history_response.json")
    )


@pytest.fixture()
def mock_bet_history_response(
    mock_bet_history_pkl: Response, mock_bet_history_json: Dict[str, Any]
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_bet_history_pkl, mock_bet_history_json, 1.0


@pytest.fixture()
def mock_get_balance_pkl() -> Response:
    return load_pickle(
        build_path("resources/endpoints/betting/get_balance_response.pkl")
    )


@pytest.fixture()
def mock_get_balance_json() -> Dict[str, Any]:
    return load_json(
        build_path("resources/endpoints/betting/get_balance_response.json")
    )


@pytest.fixture()
def mock_get_balance_response(
    mock_get_balance_pkl: Response, mock_get_balance_json: Dict[str, Any]
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_get_balance_pkl, mock_get_balance_json, 1.0


@pytest.fixture()
def mock_my_bets_pkl() -> Response:
    return load_pickle(build_path("resources/endpoints/betting/my_bets_response.pkl"))


@pytest.fixture()
def mock_my_bets_json() -> Dict[str, Any]:
    return load_json(build_path("resources/endpoints/betting/my_bets_response.json"))


@pytest.fixture()
def mock_my_bets_response(
    mock_my_bets_pkl: Response, mock_my_bets_json: Dict[str, Any]
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_my_bets_pkl, mock_my_bets_json, 1.0


@pytest.fixture()
def mock_selections_for_market_line_market_pkl() -> Response:
    return load_pickle(
        build_path("resources/endpoints/betting/selections_for_market_line_market.pkl")
    )


@pytest.fixture()
def mock_selections_for_market_line_market_json() -> Dict[str, Any]:
    return load_json(
        build_path("resources/endpoints/betting/selections_for_market_line_market.json")
    )


@pytest.fixture()
def mock_selections_for_market_line_market_response(
    mock_selections_for_market_line_market_pkl: Response,
    mock_selections_for_market_line_market_json: Dict[str, Any],
) -> Tuple[Response, Dict[str, Any], float]:
    return (
        mock_selections_for_market_line_market_pkl,
        mock_selections_for_market_line_market_json,
        1.0,
    )


@pytest.fixture()
def mock_prices_pkl() -> Response:
    return load_pickle(build_path("resources/endpoints/betting/prices_response.pkl"))


@pytest.fixture()
def mock_prices_json() -> Dict[str, Any]:
    return load_json(build_path("resources/endpoints/betting/prices_response.json"))


@pytest.fixture()
def mock_prices_response(
    mock_prices_pkl: Response, mock_prices_json: Dict[str, Any]
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_prices_pkl, mock_prices_json, 1.0


@pytest.fixture()
def mock_bet_request_create_pkl() -> Response:
    return load_pickle(
        build_path("resources/endpoints/betting/bet_request_create_response.pkl")
    )


@pytest.fixture()
def mock_bet_request_create_json() -> Dict[str, Any]:
    return load_json(
        build_path("resources/endpoints/betting/bet_request_create_response.json")
    )


@pytest.fixture()
def mock_bet_request_create_response(
    mock_bet_request_create_pkl: Response, mock_bet_request_create_json: Dict[str, Any]
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_bet_request_create_pkl, mock_bet_request_create_json, 1.0


@pytest.fixture()
def mock_bet_request_get_pkl() -> Response:
    return load_pickle(
        build_path("resources/endpoints/betting/bet_request_get_response.pkl")
    )


@pytest.fixture()
def mock_bet_request_get_json() -> Dict[str, Any]:
    return load_json(
        build_path("resources/endpoints/betting/bet_request_get_response.json")
    )


@pytest.fixture()
def mock_bet_request_get_response(
    mock_bet_request_get_pkl: Response, mock_bet_request_get_json: Dict[str, Any]
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_bet_request_get_pkl, mock_bet_request_get_json, 1.0


@pytest.fixture()
def mock_bet_request_match_pkl() -> Response:
    return load_pickle(
        build_path("resources/endpoints/betting/bet_request_match_response.pkl")
    )


@pytest.fixture()
def mock_bet_request_match_json() -> Dict[str, Any]:
    return load_json(
        build_path("resources/endpoints/betting/bet_request_match_response.json")
    )


@pytest.fixture()
def mock_bet_request_match_response(
    mock_bet_request_match_pkl: Response, mock_bet_request_match_json: Dict[str, Any]
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_bet_request_match_pkl, mock_bet_request_match_json, 1.0


@pytest.fixture()
def mock_bet_request_stop_pkl() -> Response:
    return load_pickle(
        build_path("resources/endpoints/betting/bet_request_stop_response.pkl")
    )


@pytest.fixture()
def mock_bet_request_stop_json() -> Dict[str, Any]:
    return load_json(
        build_path("resources/endpoints/betting/bet_request_stop_response.json")
    )


@pytest.fixture()
def mock_bet_request_stop_response(
    mock_bet_request_stop_pkl: Response, mock_bet_request_stop_json: Dict[str, Any]
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_bet_request_stop_pkl, mock_bet_request_stop_json, 1.0


@pytest.fixture()
def mock_bet_request_match_more_pkl() -> Response:
    return load_pickle(
        build_path("resources/endpoints/betting/bet_request_match_more_response.pkl")
    )


@pytest.fixture()
def mock_bet_request_match_more_json() -> Dict[str, Any]:
    return load_json(
        build_path("resources/endpoints/betting/bet_request_match_more_response.json")
    )


@pytest.fixture()
def mock_bet_request_match_more_response(
    mock_bet_request_match_more_pkl: Response,
    mock_bet_request_match_more_json: Dict[str, Any],
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_bet_request_match_more_pkl, mock_bet_request_match_more_json, 1.0


@pytest.fixture()
def mock_get_active_bet_requests_pkl() -> Response:
    return load_pickle(
        build_path("resources/endpoints/betting/get_active_bet_requests_response.pkl")
    )


@pytest.fixture()
def mock_get_active_bet_requests_json() -> Dict[str, Any]:
    return load_json(
        build_path("resources/endpoints/betting/get_active_bet_requests_response.json")
    )


@pytest.fixture()
def mock_bet_get_active_bet_requests_response(
    mock_get_active_bet_requests_pkl: Response,
    mock_get_active_bet_requests_json: Dict[str, Any],
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_get_active_bet_requests_pkl, mock_get_active_bet_requests_json, 1.0


@pytest.fixture()
def mock_get_viewed_next_page_pkl() -> Response:
    return load_pickle(
        build_path("resources/endpoints/betting/get_viewed_next_page_response.pkl")
    )


@pytest.fixture()
def mock_get_viewed_next_page_json() -> Dict[str, Any]:
    return load_json(
        build_path("resources/endpoints/betting/get_viewed_next_page_response.json")
    )


@pytest.fixture()
def mock_get_viewed_next_page_response(
    mock_get_viewed_next_page_pkl: Response,
    mock_get_viewed_next_page_json: Dict[str, Any],
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_get_viewed_next_page_pkl, mock_get_viewed_next_page_json, 1.0


@pytest.fixture()
def mock_selections_for_market_pkl() -> Response:
    return load_pickle(
        build_path("resources/endpoints/betting/selections_for_market_response.pkl")
    )


@pytest.fixture()
def mock_selections_for_market_json() -> Dict[str, Any]:
    return load_json(
        build_path("resources/endpoints/betting/selections_for_market_response.json")
    )


@pytest.fixture()
def mock_selections_for_market_response(
    mock_selections_for_market_pkl: Response,
    mock_selections_for_market_json: Dict[str, Any],
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_selections_for_market_pkl, mock_selections_for_market_json, 1.0


"""
NEW ACCOUNT FIXTURES
"""


@pytest.fixture()
def mock_get_user_preferences_response_pkl() -> Response:
    return load_pickle(
        build_path("resources/endpoints/account/mock_get_user_preferences_response.pkl")
    )


@pytest.fixture()
def mock_get_user_preferences_response_json() -> Dict[str, Any]:
    return load_json(
        build_path(
            "resources/endpoints/account/mock_get_user_preferences_response.json"
        )
    )


@pytest.fixture()
def mock_get_user_preferences_response_response(
    mock_get_user_preferences_response_pkl: Response,
    mock_get_user_preferences_response_json: Dict[str, Any],
) -> Tuple[Response, Dict[str, Any], float]:
    return (
        mock_get_user_preferences_response_pkl,
        mock_get_user_preferences_response_json,
        1.0,
    )


@pytest.fixture()
def mock_login_resource() -> resources.Login:
    return resources.Login(message="Login Successful", data={"token": "12345"})


@pytest.fixture()
def mock_token_resource() -> resources.Token:
    return resources.Token(
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySUQiOiJhNmExZWI5MS02MjE3LTRlMGMtYjc1OS1mYmNhYTJiN2E4YWMiLCJsYXN0X3JlZnJlc2giOjE2Mzk4NDk2NzguODAzODYzLCJleHAiOjE2Mzk4Nzg0Nzh9.SiH-iupnvhMXqFjIQuhnXS-YcbxKFXTwowRfytdlrBw"
    )


@pytest.fixture()
def mock_account_preferences_resource(
    mock_get_user_preferences_response_response: Tuple[Response, Dict[str, Any], float]
) -> resources.AccountPreferences:
    return resources.AccountPreferences(
        **mock_get_user_preferences_response_response[1]["data"]
    )


@pytest.fixture()
def mock_get_balance_response_pkl() -> Response:
    return load_pickle(
        build_path("resources/endpoints/account/mock_get_balance_response.pkl")
    )


@pytest.fixture()
def mock_get_balance_response_json() -> Dict[str, Any]:
    return load_json(
        build_path("resources/endpoints/account/mock_get_balance_response.json")
    )


@pytest.fixture()
def mock_get_balance_response(
    mock_get_balance_response_pkl: Response,
    mock_get_balance_response_json: Dict[str, Any],
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_get_balance_response_pkl, mock_get_balance_response_json, 1.0


@pytest.fixture()
def mock_balance_resource(
    mock_get_balance_response: Tuple[Response, Dict[str, Any], float]
) -> resources.Balance:
    return resources.Balance(**mock_get_balance_response[1]["data"])


@pytest.fixture()
def mock_bet_request_match_more_response(
    mock_bet_request_match_more_pkl: Response,
    mock_bet_request_match_more_json: Dict[str, Any],
) -> Tuple[Response, Dict[str, Any], float]:
    return mock_bet_request_match_more_pkl, mock_bet_request_match_more_json, 1.0


@pytest.fixture()
def mock_refresh_session_token_response_pkl() -> Response:
    return load_pickle(
        build_path(
            "resources/endpoints/account/mock_refresh_session_token_response.pkl"
        )
    )


@pytest.fixture()
def mock_refresh_session_token_response_json() -> Dict[str, Any]:
    return load_json(
        build_path(
            "resources/endpoints/account/mock_refresh_session_token_response.json"
        )
    )


@pytest.fixture()
def mock_refresh_session_token_response(
    mock_refresh_session_token_response_pkl: Response,
    mock_refresh_session_token_response_json: Dict[str, Any],
) -> Tuple[Response, Dict[str, Any], float]:
    return (
        mock_refresh_session_token_response_pkl,
        mock_refresh_session_token_response_json,
        1.0,
    )


@pytest.fixture()
def mock_active_bookmaker_resource() -> resources.ActiveBookmaker:
    return resources.ActiveBookmaker(
        name="10Bet", bookmaker_id=6122, order=99, active=1
    )


@pytest.fixture()
def mock_active_sport_resource() -> resources.ActiveSport:
    return resources.ActiveSport(
        id=21,
        sport_id=14,
        name="Horse Racing",
        display_name="Horse Racing",
        slug="horse-racing",
        order=1,
        active=1,
        rate=2.0,
    )


@pytest.fixture()
def mock_active_region_resource() -> resources.ActiveRegion:
    return resources.ActiveRegion(
        name="England", region_id=3795032, iso="england", order=2
    )


@pytest.fixture()
def mock_active_competition_resource() -> resources.ActiveCompetition:
    return resources.ActiveCompetition(
        name="Southwell",
        display_name="Southwell",
        competition_id=840,
        active=1,
        order=9999,
    )


@pytest.fixture()
def mock_active_market_type_resource() -> resources.ActiveMarketType:
    return resources.ActiveMarketType(market_type_id=6, name="WIN", active=1)


@pytest.fixture()
def mock_active_market_resource() -> resources.ActiveMarket:
    return resources.ActiveMarket(
        name="Race Winner",
        display_name="Race Winner",
        trading_status="Open",
        is_handicap="False",
        source_market_id="102347558",
        market_type_id=6,
        order=1,
        bet_types=["Win", "Each Way (1/4 odds 1-2-3)"],
    )


@pytest.fixture()
def mock_prices_bookmaker_resource() -> resources.PricesBookmaker:
    return resources.PricesBookmaker(id="123", name="Betfair")


@pytest.fixture()
def mock_price_resource() -> resources.Price:
    return resources.Price(
        price="10",
        numerator="10",
        denominator="1",
        bookmakers=[{"id": "123", "name": "Betfair"}],
    )


@pytest.fixture()
def mock_active_selection_resource() -> resources.ActiveSelection:
    return resources.ActiveSelection(
        name="Metal Man",
        trading_status="NonRunner",
        selection_id="308685953",
        ut="2021-12-17 15:49:20.068318",
        competitor="1095697",
    )


@pytest.fixture()
def mock_active_fixture_resource() -> resources.ActiveFixture:
    return resources.ActiveFixture(
        fixture_id="8757184",
        display_name="Kempton Park",
        start_date="2021-12-17",
        time="16:15",
        each_way_active="1",
    )


@pytest.fixture()
def mock_backers_stats_resource() -> resources.BackersStats:
    return resources.BackersStats(strike_rate=100.0, roi=10.0, bet_requests="1234")


@pytest.fixture()
def mock_bet_request_resource() -> resources.BetRequest:
    return resources.BetRequest(
        sport_name="Horse Racing",
        sport_id="14",
        competition_name="Kempton Park",
        region_name="England",
        start_time_utc="2021-12-17 19:45:00+00:00",
        fixture_name="Kempton Park",
        market_name="Race Winner",
        selection_name="Starter For Ten",
        price={
            "decimal": "3.25",
            "fraction": {"numerator": "9", "denominator": "4"},
        },
        fixture_id=8757185,
        market_type_id=6,
        competitor="1207634",
        bet_request_id="0f6efaa7-ffc3-45e9-8cf5-aa07e8ef5369",
        bet_type="Win",
        requested_stake=5.0,
        liability=11.25,
        locked_stake=0.0,
        backer_stats={
            "strike_rate": 0.33,
            "roi": -100.0,
            "bet_requests": "10-50",
            "recent_performance": "L,L,L,L,L,L,L,L",
        },
        others_viewing_bet=0,
        lockable=True,
    )


@pytest.fixture()
def mock_bet_request_create_resource() -> resources.BetRequestCreate:
    return resources.BetRequestCreate(
        bet_request_id="0f6efaa7-ffc3-45e9-8cf5-aa07e8ef5369",
        created="2021-12-17 16:20:49.113386",
        debit_stake=5,
        debit_commission=0.1,
    )


@pytest.fixture()
def mock_active_bet_resource() -> resources.ActiveBet:
    return resources.ActiveBet(
        bet_request_id="45e1a024-523a-4b25-a33d-4466775d0aac",
        bet_type_name="Win",
        competition_name="Hamilton Park",
        created_at="2021-07-15 09:38:22",
        fill_percentage=0.0,
        fixture_id=8248855,
        fixture_name="Hamilton Park",
        fixture_start_date="2021-07-15 12:00:00",
        market_name="Race Winner",
        matched_stake=0.0,
        price=1.16,
        price_denominator=25,
        price_numerator=4,
        selection_name="Misty Ayr",
        sport_name="Horse Racing",
        stake=10.0,
        status_name="Active",
    )


@pytest.fixture()
def mock_bet_request_match_more_resource() -> resources.BetRequestMatch:
    return resources.BetRequestMatch(
        matched=True,
        available=True,
        bet_request_id="45e1a024-523a-4b25-a33d-4466775d0aac",
        bet_id="124",
        bet_status="Active",
        amount_matched=10.0,
    )


@pytest.fixture()
def mock_bet_history_resource() -> resources.BetHistory:
    return resources.BetHistory(
        bet_request_id="0f6efaa7-ffc3-45e9-8cf5-aa07e8ef5369",
        bet_request_status="Active",
        bet_type_name="Win",
        competition_name="Kempton Park",
        fill_percentage=0.0,
        fixture_name="Kempton Park",
        fixture_start_date="2021-12-17 19:45:00",
        market_name="Race Winner",
        matched_stake=0.0,
        price=3.25,
        price_denominator=4,
        price_numerator=9,
        region_iso="england",
        region_name="England",
        selection_name="Starter For Ten",
        sport_name="Horse Racing",
        stake=5.0,
    )


@pytest.fixture()
def mock_active_bet_requests_resource(
    mock_active_bet_resource: resources.ActiveBet,
) -> resources.ActiveBetRequests:
    return resources.ActiveBetRequests(
        bets=[mock_active_bet_resource], bets_active=10, last_page=10, total_bets=20
    )


@pytest.fixture()
def mock_bet_history_request_resource(
    mock_bet_history_resource: resources.BetHistory,
) -> resources.ActiveBetRequests:
    return resources.ActiveBetRequests(
        bets=[mock_bet_history_resource], bets_active=10, last_page=10, total_bets=20
    )


@pytest.fixture()
def mock_selections_for_market_resource() -> resources.SelectionsForMarket:
    return resources.SelectionsForMarket(
        source_fixture_id="8757185",
        source_market_id="102347567",
        source_market_type_id="6",
        source_selection_id="308686039",
        trading_status="Trading",
        name="Starter For Ten",
        competitor_id="1207634",
        ut="2021-12-16 08:53:29.827063",
        order=0,
        max_price=3.25,
        prices=[
            {
                "price": "3.25",
                "numerator": "9",
                "denominator": "4",
                "bookmakers": [
                    {"id": "4", "name": "William Hill"},
                    {"id": "6002", "name": "Skybet"},
                ],
            },
            {
                "price": "3.20",
                "numerator": "11",
                "denominator": "5",
                "bookmakers": [
                    {"id": "3", "name": "Paddy Power"},
                    {"id": "6316", "name": "Betfair Sportsbook"},
                ],
            },
            {
                "price": "3.00",
                "numerator": "2",
                "denominator": "1",
                "bookmakers": [
                    {"id": "6006", "name": "Coral"},
                    {"id": "6001", "name": "BetVictor"},
                    {"id": "17", "name": "Ladbrokes"},
                ],
            },
        ],
    )


@pytest.fixture()
def mock_viewed_resource() -> resources.Viewed:
    return resources.Viewed(
        prev="0f6efaa7-ffc3-45e9-8cf5-aa07e8ef5369",
        next="0f6efaa7-ffc3-45e9-8cf5-aa07e8ef5589",
    )


@pytest.fixture()
def mock_bet_request_match_more_resource() -> resources.BetRequestMatchMore:
    return resources.BetRequestMatchMore(
        matched=True,
        available=True,
        viewed={
            "prev": "0f6efaa7-ffc3-45e9-8cf5-aa07e8ef5369",
            "next": "0f6efaa7-ffc3-45e9-8cf5-aa07e8ef5589",
        },
    )


@pytest.fixture()
def mock_bet_request_stop_resource() -> resources.BetRequestStop:
    return resources.BetRequestStop(pending=False)


@pytest.fixture()
def mock_my_active_bet_resource() -> resources.MyActiveBet:
    return resources.MyActiveBet(
        actioned_at="2021-07-15 09:35:26",
        bet_created=1,
        bet_request_id="a575ba8b-2264-4f14-8f59-9eeb805e5a37",
        bet_request_status_id=1,
        bet_request_user_id="a6a1eb91-6217-4e0c-b759-fbcaa2b7a8ac",
        bet_type_name="Win",
        competition_name="Hamilton Park",
        count_in_place=None,
        fill_percentage=0.0,
        fixture_name="Hamilton Park",
        fixture_start_date="2021-07-15 12:00:00",
        market_name="Race Winner",
        matched_stake=0,
        price={"decimal": "1.16", "fraction": {"denominator": 25, "numerator": 4}},
        profit=0,
        region_iso="scotland",
        region_name="Scotland",
        selection_name="Misty Ayr",
        sport_external_id=14,
        sport_name="Horse Racing",
        sport_slug="horse-racing",
        stake=1000,
        status_name="Active",
        status_slug="active",
    )


@pytest.fixture()
def mock_customer_order_ref_resource() -> resources.CustomerOrderRef:
    customer_order_ref_gen = resources.CustomerOrderRef.generate_random_order_ref()
    return resources.CustomerOrderRef(customer_order_ref=customer_order_ref_gen)


@pytest.fixture()
def mock_customer_strategy_ref_resource() -> resources.CustomerStrategyRef:
    customer_strategy_ref_value = "best_strategy"
    return resources.CustomerStrategyRef(
        customer_strategy_ref=customer_strategy_ref_value
    )
