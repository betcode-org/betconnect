from typing import Union, List
import requests
from betconnect import enums
from betconnect import resources
from .baseendpoint import BaseEndpoint
import logging
from betconnect import exceptions
from uuid import UUID

logger = logging.getLogger(__name__)


class Betting(BaseEndpoint):
    def active_bookmakers(self) -> List[resources.ActiveBookmaker]:
        """
        Returns a list of active sports
        :return: List of ActiveBookmaker
        """

        (response, response_json, elapsed_time) = self._request(
            method_uri=f"{self.api_version}/active_bookmakers", authenticated=True
        )

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveBookmaker,
            elapsed_time=elapsed_time,
        )

    def active_sports(self, with_bets: bool = False) -> List[resources.ActiveSport]:
        """
        Gets a list of active sports
        :param with_bets: boolean value (True, False). Returns the number of active bet_request available for each sport
        :return: List of ActiveSport
        """

        (response, response_json, elapsed_time) = self._request(
            method_uri=f"{self.api_version}/active_sports{'/True' if with_bets else ''}"
        )

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveSport,
            elapsed_time=elapsed_time,
        )

    def active_regions(self, sport_id: int) -> List[resources.ActiveRegion]:
        """
        Gets the active regions for a sport
        :param sport_id: The sport ID
        :return: List of ActiveRegion
        """

        (response, response_json, elapsed_time) = self._request(
            method_uri=f"{self.api_version}/active_regions/{sport_id}"
        )

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveRegion,
            elapsed_time=elapsed_time,
        )

    def active_competitions(
        self, sport_id: int, region_id: int
    ) -> List[resources.ActiveCompetition]:
        """
        Returns a list of active competitions for a given sport id and region id
        :param int sport_id: The sport ID
        :param int region_id: The region ID
        :return: List of ActiveCompetition
        """

        (response, response_json, elapsed_time) = self._request(
            method_uri=f"{self.api_version}/active_competitions/{sport_id}/{region_id}"
        )

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveCompetition,
            elapsed_time=elapsed_time,
        )

    def active_fixtures(
        self, sport_id: int, region_id: int = None, competition_id: int = None
    ) -> List[resources.ActiveFixture]:
        """
        Gets active fixtures for a sport, region and competition
        :param sport_id: The sport ID
        :param region_id: The region ID
        :param competition_id: The competition ID
        :return: List of ActiveFixture
        """
        if competition_id:
            assert region_id is not None

        (response, response_json, elapsed_time) = self._request(
            method_uri=f"{self.api_version}/active_fixtures/{sport_id}/{region_id if region_id else ''}{f'/{competition_id}' if competition_id is not None else ''}"
        )

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveFixture,
            elapsed_time=elapsed_time,
        )

    def active_market_types(self, sport_id: int) -> List[resources.ActiveMarketType]:
        """
        Gets the active market type for a sport
        :param sport_id: The sport ID
        :return: List of ActiveMarketType
        """

        (response, response_json, elapsed_time) = self._request(
            method_uri=f"{self.api_version}/active_market_types/{sport_id}"
        )

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveMarketType,
            elapsed_time=elapsed_time,
        )

    def active_markets(
        self, fixture_id: int, grouped: bool = False
    ) -> List[resources.ActiveMarket]:
        """
        Gets a list of active markets for the fixture
        :param fixture_id: The fixture ID
        :param grouped: boolean value to determine whether the response should be grouped
        :return: List of ActiveMarket
        """

        (response, response_json, elapsed_time) = self._request(
            method_uri=f"{self.api_version}/active_markets/{fixture_id}{'/grouped' if grouped else ''}"
        )

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveMarket,
            elapsed_time=elapsed_time,
        )

    def active_selections(
        self, fixture_id: int, market_type_id: int, handicap: str = None
    ) -> List[resources.ActiveSelection]:
        """
        Gets active selections for a given fixture and market type
        :param fixture_id: The fixture ID
        :param market_type_id: The market type ID
        :param handicap: string handicap value. example '4.5'
        :return: List of ActiveSelection
        """
        (response, response_json, elapsed_time) = self._request(
            method_uri=f"{self.api_version}/active_selections/{fixture_id}/{market_type_id}{f'/{handicap}' if handicap is not None else ''}"
        )

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveSelection,
            elapsed_time=elapsed_time,
        )

    def bet_request_create(
        self, request_filter: resources.CreateBetRequestFilter
    ) -> Union[resources.BaseRequestException, resources.BetRequestCreate]:
        """
        Creates a bet (Authenticated)
        :param request_filter: The bet create filter
        :return: a successful BetRequestCreate resource or an BaseRequestException when BetConnect detects an issue.
        """

        (response, response_json, elapsed_time) = self._post(
            method_uri=f"{self.api_version}/bet_request_create",
            data=request_filter.generate_request_data(exclude_none=True),
        )

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.BetRequestCreate,
            elapsed_time=elapsed_time,
        )

    def bet_request_get(
        self, request_filter: resources.GetBetRequestFilter
    ) -> Union[resources.BaseRequestException, resources.BetRequest]:
        """
        Gets a bet request for the given filter.

        This is other users bet requests (please use my_bets to get your own).

        :param request_filter: A bet request filter, either enter a bet request id or other filter values
        :return: A bet BetRequest resource or an BaseRequestException when BetConnect detects an issue.
        """

        if request_filter.bet_request_id:
            (response, response_json, elapsed_time) = self._post(
                method_uri=f"{self.api_version}/bet_request_get",
                data=request_filter.generate_request_data(
                    exclude={
                        "sport_id",
                        "bookmakers",
                        "min_odds",
                        "max_odds",
                        "accept_each_way",
                    }
                ),
            )
        else:
            if request_filter.accept_each_way:
                (response, response_json, elapsed_time) = self._post(
                    method_uri=f"{self.api_version}/bet_request_get",
                    data=request_filter.generate_request_data(
                        exclude={"bet_request_id", "accept_each_way"}
                    ),
                )
            else:
                (response, response_json, elapsed_time) = self._post(
                    method_uri=f"{self.api_version}/bet_request_get",
                    data=request_filter.generate_request_data(
                        exclude={"bet_request_id"}
                    ),
                )

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.BetRequest,
            elapsed_time=elapsed_time,
        )

    def _is_line_market(self, response: requests.Response, response_json: dict) -> bool:
        """
        Function to check whether the market is a line market returned from BetConnect
        :param response: A response resource return from BetConnect
        :param response_json: The response json containing thee data
        :return: A boolean {True, False} as whether it is a Line market
        """
        if self.check_status_code(response):
            if "data" in response_json:
                data = response_json["data"]

                if isinstance(data, list):
                    if data:
                        return True if "line" in data[0] else False

        return False

    def selections_for_market(
        self, fixture_id: int, market_type_id: int, top_price_only: bool = False
    ) -> Union[resources.BaseRequestException, List[resources.SelectionsForMarket]]:
        """
        Returns the selection for a given market with their prices. This method is the fastest way to get selections
        and prices in few requests.
        :param fixture_id: The fixture ID
        :param market_type_id: the market type ID
        :param top_price_only: a bool value that represents whether to only return the top value
        :return: A List of SelectionsForMarket resources or an BaseRequestException when BetConnect detects an issue.
        """
        (response, response_json, elapsed_time) = self._request(
            method_uri=f"{self.api_version}/selections_for_market/{fixture_id}/{market_type_id}/{f'True'if top_price_only else 'False'}"
        )
        # Check is response a line market
        if self._is_line_market(response=response, response_json=response_json):
            return self.process_response(
                response=response,
                response_json=response_json,
                resource=resources.LineMarketsSelectionsForMarket,
                elapsed_time=elapsed_time,
            )
        else:
            return self.process_response(
                response=response,
                response_json=response_json,
                resource=resources.SelectionsForMarket,
                elapsed_time=elapsed_time,
            )

    def bet_request_match(
        self, bet_request_id: UUID, accepted_stake: int
    ) -> Union[resources.BaseRequestException, resources.BetRequestMatch]:
        """
        A request to match for part or all of an active bet request.
        :param bet_request_id: The bet request ID
        :param accepted_stake: the target stake you would like to match
        :return: A BetRequestMatch resource or an BaseRequestException when BetConnect detects an issue.
        """
        self.check_bet_request_id(bet_request_id=bet_request_id)

        (response, response_json, elapsed_time) = self._patch(
            method_uri=f"{self.api_version}/bet_request_match",
            data={
                "bet_request_id": str(bet_request_id),
                "accepted_stake": accepted_stake,
            },
        )

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.BetRequestMatch,
            elapsed_time=elapsed_time,
        )

    def bet_request_match_more(
        self, bet_request_id: UUID, requested_stake: float
    ) -> Union[resources.BetRequestMatchMore, resources.BaseRequestException]:
        """
        Allows you to match a bet request fully (up to the maximum liability allowed for a single bet)
        and request more of that bet until no liability is left.
        :param bet_request_id: The bet request ID
        :param requested_stake: The requested stake
        :return: A BetRequestMatchMore resource or an BaseRequestException when BetConnect detects an issue.
        """
        self.check_bet_request_id(bet_request_id=bet_request_id)

        (response, response_json, elapsed_time) = self._patch(
            method_uri=f"{self.api_version}/bet_request_match_more",
            data={
                "bet_request_id": str(bet_request_id),
                "requested_stake": int(requested_stake),
            },
        )

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.BetRequestMatchMore,
            elapsed_time=elapsed_time,
        )

    def bet_request_stop(
        self, bet_request_id: UUID, stop_bet_reason: str = ""
    ) -> Union[resources.BetRequestStop, resources.BaseRequestException]:
        """
        Stops an active bet request
        :param bet_request_id: The bet request ID
        :param stop_bet_reason: optional reason (i.e. 'no longer value')
        :return: A BetRequestStop resource or an BaseRequestException when BetConnect detects an issue.
        """
        self.check_bet_request_id(bet_request_id=bet_request_id)

        (response, response_json, elapsed_time) = self._post(
            method_uri=f"{self.api_version}/bet_request_stop",
            data={
                "bet_request_id": str(bet_request_id),
                "stop_bet_reason": stop_bet_reason,
            },
            authenticated=True,
        )

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.BetRequestStop,
            elapsed_time=elapsed_time,
        )

    def prices(
        self,
        fixture_id: int,
        market_type_id: int,
        competitor: str,
        handicap: str = None,
    ) -> List[resources.Price]:
        """
        Returns a set of prices for a given fixture, market type and competition.
        :param fixture_id: The fixture ID
        :param market_type_id: the market type ID
        :param competitor: the compeitor string
        :param handicap: handicap string value (If the market type is a handicap market a handicap is required)
        :return: A List of Price resources
        """

        (response, response_json, elapsed_time) = self._request(
            method_uri=f"{self.api_version}/prices/{fixture_id}/{market_type_id}/{competitor.lower()}{f'/{handicap}' if handicap is not None else ''}"
        )

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.Price,
            elapsed_time=elapsed_time,
        )

    def bet_history(
        self,
        status: enums.BetStatus,
        side: enums.BetSide,
        limit: int = None,
        page: int = None,
    ) -> Union[resources.BaseRequestException, resources.BetHistoryRequest]:
        """
        Returns bet history with paging options
        :param status: The status of the bet
        :param side: BetSide enum - either back or lay
        :param limit: Limit the number of bets returned
        :param page: The page number to start from
        :return: A BetHistoryRequest resource or an BaseRequestException when BetConnect detects an issue.
        """
        if (page is not None) or (limit is not None):
            limit = (
                max(limit, self.client.minimum_limit_value)
                if limit
                else self.client.minimum_limit_value
            )
            page = (
                max(page, self.client.page_start_value)
                if page
                else self.client.page_start_value
            )

        (response, response_json, elapsed_time) = self._request(
            method_uri=f"{self.api_version}/bet_history/{str(side.value)}/{self.client.username}/{str(status.value)}{f'/{limit}/{page}'if page is not None else ''}",
            authenticated=True,
        )

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.BetHistoryRequest,
            elapsed_time=elapsed_time,
        )

    def get_viewed_next_page(
        self, bet_request_id: UUID, sport_id: int = None
    ) -> Union[resources.Viewed, resources.BaseRequestException]:
        """
        Returns the next bet request available to be viewed. (mprefered approach is to use bet_request_get
        with a wide filter instead)
        :param bet_request_id: The bet request ID
        :param sport_id: the sport ID
        :return: A Viewed resource or an BaseRequestException when BetConnect detects an issue.
        """
        self.check_bet_request_id(bet_request_id=bet_request_id)

        (response, response_json, elapsed_time) = self._request(
            method_uri=f"{self.api_version}/get_viewed_next_prev/{str(bet_request_id)}{f'/{sport_id}'if sport_id is not None else ''}"
        )

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.Viewed,
            elapsed_time=elapsed_time,
        )

    def my_bets(
        self,
        side: enums.BetSide,
        status: enums.BetRequestStatus,
        user_id: str = None,
        limit: int = None,
        page: int = None,
        get_all: str = None,
        customer_strategy_ref: str = None,
    ) -> Union[
        resources.MyBetsBetRequests,
        resources.MyBetsBets,
        resources.BaseRequestException,
    ]:
        """
        Returns a list of MyBets allowing for per strategy recall of bets
        :param side: the side of the bet, enum value BACK and LAY
        :param status: The bet request status, enum values ACTIVE and SETTLED
        :param user_id: The user_id, optional will try to get this from the user preference which is called on login.
        :param limit: Limit the number of bets coming back.
        :param page: T page number for (pagination)
        :param get_all: string value to return all values with the above limit and page
        :param customer_strategy_ref: The customer strategy ref which has been attached to any bet requests
        :return: A MyBetsBetRequests resource or an BaseRequestException when BetConnect detects an issue.
        """
        if (page is not None) or (limit is not None):
            limit = (
                max(limit, self.client.minimum_limit_value)
                if limit
                else self.client.minimum_limit_value
            )
            page = (
                max(page, self.client.page_start_value)
                if page
                else self.client.page_start_value
            )

        if not user_id:
            if self.client.user_preferences:
                user_id = self.client.user_preferences.user_id

        if get_all:
            (response, response_json, elapsed_time) = self._request(
                method_uri=f"{self.api_version}/my_bets/{str(side.value)}/{user_id}/{str(status.value)}{f'/{limit}/{page}'if page is not None else ''}/{get_all}{f'/{customer_strategy_ref}'if customer_strategy_ref is not None else ''}",
                authenticated=True,
            )
        else:
            if customer_strategy_ref:
                (response, response_json, elapsed_time) = self._request(
                    method_uri=f"{self.api_version}/my_bets/{str(side.value)}/{user_id}/{str(status.value)}{f'/{limit}/{page}'if page is not None else ''}/get_only/{customer_strategy_ref}",
                    authenticated=True,
                )
            else:
                (response, response_json, elapsed_time) = self._request(
                    method_uri=f"{self.api_version}/my_bets/{str(side.value)}/{user_id}/{str(status.value)}{f'/{limit}/{page}'if page is not None else ''}",
                    authenticated=True,
                )

        if str(side.value).upper() == "BACK":
            return self.process_response(
                response=response,
                response_json=response_json,
                resource=resources.MyBetsBetRequests,
                elapsed_time=elapsed_time,
            )
        else:
            return self.process_response(
                response=response,
                response_json=response_json,
                resource=resources.MyBetsBets,
                elapsed_time=elapsed_time,
            )

    def lock_bet(self, bet_request_id: UUID, amount: int, seconds: int):
        """
        Not Yet Implemented: Locks a bet for a set amount of seconds for a set amount
        :param bet_request_id: The bet request ID
        :param amount: the amount
        :param seconds: the seconds to lock the bet
        :return: A Lock bet resource
        """
        raise NotImplementedError()
