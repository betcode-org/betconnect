from betconnect.endpoints import Betting
from betconnect import resources
from betconnect.apiclient import APIClient
from typing import Tuple, Dict, Any
from requests import Response
from pytest_mock import mocker


class TestBetting:

    def test___init__(self, mock_api_client: APIClient):
        configuration = Betting(mock_api_client)
        assert configuration.client == mock_api_client

    def test_active_bookmakers(self, mocker, mock_betting_endpoint: Betting, mock_active_bookmakers_response: Tuple[
        Response, Dict[str, Any], float]):
        request = mocker.patch('betconnect.endpoints.baseendpoint.BaseEndpoint.request',
                               return_value=mock_active_bookmakers_response)
        active_bookmakers = mock_betting_endpoint.active_bookmakers()
        assert isinstance(active_bookmakers, list)
        for s in active_bookmakers:
            assert isinstance(s, resources.ActiveBookmakers)
        request.assert_called()

    def test_active_competitions(self, mocker, mock_betting_endpoint: Betting,
                                 mock_active_competitions_response: Tuple[Response, Dict[str, Any], float]):
        request = mocker.patch('betconnect.endpoints.baseendpoint.BaseEndpoint.request',
                               return_value=mock_active_competitions_response)
        active_competitions = mock_betting_endpoint.active_competitions(sport_id=14, region_id=3795032)
        assert isinstance(active_competitions, list)
        for r in active_competitions:
            assert isinstance(r, resources.ActiveCompetitions)
        request.assert_called()

    def test_active_fixtures(self, mocker, mock_betting_endpoint: Betting,
                             mock_active_fixtures_response: Tuple[Response, Dict[str, Any], float]):
        request = mocker.patch('betconnect.endpoints.baseendpoint.BaseEndpoint.request',
                               return_value=mock_active_fixtures_response)
        active_fixtures = mock_betting_endpoint.active_fixtures(sport_id=14)
        assert isinstance(active_fixtures, list)
        for r in active_fixtures:
            assert isinstance(r, resources.ActiveFixtures)

        active_fixtures = mock_betting_endpoint.active_fixtures(sport_id=14, region_id=3795032)
        assert isinstance(active_fixtures, list)
        for r in active_fixtures:
            assert isinstance(r, resources.ActiveFixtures)

        active_fixtures = mock_betting_endpoint.active_fixtures(sport_id=14, region_id=3795032, competition_id=828)
        assert isinstance(active_fixtures, list)
        for r in active_fixtures:
            assert isinstance(r, resources.ActiveFixtures)
        request.assert_called()

    def test_active_market_types(self, mocker, mock_betting_endpoint: Betting, mock_active_market_types_response: Tuple[
        Response, Dict[str, Any], float]):
        request = mocker.patch('betconnect.endpoints.baseendpoint.BaseEndpoint.request',
                               return_value=mock_active_market_types_response)
        active_market_types = mock_betting_endpoint.active_market_types(sport_id=14)
        assert isinstance(active_market_types, list)
        for r in active_market_types:
            assert isinstance(r, resources.ActiveMarketTypes)
        request.assert_called()

    def test_active_markets(self, mocker, mock_betting_endpoint: Betting, mock_active_markets_response: Tuple[
        Response, Dict[str, Any], float]):
        request = mocker.patch('betconnect.endpoints.baseendpoint.BaseEndpoint.request',
                               return_value=mock_active_markets_response)
        active_markets = mock_betting_endpoint.active_markets(fixture_id=8573302)
        assert isinstance(active_markets, list)
        for r in active_markets:
            assert isinstance(r, resources.ActiveMarkets)

        active_markets = mock_betting_endpoint.active_markets(fixture_id=8573302, grouped=True)
        assert isinstance(active_markets, list)
        for r in active_markets:
            assert isinstance(r, resources.ActiveMarkets)

        request.assert_called()

    def test_active_regions(self, mocker, mock_betting_endpoint: Betting,
                            mock_active_regions_response: Tuple[Response, Dict[str, Any], float]):

        request = mocker.patch('betconnect.endpoints.baseendpoint.BaseEndpoint.request',
                               return_value=mock_active_regions_response)

        active_regions = mock_betting_endpoint.active_regions(sport_id=14)
        assert isinstance(active_regions, list)
        for r in active_regions:
            assert isinstance(r, resources.ActiveRegion)
        request.assert_called()

    def test_active_sports(self, mocker, mock_betting_endpoint: Betting, mock_active_sports_response: Tuple[
        Response, Dict[str, Any], float]):
        request = mocker.patch('betconnect.endpoints.baseendpoint.BaseEndpoint.request',
                               return_value=mock_active_sports_response)

        active_sports = mock_betting_endpoint.active_sports()
        assert isinstance(active_sports, list)
        for s in active_sports:
            assert isinstance(s, resources.ActiveSports)
        request.assert_called()

        active_sports = mock_betting_endpoint.active_sports(with_bets=True)
        assert isinstance(active_sports, list)
        for s in active_sports:
            assert isinstance(s, resources.ActiveSports)
        request.assert_called()

    def test_active_selections(self, mocker, mock_betting_endpoint: Betting, mock_active_selections_response: Tuple[
        Response, Dict[str, Any], float]):

        active_selections = mock_betting_endpoint.active_selections(fixture_id=8573295, market_type_id=6)

        request = mocker.patch('betconnect.endpoints.baseendpoint.BaseEndpoint.request',
                               return_value=mock_active_selections_response)
        active_selections = mock_betting_endpoint.active_selections(fixture_id=8573302, market_type_id=6)
        assert isinstance(active_selections, list)
        for r in active_selections:
            assert isinstance(r, resources.ActiveSelections)

        active_selections = mock_betting_endpoint.active_selections(fixture_id=8234079, market_type_id=6, handicap=True)
        assert isinstance(active_selections, list)
        for r in active_selections:
            assert isinstance(r, resources.ActiveSelections)

        request.assert_called()

    def test_bet_history(self, mocker, mock_betting_endpoint: Betting, mock_bet_history_response: Tuple[
        Response, Dict[str, Any], float]):
        request = mocker.patch('betconnect.endpoints.baseendpoint.BaseEndpoint.request',
                               return_value=mock_bet_history_response)
        bet_history = mock_betting_endpoint.bet_history(username='varneyo', status=6)
        assert isinstance(bet_history, resources.BetHistoryRequest)
        request.assert_called()

    def test_get_balance(self, mocker, mock_betting_endpoint: Betting, mock_get_balance_response: Tuple[
        Response, Dict[str, Any], float]):
        request = mocker.patch('betconnect.endpoints.baseendpoint.BaseEndpoint.request',
                               return_value=mock_get_balance_response)
        balance = mock_betting_endpoint.get_balance()
        assert isinstance(balance, resources.Balance)
        request.assert_called()

    def test_prices(self, mocker, mock_betting_endpoint: Betting, mock_prices_response: Tuple[
        Response, Dict[str, Any], float]):
        request = mocker.patch('betconnect.endpoints.baseendpoint.BaseEndpoint.request',
                               return_value=mock_prices_response)
        prices = mock_betting_endpoint.prices(
            fixture_id=8573295,
            market_type_id=6,
            competitor='1247097'
        )
        assert isinstance(prices, list)
        for p in prices:
            assert isinstance(p, resources.Price)
        request.assert_called()

    def test_bet_request_get(self, mocker, staging_lay_api_client, mock_betting_endpoint: Betting,
                             mock_bet_request_get_response: Tuple[
                                 Response, Dict[str, Any], float]):
        request = mocker.patch('betconnect.endpoints.baseendpoint.BaseEndpoint.post',
                               return_value=mock_bet_request_get_response)
        bet_request = mock_betting_endpoint.bet_request_get(
            filter=resources.GetBetRequestFilter(
                sport_id=14,
                bet_request_id='712d7387-c059-4d58-be66-12eccdeed384'
            )
        )
        assert isinstance(bet_request, resources.BetRequest)
        request.assert_called()

    def test_bet_request_create(self, mocker, mock_betting_endpoint: Betting, mock_bet_request_create_response: Tuple[
        Response, Dict[str, Any], float]):
        request = mocker.patch('betconnect.endpoints.baseendpoint.BaseEndpoint.post',
                               return_value=mock_bet_request_create_response)
        bet_request = mock_betting_endpoint.bet_request_create(
            filter=resources.CreateBetRequestFilter(
                fixture_id=8573295,
                market_type_id=6,
                competitor='1247097',
                price=2.63,
                stake=100,
                bet_type='Win'
            )
        )
        assert isinstance(bet_request, resources.BetRequestCreate)
        request.assert_called()

    def test_bet_request_match(self, mocker, staging_lay_api_client: APIClient, mock_betting_endpoint: Betting,
                               mock_bet_request_match_response: Tuple[
                                   Response, Dict[str, Any], float]):
        request = mocker.patch('betconnect.endpoints.baseendpoint.BaseEndpoint.patch',
                               return_value=mock_bet_request_match_response)
        mock_betting_endpoint.client = staging_lay_api_client
        bet_request_match = mock_betting_endpoint.bet_request_match(
            bet_request_id='d05215ce-d46f-40fd-8fc6-232dedcfdce4',
            accepted_stake=10

        )
        assert isinstance(bet_request_match, resources.BetRequestMatch)
        request.assert_called()

    def test_bet_request_match_more(self, mocker, mock_betting_endpoint, staging_lay_api_client,
                                    mock_bet_request_match_more_response: Tuple[
                                        Response, Dict[str, Any], float]):
        request = mocker.patch('betconnect.endpoints.baseendpoint.BaseEndpoint.patch',
                               return_value=mock_bet_request_match_more_response)
        mock_betting_endpoint.client = staging_lay_api_client
        bet_request = mock_betting_endpoint.bet_request_match_more(
            bet_request_id='d05215ce-d46f-40fd-8fc6-232dedcfdce4',
            requested_stake=50

        )
        assert isinstance(bet_request, resources.BetRequestMatchMore)

    def test_bet_request_stop(self, mocker, mock_betting_endpoint: Betting, mock_bet_request_stop_response: Tuple[
        Response, Dict[str, Any], float]):
        request = mocker.patch('betconnect.endpoints.baseendpoint.BaseEndpoint.post',
                               return_value=mock_bet_request_stop_response)
        bet_request_stop = mock_betting_endpoint.bet_request_stop(
            bet_request_id='d05215ce-d46f-40fd-8fc6-232dedcfdce4'
        )
        assert isinstance(bet_request_stop, resources.ResponseMessage)
        request.assert_called()

    def test_get_active_bet_requests(self, mocker, mock_betting_endpoint: Betting,
                                     mock_bet_get_active_bet_requests_response: Tuple[
                                         Response, Dict[str, Any], float]):
        request = mocker.patch('betconnect.endpoints.baseendpoint.BaseEndpoint.request',
                               return_value=mock_bet_get_active_bet_requests_response)
        active_bets = mock_betting_endpoint.get_active_bet_requests()
        assert isinstance(active_bets, resources.ActiveBetsRequest)
        request.assert_called()

    def test_get_viewed_next_page(self, mocker, mock_betting_endpoint: Betting,
                                     mock_get_viewed_next_page_response: Tuple[
                                         Response, Dict[str, Any], float]):
        request = mocker.patch('betconnect.endpoints.baseendpoint.BaseEndpoint.request',
                              return_value=mock_get_viewed_next_page_response)
        next_page = mock_betting_endpoint.get_viewed_next_page(bet_request_id='test',sport_id=14)
        assert isinstance(next_page, resources.Viewed)
        request.assert_called()
