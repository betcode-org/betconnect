from .baseendpoint import BaseEndpoint
from betconnect import resources
from typing import Union, List
import requests
import json
from tests.utils import save_data_to_pickle_file, save_json_to_file


class Betting(BaseEndpoint):
    _METHOD_URIS = {
        'active_bookmakers': 'api/v2/active_bookmakers',
        'active_sports': 'api/v2/active_sports',
        'active_sports_with_bets': 'api/v2/active_sports/True',
        'active_regions': 'api/v2/active_regions/{}',
        'active_competitions': 'api/v2/active_competitions/{}/{}',
        'active_fixtures': 'api/v2/active_fixtures/{}',
        'active_fixtures_region': 'api/v2/active_fixtures/{}/{}',
        'active_fixtures_region_competition': 'api/v2/active_fixtures/{}/{}/{}',
        'active_market_types': 'api/v2/active_market_types/{}',
        'active_markets': 'api/v2/active_markets/{}',
        'active_markets_grouped': 'api/v2/active_markets/{}/grouped',
        'active_selections': 'api/v2/active_selections/{}/{}',
        'active_selections_handicap': 'api/v2/active_selections/{}/{}/handicap',
        'bet_history': 'api/v2/bet_history/back/{}/{}',
        'bet_history_limits': 'api/v2/bet_history/back/{}/{}/{}/{}',
        'bet_request_create': 'api/v2/bet_request_create',
        'bet_request_get': 'api/v2/bet_request_get',
        'bet_request_match': 'api/v2/bet_request_match',
        'bet_request_match_more': 'api/v2/bet_request_match_more',
        'bet_request_reject': 'api/v2/bet_request_reject',
        'bet_request_stop': 'api/v2/bet_request_stop',
        'get_active_bet_requests': 'api/v2/get_active_bet_requests',
        'get_active_bet_requests_limit_page': 'api/v2/get_active_bet_requests/{}/{}',
        'my_bets': 'api/v2/my_bets/{}/{}/{}',
        'my_bets_get_all': 'api/v2/my_bets/{}/{}/{}/{}/{}',
        'prices': 'api/v2/prices/{}/{}/{}',
        'prices_handicap': 'api/v2/prices/{}/{}/{}/{}',
        'get_balance': '/api/v2/get_balance',
        'get_viewed_next_prev': '/api/v2/get_viewed_next_prev/{}',
        'get_viewed_next_prev_sport': '/api/v2/get_viewed_next_prev/{}/{}',
        'selections_for_market': 'api/v2/selections_for_market/{}/{}',
        'selections_for_market_top_price': 'api/v2/selections_for_market/{}/{}/{}'
    }

    def active_bookmakers(self) -> List[resources.ActiveBookmakers]:
        """
        Returns an list of active sports
        :return: List of ActiveBookmakers
        """

        method_uri = self._METHOD_URIS['active_bookmakers']

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={})

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveBookmakers,
            elapsed_time=elapsed_time
        )

    def active_sports(self, with_bets: bool = None) -> List[resources.ActiveSports]:
        if with_bets:
            method_uri = self._METHOD_URIS['active_sports_with_bets']
        else:
            method_uri = self._METHOD_URIS['active_sports']

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={})

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveSports,
            elapsed_time=elapsed_time
        )

    def active_regions(self,
                       sport_id: int) -> List[resources.ActiveRegion]:

        method_uri = self._METHOD_URIS['active_regions'].format(sport_id)

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={})

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveRegion,
            elapsed_time=elapsed_time
        )

    def active_competitions(self,
                            sport_id: int,
                            region_id: int
                            ) -> List[resources.ActiveCompetitions]:

        method_uri = self._METHOD_URIS['active_competitions'].format(sport_id, region_id)

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={})

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveCompetitions,
            elapsed_time=elapsed_time
        )

    def active_fixtures(self,
                        sport_id: int,
                        region_id: int = None,
                        competition_id: int = None
                        ) -> List[resources.ActiveFixtures]:

        if competition_id:
            method_uri = self._METHOD_URIS['active_fixtures_region_competition'].format(sport_id, region_id,
                                                                                        competition_id)
        elif region_id:
            method_uri = self._METHOD_URIS['active_fixtures_region'].format(sport_id, region_id)
        else:
            method_uri = self._METHOD_URIS['active_fixtures'].format(sport_id)

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={})

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveFixtures,
            elapsed_time=elapsed_time
        )

    def active_market_types(self, sport_id: int) -> List[resources.ActiveMarketTypes]:
        method_uri = self._METHOD_URIS['active_market_types'].format(sport_id)

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={})

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveMarketTypes,
            elapsed_time=elapsed_time
        )

    def active_markets(self, fixture_id: int, grouped: bool = None) -> List[resources.ActiveMarkets]:
        if grouped:
            method_uri = self._METHOD_URIS['active_markets_grouped'].format(fixture_id)
        else:
            method_uri = self._METHOD_URIS['active_markets'].format(fixture_id)

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={})

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveMarkets,
            elapsed_time=elapsed_time
        )

    def active_selections(self, fixture_id: int, market_type_id: int, handicap: bool = None) -> List[
        resources.ActiveSelections]:
        if handicap:
            method_uri = self._METHOD_URIS['active_selections_handicap'].format(fixture_id, market_type_id, handicap)
        else:
            method_uri = self._METHOD_URIS['active_selections'].format(fixture_id, market_type_id)

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={})

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveSelections,
            elapsed_time=elapsed_time
        )

    def get_fixtures_with_active_selections(self,
                                            sport_id: int,
                                            market_type_id: int,
                                            handicap: bool = False,
                                            region_id: int = None,
                                            competition_id: int = None
                                            ) -> List[resources.ActiveFixtures]:
        active_fixtures = self.active_fixtures(
            sport_id=sport_id,
            region_id=region_id,
            competition_id=competition_id
        )
        for fixture in active_fixtures:
            selections = self.active_selections(
                fixture_id=fixture.fixture_id,
                market_type_id=market_type_id,
                handicap=handicap
            )
            if selections:
                for selection in selections:
                    price = self.prices(
                        fixture_id=fixture.fixture_id,
                        market_type_id=market_type_id,
                        competitor=selection.competitor,
                        handicap=handicap
                    )
                    if price:
                        selection.add_prices(price)
                    fixture.add_selections(selection)
        return active_fixtures

    def bet_request_create(self,
                           filter: resources.CreateBetRequestFilter
                           ) -> resources.BetRequestCreate:

        method_uri = self._METHOD_URIS['bet_request_create']

        (response, response_json, elapsed_time) = self.post(
            method_uri=method_uri,
            data=filter.dict(exclude_none=True)
        )
        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.BetRequestCreate,
            elapsed_time=elapsed_time,
        )

    def bet_request_get(self,
                        filter: resources.GetBetRequestFilter
                        ) -> resources.BetRequest:

        method_uri = self._METHOD_URIS['bet_request_get']

        if filter.bet_request_id:
            (response, response_json, elapsed_time) = self.post(
                method_uri=method_uri,
                data=filter.dict(exclude={'sport_id','bookmakers','min_odds','max_odds','accept_each_way'})
            )
        else:
            (response, response_json, elapsed_time) = self.post(
                method_uri=method_uri,
                data=filter.dict(exclude={'bet_request_id'})
            )


        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.BetRequest,
            elapsed_time=elapsed_time
        )

    def selections_for_market(self,
                              fixture_id: int,
                              market_type_id: int,
                              top_price_only: bool = None
                              ) -> resources.BetRequest:
        if top_price_only:
            assert isinstance(top_price_only, bool)
            method_uri = self._METHOD_URIS['selections_for_market_top_price'].format(fixture_id, market_type_id,
                                                                                     top_price_only)
        else:
            method_uri = self._METHOD_URIS['selections_for_market'].format(fixture_id, market_type_id)

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={})

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.SelectionsForMarket,
            elapsed_time=elapsed_time
        )

    def bet_request_match(self,
                          bet_request_id: str,
                          accepted_stake: int
                          ) -> resources.BetRequestMatch:

        method_uri = self._METHOD_URIS['bet_request_match'].format(accepted_stake)

        (response, response_json, elapsed_time) = self.patch(method_uri=method_uri, data={
            "bet_request_id": bet_request_id,
            "accepted_stake": accepted_stake
        })

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.BetRequestMatch,
            elapsed_time=elapsed_time
        )

    def bet_request_match_more(self,
                               bet_request_id: str,
                               requested_stake: float
                               ):

        method_uri = self._METHOD_URIS['bet_request_match_more']

        (response, response_json, elapsed_time) = self.patch(method_uri=method_uri, data={
            "bet_request_id": bet_request_id,
            "requested_stake": requested_stake
        })

        save_data_to_pickle_file('bet_request_match_more_response.pkl', response)
        save_json_to_file('bet_request_match_more_response.json', response_json)
        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.BetRequestMatch,
            elapsed_time=elapsed_time
        )

    def bet_request_reject(self):

        method_uri = self._METHOD_URIS['bet_request_reject']

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={})

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveSelections,
            elapsed_time=elapsed_time
        )

    def bet_request_stop(self,
                         bet_request_id: str,
                         stop_bet_reason: str = None
                         ):
        data = {
            'bet_request_id': bet_request_id,
            'stop_bet_reason': stop_bet_reason
        }
        method_uri = self._METHOD_URIS['bet_request_stop']

        (response, response_json, elapsed_time) = self.post(method_uri=method_uri, params={})

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveSelections,
            elapsed_time=elapsed_time
        )

    def get_active_bet_requests(self,
                                limit: int = None,
                                page: int = None
                                )->List[resources.ActiveBets]:
        if limit and page:
            method_uri = self._METHOD_URIS['get_active_bet_requests_limit_page'].format(limit, page)
        else:
            method_uri = self._METHOD_URIS['get_active_bet_requests']

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={},authenticated=True)

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveBetsRequest,
            elapsed_time=elapsed_time
        )


    def my_bets(self,
                side: str,
                user_id: str,
                status: str,
                limit: int = None,
                page: int = None,
                get_all: bool = None
                ):
        if get_all:
            method_uri = self._METHOD_URIS['my_bets_get_all'].format(side, user_id, status)
        else:
            method_uri = self._METHOD_URIS['my_bets'].format(side, user_id, status)

        (response, response_json, elapsed_time) = self.post(method_uri=method_uri, params={})

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveSelections,
            elapsed_time=elapsed_time
        )

    def prices(self,
               fixture_id: int,
               market_type_id: int,
               competitor: str,
               handicap: float = None
               ) -> List[resources.Price]:

        if handicap:
            method_uri = self._METHOD_URIS['prices'].format(fixture_id, market_type_id, competitor, handicap)
        else:
            method_uri = self._METHOD_URIS['prices'].format(fixture_id, market_type_id, competitor)

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={})

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.Price,
            elapsed_time=elapsed_time
        )

    def bet_history(self,
                    username: str,
                    status: str,
                    limit: int = None,
                    page: int = None
                    ) -> resources.BetHistoryRequest:

        if limit is None:
            method_uri = self._METHOD_URIS['bet_history'].format(username, status)
        else:
            method_uri = self._METHOD_URIS['bet_history_limits'].format(username, status, limit, page)

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={}, authenticated=True)

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.BetHistoryRequest,
            elapsed_time=elapsed_time
        )

    def get_balance(self):

        method_uri = self._METHOD_URIS['get_balance']

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={}, authenticated=True)

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.Balance,
            elapsed_time=elapsed_time
        )

    def get_viewed_next_page(self,
                             bet_request_id: str,
                             sport_id: int = None
                             ):

        if sport_id:
            method_uri = self._METHOD_URIS['get_viewed_next_prev'].format(bet_request_id)
        else:
            method_uri = self._METHOD_URIS['get_viewed_next_prev_sport'].format(bet_request_id, sport_id)

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={})
        save_data_to_pickle_file('get_balance_response.pkl', response)
        save_json_to_file('get_balance_response.json', response_json)
        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.Balance,
            elapsed_time=elapsed_time
        )
