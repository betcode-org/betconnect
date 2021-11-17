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
        'prices': 'api/v2/prices/{}/{}/{}',
        'prices_handicap': 'api/v2/prices/{}/{}/{}/{}',
        'get_balance': '/api/v2/get_balance',
        'get_viewed_next_prev': '/api/v2/get_viewed_next_prev/{}',
        'get_viewed_next_prev_sport': '/api/v2/get_viewed_next_prev/{}/{}',
        'selections_for_market': 'api/v2/selections_for_market/{}/{}',
        'selections_for_market_top_price': 'api/v2/selections_for_market/{}/{}/{}'
    }

    def active_bookmakers(self) -> List[resources.ActiveBookmaker]:
        """
        Returns a list of active sports
        :return: List of ActiveBookmaker
        """

        method_uri = self._METHOD_URIS['active_bookmakers']

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={})

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveBookmaker,
            elapsed_time=elapsed_time
        )

    def active_sports(self, with_bets: bool = None) -> List[resources.ActiveSport]:
        """
        Gets a list of active sports
        :param with_bets: boolean value (True, False)
        :return: List of active sports
        """
        if with_bets:
            method_uri = self._METHOD_URIS['active_sports_with_bets']
        else:
            method_uri = self._METHOD_URIS['active_sports']

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={})

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveSport,
            elapsed_time=elapsed_time
        )

    def active_regions(self,
                       sport_id: int) -> List[resources.ActiveRegion]:
        """
        Gets the active regions for a sport
        :param sport_id: The sport ID
        :return: List of active regions
        """

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
                            ) -> List[resources.ActiveCompetition]:
        """
        Returns a list of active competitions for a given sport id and region id
        :param sport_id: The sport ID
        @:param region_id: The region ID
        :return: List of ActiveBookmaker
        """

        method_uri = self._METHOD_URIS['active_competitions'].format(sport_id, region_id)

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={})

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveCompetition,
            elapsed_time=elapsed_time
        )

    def active_fixtures(self,
                        sport_id: int,
                        region_id: int = None,
                        competition_id: int = None
                        ) -> List[resources.ActiveFixture]:
        """
        Gets active fixtures for a sport, region and competition
        :param sport_id: The sport ID
        :param region_id: The region ID
        :param competition_id: The competition ID
        :return: List of active fixtures
        """

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
            resource=resources.ActiveFixture,
            elapsed_time=elapsed_time
        )

    def active_market_types(self, sport_id: int) -> List[resources.ActiveMarketType]:
        """
        Gets the active market type for a sport
        :param sport_id: The sport ID
        :return: List of active market types
        """
        method_uri = self._METHOD_URIS['active_market_types'].format(sport_id)

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={})

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveMarketType,
            elapsed_time=elapsed_time
        )

    def active_markets(self, fixture_id: int, grouped: bool = None) -> List[resources.ActiveMarket]:
        """
        Gets a list of active markets for the fixture
        :param fixture_id: The fixture ID
        :param grouped: boolean value to determine whether the response should be grouped
        :return: List of active markets
        """
        if grouped:
            method_uri = self._METHOD_URIS['active_markets_grouped'].format(fixture_id)
        else:
            method_uri = self._METHOD_URIS['active_markets'].format(fixture_id)

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={})

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveMarket,
            elapsed_time=elapsed_time
        )

    def active_selections(self, fixture_id: int, market_type_id: int, handicap: bool = None) -> List[
        resources.ActiveSelection]:
        """
        Gets active selections for a given fixture and market type
        :param fixture_id: The fixture ID
        :param market_type_id: The market type ID
        :param handicap: boolean handicap value (True, False)
        :return: List of active selections
        """
        if handicap:
            method_uri = self._METHOD_URIS['active_selections_handicap'].format(fixture_id, market_type_id, handicap)
        else:
            method_uri = self._METHOD_URIS['active_selections'].format(fixture_id, market_type_id)

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={})

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveSelection,
            elapsed_time=elapsed_time
        )

    def bet_request_create(self,
                           filter: resources.CreateBetRequestFilter
                           ) -> Union[resources.BaseRequestException, resources.BetRequestCreate]:
        """
        Creates a bet (Authenticated)
        :param filter: The bet create filter
        :return: a successful bet create response or an exception
        """

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
                        ) -> Union[resources.BaseRequestException, resources.BetRequest]:
        """
        Gets a bet request for the given filter
        :param filter: A bet request filter, either enter a bet request id or other filter values
        :return: A bet request resource or a request exception resource
        """

        method_uri = self._METHOD_URIS['bet_request_get']

        if filter.bet_request_id:
            (response, response_json, elapsed_time) = self.post(
                method_uri=method_uri,
                data=filter.dict(exclude={'sport_id', 'bookmakers', 'min_odds', 'max_odds', 'accept_each_way'})
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
                              ) -> Union[resources.BaseRequestException,List[resources.SelectionsForMarket]]:
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
                          ) -> Union[resources.BaseRequestException, resources.BetRequestMatch]:
        """
        A request to match for part or all of an active bet request.
        :param bet_request_id: The bet request ID
        :param accepted_stake: the target stake you would like to match
        :return: A bet request match resource or a request exception resource
        """

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
                               ) -> Union[resources.BetRequestMatchMore, resources.BaseRequestException]:
        """
        Allows you to match a bet request fully (up to the maximum liability allowed for a single bet) and request more of that bet until no liability is left.
        :param bet_request_id: The bet request ID
        :param requested_stake: The requested stake
        :return: A bet request match more resource or a request exception resource
        """

        method_uri = self._METHOD_URIS['bet_request_match_more']

        (response, response_json, elapsed_time) = self.patch(method_uri=method_uri, data={
            "bet_request_id": bet_request_id,
            "requested_stake": int(requested_stake)
        })

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.BetRequestMatchMore,
            elapsed_time=elapsed_time
        )

    def bet_request_stop(self,
                         bet_request_id: str,
                         stop_bet_reason: str = ''
                         ) -> resources.ResponseMessage:
        """
        Stops an active bet bet request
        :param bet_request_id: The bet request ID
        :param stop_bet_reason: optional reason
        :return: A bet request stop response message
        """

        method_uri = self._METHOD_URIS['bet_request_stop']

        (response, response_json, elapsed_time) = self.post(method_uri=method_uri, data={
            'bet_request_id': bet_request_id,
            'stop_bet_reason': stop_bet_reason
        })

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ResponseMessage,
            elapsed_time=elapsed_time
        )

    def get_active_bet_requests(self,
                                limit: int = None,
                                page: int = None
                                ) -> Union[resources.ActiveBetsRequest, resources.BaseRequestException]:
        """
        Gets active bet requests, taking into account pagination
        :param limit: Limit the number of active bets returned
        :param page: The page starting number
        :return: An active bet request resource or request exception resource
        """
        if limit and page:
            method_uri = self._METHOD_URIS['get_active_bet_requests_limit_page'].format(limit, page)
        else:
            method_uri = self._METHOD_URIS['get_active_bet_requests']

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={}, authenticated=True)

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveBetsRequest,
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
        """
        Returns bet history with paging options
        :param username: Your username
        :param status: The status of the bet
        :param limit: Limit the number of bets returned
        :param page: The page number to start from
        :return: return a bet history resource
        """

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

    def get_balance(self)->Union[resources.Balance, resources.BaseRequestException]:
        """
        Gets the account balance
        :return: The balance resource or the request exception resaource
        """

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
                             )->Union[resources.Viewed, resources.BaseRequestException]:

        if sport_id is None:
            method_uri = self._METHOD_URIS['get_viewed_next_prev'].format(bet_request_id)
        else:
            method_uri = self._METHOD_URIS['get_viewed_next_prev_sport'].format(bet_request_id, sport_id)

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={})

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.Viewed,
            elapsed_time=elapsed_time
        )
