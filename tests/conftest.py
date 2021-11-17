from betconnect import endpoints
import pytest
from betconnect.apiclient import APIClient
from betconnect.baseclient import BaseClient
from requests import sessions
from betconnect.enums import Envirnoment
from decouple import config
from requests import Response
from typing import Tuple, Dict, Any
from tests.utils import build_path, load_pickle, load_json


@pytest.fixture
def mock_base_client() -> BaseClient:
    return BaseClient(username='test',
                      password='123',
                      api_key="456",
                      environment=Envirnoment.STAGING
                      )


@pytest.fixture
def mock_api_client() -> APIClient:
    return APIClient(username='test', password='123', api_key='456', environment=Envirnoment.STAGING)


@pytest.fixture
def staging_api_client() -> APIClient:
    return APIClient(username=config('STAGING_BETCONNECT_USERNAME'), password=config('STAGING_BETCONNECT_PASSWORD'),
                     api_key=config('STAGING_BETCONNECT_API_KEY'), environment=Envirnoment.STAGING)


@pytest.fixture
def staging_lay_api_client() -> APIClient:
    return APIClient(username=config('STAGING_BETCONNECT_LAY_USERNAME'), password=config('STAGING_BETCONNECT_LAY_PASSWORD'),
                     api_key=config('STAGING_BETCONNECT_LAY_API_KEY'), environment=Envirnoment.STAGING)


@pytest.fixture
def mock_betting_endpoint(staging_api_client) -> endpoints.Betting:
    return endpoints.Betting(staging_api_client)


@pytest.fixture
def mock_login_endpoint(staging_api_client) -> endpoints.Login:
    return endpoints.Login(staging_api_client)


@pytest.fixture()
def mock_login_response_pkl() -> Response:
    return load_pickle(build_path('resources/endpoints/login/mock_login_response_success.pkl'))


@pytest.fixture()
def mock_login_response_json() -> Dict[str, Any]:
    return load_json(build_path('resources/endpoints/login/mock_login_response_success.json'))


@pytest.fixture()
def mock_login_response(mock_login_response_pkl: Response, mock_login_response_json: Dict[str, Any]) -> Tuple[
    Response, Dict[str, Any], float]:
    return mock_login_response_pkl, mock_login_response_json, 1.0


@pytest.fixture()
def mock_login_response_failure_pkl() -> Response:
    return load_pickle(build_path('resources/endpoints/login/mock_login_response_failure.pkl'))


@pytest.fixture()
def mock_login_response_failure_json() -> Dict[str, Any]:
    return load_json(build_path('resources/endpoints/login/mock_login_response_failure.json'))


@pytest.fixture()
def mock_login_failure_response(mock_login_response_failure_pkl: Response,
                                mock_login_response_failure_json: Dict[str, Any]) -> Tuple[
    Response, Dict[str, Any], float]:
    return mock_login_response_failure_pkl, mock_login_response_failure_json, 1.0


@pytest.fixture()
def mock_logout_response_pkl() -> Response:
    return load_pickle(build_path('resources/endpoints/login/mock_logout_response_success.pkl'))


@pytest.fixture()
def mock_logout_response_json() -> Dict[str, Any]:
    return load_json(build_path('resources/endpoints/login/mock_logout_response_success.json'))


@pytest.fixture()
def mock_logout_response(mock_logout_response_pkl: Response, mock_logout_response_json: Dict[str, Any]) -> Tuple[
    Response, Dict[str, Any], float]:
    return mock_logout_response_pkl, mock_logout_response_json, 1.0


@pytest.fixture()
def mock_logout_response_failure_pkl() -> Response:
    return load_pickle(build_path('resources/endpoints/login/mock_logout_response_failure.pkl'))


@pytest.fixture()
def mock_logout_response_failure_json() -> Dict[str, Any]:
    return load_json(build_path('resources/endpoints/login/mock_logout_response_failure.json'))


@pytest.fixture()
def mock_logout_failure_response(mock_logout_response_failure_pkl: Response,
                                 mock_logout_response_failure_json: Dict[str, Any]) -> Tuple[
    Response, Dict[str, Any], float]:
    return mock_logout_response_failure_pkl, mock_logout_response_failure_json, 1.0

@pytest.fixture()
def mock_active_bookmakers_pkl() -> Response:
    return load_pickle(build_path('resources/endpoints/betting/active_bookmakers_response.pkl'))


@pytest.fixture()
def mock_active_bookmakers_json() -> Dict[str, Any]:
    return load_json(build_path('resources/endpoints/betting/active_bookmakers_response.json'))


@pytest.fixture()
def mock_active_bookmakers_response(mock_active_bookmakers_pkl: Response,
                                 mock_active_bookmakers_json: Dict[str, Any]) -> Tuple[
    Response, Dict[str, Any], float]:
    return mock_active_bookmakers_pkl, mock_active_bookmakers_json, 1.0

@pytest.fixture()
def mock_active_sports_pkl() -> Response:
    return load_pickle(build_path('resources/endpoints/betting/active_sports_response.pkl'))


@pytest.fixture()
def mock_active_sports_json() -> Dict[str, Any]:
    return load_json(build_path('resources/endpoints/betting/active_sports_response.json'))


@pytest.fixture()
def mock_active_sports_response(mock_active_sports_pkl: Response,
                                 mock_active_sports_json: Dict[str, Any]) -> Tuple[
    Response, Dict[str, Any], float]:
    return mock_active_sports_pkl, mock_active_sports_json, 1.0

@pytest.fixture()
def mock_active_regions_pkl() -> Response:
    return load_pickle(build_path('resources/endpoints/betting/active_regions_response.pkl'))


@pytest.fixture()
def mock_active_regions_json() -> Dict[str, Any]:
    return load_json(build_path('resources/endpoints/betting/active_regions_response.json'))


@pytest.fixture()
def mock_active_regions_response(mock_active_regions_pkl: Response,
                                 mock_active_regions_json: Dict[str, Any]) -> Tuple[
    Response, Dict[str, Any], float]:
    return mock_active_regions_pkl, mock_active_regions_json, 1.0

@pytest.fixture()
def mock_active_competitions_pkl() -> Response:
    return load_pickle(build_path('resources/endpoints/betting/active_competitions_response.pkl'))


@pytest.fixture()
def mock_active_competitions_json() -> Dict[str, Any]:
    return load_json(build_path('resources/endpoints/betting/active_competitions_response.json'))


@pytest.fixture()
def mock_active_competitions_response(mock_active_competitions_pkl: Response,
                                 mock_active_competitions_json: Dict[str, Any]) -> Tuple[
    Response, Dict[str, Any], float]:
    return mock_active_competitions_pkl, mock_active_competitions_json, 1.0

@pytest.fixture()
def mock_active_fixtures_pkl() -> Response:
    return load_pickle(build_path('resources/endpoints/betting/active_fixtures_response.pkl'))


@pytest.fixture()
def mock_active_fixtures_json() -> Dict[str, Any]:
    return load_json(build_path('resources/endpoints/betting/active_fixtures_response.json'))


@pytest.fixture()
def mock_active_fixtures_response(mock_active_fixtures_pkl: Response,
                                 mock_active_fixtures_json: Dict[str, Any]) -> Tuple[
    Response, Dict[str, Any], float]:
    return mock_active_fixtures_pkl, mock_active_fixtures_json, 1.0

@pytest.fixture()
def mock_active_market_types_pkl() -> Response:
    return load_pickle(build_path('resources/endpoints/betting/active_market_types_response.pkl'))


@pytest.fixture()
def mock_active_market_types_json() -> Dict[str, Any]:
    return load_json(build_path('resources/endpoints/betting/active_market_types_response.json'))


@pytest.fixture()
def mock_active_market_types_response(mock_active_market_types_pkl: Response,
                                 mock_active_market_types_json: Dict[str, Any]) -> Tuple[
    Response, Dict[str, Any], float]:
    return mock_active_market_types_pkl, mock_active_market_types_json, 1.0

@pytest.fixture()
def mock_active_markets_pkl() -> Response:
    return load_pickle(build_path('resources/endpoints/betting/active_markets_response.pkl'))


@pytest.fixture()
def mock_active_markets_json() -> Dict[str, Any]:
    return load_json(build_path('resources/endpoints/betting/active_markets_response.json'))


@pytest.fixture()
def mock_active_markets_response(mock_active_markets_pkl: Response,
                                 mock_active_markets_json: Dict[str, Any]) -> Tuple[
    Response, Dict[str, Any], float]:
    return mock_active_markets_pkl, mock_active_markets_json, 1.0

@pytest.fixture()
def mock_active_selections_pkl() -> Response:
    return load_pickle(build_path('resources/endpoints/betting/active_selections_response.pkl'))


@pytest.fixture()
def mock_active_selections_json() -> Dict[str, Any]:
    return load_json(build_path('resources/endpoints/betting/active_selections_response.json'))


@pytest.fixture()
def mock_active_selections_response(mock_active_selections_pkl: Response,
                                 mock_active_selections_json: Dict[str, Any]) -> Tuple[
    Response, Dict[str, Any], float]:
    return mock_active_selections_pkl, mock_active_selections_json, 1.0

@pytest.fixture()
def mock_bet_history_pkl() -> Response:
    return load_pickle(build_path('resources/endpoints/betting/bet_history_response.pkl'))


@pytest.fixture()
def mock_bet_history_json() -> Dict[str, Any]:
    return load_json(build_path('resources/endpoints/betting/bet_history_response.json'))


@pytest.fixture()
def mock_bet_history_response(mock_bet_history_pkl: Response,
                                 mock_bet_history_json: Dict[str, Any]) -> Tuple[
    Response, Dict[str, Any], float]:
    return mock_bet_history_pkl, mock_bet_history_json, 1.0

@pytest.fixture()
def mock_get_balance_pkl() -> Response:
    return load_pickle(build_path('resources/endpoints/betting/get_balance_response.pkl'))


@pytest.fixture()
def mock_get_balance_json() -> Dict[str, Any]:
    return load_json(build_path('resources/endpoints/betting/get_balance_response.json'))


@pytest.fixture()
def mock_get_balance_response(mock_get_balance_pkl: Response,
                                 mock_get_balance_json: Dict[str, Any]) -> Tuple[
    Response, Dict[str, Any], float]:
    return mock_get_balance_pkl, mock_get_balance_json, 1.0

@pytest.fixture()
def mock_prices_pkl() -> Response:
    return load_pickle(build_path('resources/endpoints/betting/prices_response.pkl'))


@pytest.fixture()
def mock_prices_json() -> Dict[str, Any]:
    return load_json(build_path('resources/endpoints/betting/prices_response.json'))


@pytest.fixture()
def mock_prices_response(mock_prices_pkl: Response,
                                 mock_prices_json: Dict[str, Any]) -> Tuple[
    Response, Dict[str, Any], float]:
    return mock_prices_pkl, mock_prices_json, 1.0

@pytest.fixture()
def mock_bet_request_create_pkl() -> Response:
    return load_pickle(build_path('resources/endpoints/betting/bet_request_create_response.pkl'))


@pytest.fixture()
def mock_bet_request_create_json() -> Dict[str, Any]:
    return load_json(build_path('resources/endpoints/betting/bet_request_create_response.json'))


@pytest.fixture()
def mock_bet_request_create_response(mock_bet_request_create_pkl: Response,
                                 mock_bet_request_create_json: Dict[str, Any]) -> Tuple[
    Response, Dict[str, Any], float]:
    return mock_bet_request_create_pkl, mock_bet_request_create_json, 1.0

@pytest.fixture()
def mock_bet_request_get_pkl() -> Response:
    return load_pickle(build_path('resources/endpoints/betting/bet_request_get_response.pkl'))


@pytest.fixture()
def mock_bet_request_get_json() -> Dict[str, Any]:
    return load_json(build_path('resources/endpoints/betting/bet_request_get_response.json'))


@pytest.fixture()
def mock_bet_request_get_response(mock_bet_request_get_pkl: Response,
                                 mock_bet_request_get_json: Dict[str, Any]) -> Tuple[
    Response, Dict[str, Any], float]:
    return mock_bet_request_get_pkl, mock_bet_request_get_json, 1.0

@pytest.fixture()
def mock_bet_request_match_pkl() -> Response:
    return load_pickle(build_path('resources/endpoints/betting/bet_request_match_response.pkl'))


@pytest.fixture()
def mock_bet_request_match_json() -> Dict[str, Any]:
    return load_json(build_path('resources/endpoints/betting/bet_request_match_response.json'))


@pytest.fixture()
def mock_bet_request_match_response(mock_bet_request_match_pkl: Response,
                                    mock_bet_request_match_json: Dict[str, Any]) -> Tuple[
    Response, Dict[str, Any], float]:
    return mock_bet_request_match_pkl, mock_bet_request_match_json, 1.0

@pytest.fixture()
def mock_bet_request_stop_pkl() -> Response:
    return load_pickle(build_path('resources/endpoints/betting/bet_request_stop_response.pkl'))


@pytest.fixture()
def mock_bet_request_stop_json() -> Dict[str, Any]:
    return load_json(build_path('resources/endpoints/betting/bet_request_stop_response.json'))


@pytest.fixture()
def mock_bet_request_stop_response(mock_bet_request_stop_pkl: Response,
                                 mock_bet_request_stop_json: Dict[str, Any]) -> Tuple[
    Response, Dict[str, Any], float]:
    return mock_bet_request_stop_pkl, mock_bet_request_stop_json, 1.0



@pytest.fixture()
def mock_bet_request_match_more_pkl() -> Response:
    return load_pickle(build_path('resources/endpoints/betting/bet_request_match_more_response.pkl'))


@pytest.fixture()
def mock_bet_request_match_more_json() -> Dict[str, Any]:
    return load_json(build_path('resources/endpoints/betting/bet_request_match_more_response.json'))


@pytest.fixture()
def mock_bet_request_match_more_response(mock_bet_request_match_more_pkl: Response,
                                    mock_bet_request_match_more_json: Dict[str, Any]) -> Tuple[
    Response, Dict[str, Any], float]:
    return mock_bet_request_match_more_pkl, mock_bet_request_match_more_json, 1.0

@pytest.fixture()
def mock_get_active_bet_requests_pkl() -> Response:
    return load_pickle(build_path('resources/endpoints/betting/get_active_bet_requests_response.pkl'))


@pytest.fixture()
def mock_get_active_bet_requests_json() -> Dict[str, Any]:
    return load_json(build_path('resources/endpoints/betting/get_active_bet_requests_response.json'))


@pytest.fixture()
def mock_bet_get_active_bet_requests_response(mock_get_active_bet_requests_pkl: Response,
                                    mock_get_active_bet_requests_json: Dict[str, Any]) -> Tuple[
    Response, Dict[str, Any], float]:
    return mock_get_active_bet_requests_pkl, mock_get_active_bet_requests_json, 1.0

@pytest.fixture()
def mock_get_viewed_next_page_pkl() -> Response:
    return load_pickle(build_path('resources/endpoints/betting/get_viewed_next_page_response.pkl'))


@pytest.fixture()
def mock_get_viewed_next_page_json() -> Dict[str, Any]:
    return load_json(build_path('resources/endpoints/betting/get_viewed_next_page_response.json'))


@pytest.fixture()
def mock_get_viewed_next_page_response(mock_get_viewed_next_page_pkl: Response,
                                    mock_get_viewed_next_page_json: Dict[str, Any]) -> Tuple[
    Response, Dict[str, Any], float]:
    return mock_get_viewed_next_page_pkl, mock_get_viewed_next_page_json, 1.0


@pytest.fixture()
def mock_status_pkl() -> Response:
    return load_pickle(build_path('resources/endpoints/login/mock_status.pkl'))


@pytest.fixture()
def mock_status_json() -> Dict[str, Any]:
    return load_json(build_path('resources/endpoints/login/mock_status.json'))


@pytest.fixture()
def mock_status_response(mock_status_pkl: Response,
                                    mock_status_json: Dict[str, Any]) -> Tuple[
    Response, Dict[str, Any], float]:
    return mock_status_pkl, mock_status_json, 1.0



