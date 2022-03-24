from betconnect import resources
from datetime import datetime
import pytest
from betconnect import exceptions
from uuid import UUID


class TestBettingResources:
    def test_active_bookmaker(self):
        active_bookmaker = resources.ActiveBookmaker(
            name="10Bet", bookmaker_id=6122, order=99, active=1
        )
        assert active_bookmaker.name == "10Bet"
        assert active_bookmaker.bookmaker_id == 6122
        assert active_bookmaker.order == 99
        assert active_bookmaker.active == 1

    def test_active_sport(self):
        active_sport = resources.ActiveSport(
            id=21,
            sport_id=14,
            name="Horse Racing",
            display_name="Horse Racing",
            slug="horse-racing",
            order=1,
            active=1,
            rate=2.0,
        )
        assert active_sport.id == 21
        assert active_sport.sport_id == 14
        assert active_sport.name == "Horse Racing"
        assert active_sport.display_name == "Horse Racing"
        assert active_sport.slug == "horse-racing"
        assert active_sport.order == 1
        assert active_sport.active == 1
        assert active_sport.rate == 2.0
        assert active_sport.bets_available is None

    def test_active_region(self):
        active_region = resources.ActiveRegion(
            name="England", region_id=3795032, iso="england", order=2
        )
        assert active_region.name == "England"
        assert active_region.region_id == 3795032
        assert active_region.iso == "england"
        assert active_region.order == 2

    def test_active_competition(self):
        active_competition = resources.ActiveCompetition(
            name="Southwell",
            display_name="Southwell",
            competition_id=840,
            active=1,
            order=9999,
        )
        assert active_competition.name == "Southwell"
        assert active_competition.display_name == "Southwell"
        assert active_competition.competition_id == 840
        assert active_competition.active == 1
        assert active_competition.order == 9999

    def test_active_market_type(self):
        active_market_type = resources.ActiveMarketType(
            market_type_id=6, name="WIN", active=1
        )
        assert active_market_type.market_type_id == 6
        assert active_market_type.name == "WIN"
        assert active_market_type.active == 1

    def test_active_market(self):
        active_market = resources.ActiveMarket(
            name="Race Winner",
            display_name="Race Winner",
            trading_status="Open",
            is_handicap="False",
            source_market_id="102347558",
            market_type_id=6,
            order=1,
            bet_types=["Win", "Each Way (1/4 odds 1-2-3)"],
        )
        assert active_market.name == "Race Winner"
        assert active_market.display_name == "Race Winner"
        assert active_market.trading_status == "Open"
        assert active_market.is_handicap == "False"
        assert active_market.source_market_id == "102347558"
        assert active_market.market_type_id == 6
        assert active_market.order == 1
        assert active_market.handicap is None
        assert active_market.bet_types == ["Win", "Each Way (1/4 odds 1-2-3)"]

    def test_balance(self):
        balance = resources.Balance(balance=1000)
        assert balance.balance == 1000
        assert balance.balance_uk_pounds == 10

    def test_prices_bookmaker(self):
        prices_bookmaker = resources.PricesBookmaker(id="123", name="Betfair")
        assert prices_bookmaker.id == "123"
        assert prices_bookmaker.name == "Betfair"

    def test_price(self):
        price = resources.Price(
            price="10",
            numerator="10",
            denominator="1",
            bookmakers=[{"id": "123", "name": "Betfair"}],
        )

        assert price.price == "10"
        assert price.numerator == "10"
        assert price.denominator == "1"
        assert price.bookmakers[0].id == "123"
        assert price.bookmakers[0].name == "Betfair"

    def test_active_selection(self):
        active_selection = resources.ActiveSelection(
            name="Metal Man",
            trading_status="NonRunner",
            selection_id="308685953",
            ut="2021-12-17 15:49:20.068318",
            competitor="1095697",
        )
        assert active_selection.name == "Metal Man"
        assert active_selection.trading_status == "NonRunner"
        assert active_selection.selection_id == "308685953"
        assert isinstance(active_selection.ut, datetime)
        assert active_selection.competitor == "1095697"

    def test_active_fixture(self):
        active_fixture = resources.ActiveFixture(
            fixture_id="8757184",
            display_name="Kempton Park",
            start_date="2021-12-17",
            time="16:15",
            each_way_active="1",
        )
        assert active_fixture.fixture_id == 8757184
        assert active_fixture.display_name == "Kempton Park"
        assert isinstance(active_fixture.start_date, datetime)
        assert active_fixture.time == "16:15"
        assert active_fixture.each_way_active == "1"

    def test_backers_stats(self):
        backers_stats = resources.BackersStats(
            strike_rate=100.0, roi=10.0, bet_requests="1234"
        )
        assert backers_stats.strike_rate == 100.0
        assert backers_stats.roi == 10.0
        assert backers_stats.bet_requests == "1234"

    def test_bet_request(self):
        bet_request = resources.BetRequest(
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
        assert bet_request.sport_name == "Horse Racing"
        assert bet_request.sport_id == "14"
        assert bet_request.competition_name == "Kempton Park"
        assert bet_request.region_name == "England"
        assert isinstance(bet_request.start_time_utc, datetime)
        assert bet_request.fixture_name == "Kempton Park"
        assert bet_request.market_name == "Race Winner"
        assert bet_request.selection_name == "Starter For Ten"
        assert isinstance(bet_request.price, resources.Price)
        assert bet_request.fixture_id == 8757185
        assert bet_request.market_type_id == 6
        assert bet_request.competitor == "1207634"
        assert bet_request.bet_request_id == UUID(
            "0f6efaa7-ffc3-45e9-8cf5-aa07e8ef5369"
        )
        assert bet_request.bet_type == "Win"
        assert bet_request.requested_stake == 5.0
        assert bet_request.liability == 11.25
        assert bet_request.locked_stake == 0.0
        assert isinstance(bet_request.backer_stats, resources.BackersStats)
        assert bet_request.others_viewing_bet == 0
        assert bet_request.lockable

    def test_bet_request_create(self):
        bet_request_create = resources.BetRequestCreate(
            bet_request_id="0f6efaa7-ffc3-45e9-8cf5-aa07e8ef5369",
            created="2021-12-17 16:20:49.113386",
            debit_stake=5,
            debit_commission=0.1,
        )
        assert bet_request_create.bet_request_id == UUID(
            "0f6efaa7-ffc3-45e9-8cf5-aa07e8ef5369"
        )
        assert isinstance(bet_request_create.created, datetime)
        assert bet_request_create.debit_stake == 5
        assert bet_request_create.debit_commission == 0.1

    def test_active_bet(self):
        active_bet = resources.ActiveBet(
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
        assert active_bet.bet_request_id == UUID("45e1a024-523a-4b25-a33d-4466775d0aac")
        assert active_bet.bet_type_name == "Win"
        assert active_bet.competition_name == "Hamilton Park"
        assert isinstance(active_bet.created_at, datetime)
        assert active_bet.fill_percentage == 0.0
        assert active_bet.fixture_id == 8248855
        assert active_bet.fixture_name == "Hamilton Park"
        assert isinstance(active_bet.fixture_start_date, datetime)
        assert active_bet.market_name == "Race Winner"
        assert active_bet.matched_stake == 0.0
        assert active_bet.price == 1.16
        assert active_bet.price_denominator == 25
        assert active_bet.price_numerator == 4
        assert active_bet.selection_name == "Misty Ayr"
        assert active_bet.sport_name == "Horse Racing"
        assert active_bet.stake == 10.0
        assert active_bet.status_name == "Active"

    def test_bet_request_match(self):
        bet_request_match = resources.BetRequestMatch(
            matched=True,
            available=True,
            bet_request_id="45e1a024-523a-4b25-a33d-4466775d0aac",
            bet_id="124",
            bet_status="Active",
            amount_matched=10.0,
        )
        assert bet_request_match.matched
        assert bet_request_match.available
        assert bet_request_match.bet_request_id == UUID(
            "45e1a024-523a-4b25-a33d-4466775d0aac"
        )
        assert bet_request_match.bet_id == "124"
        assert bet_request_match.bet_status == "Active"
        assert bet_request_match.amount_matched == 10.0

    def test_bet_history(self):
        bet_history = resources.BetHistory(
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

        assert bet_history.bet_request_id == UUID(
            "0f6efaa7-ffc3-45e9-8cf5-aa07e8ef5369"
        )
        assert bet_history.bet_request_status == "Active"
        assert bet_history.bet_type_name == "Win"
        assert bet_history.competition_name == "Kempton Park"
        assert bet_history.fill_percentage == 0.0
        assert bet_history.fixture_name == "Kempton Park"
        assert isinstance(bet_history.fixture_start_date, datetime)
        assert bet_history.market_name == "Race Winner"
        assert bet_history.matched_stake == 0.0
        assert bet_history.price == 3.25
        assert bet_history.price_denominator == 4
        assert bet_history.price_numerator == 9
        assert bet_history.region_iso == "england"
        assert bet_history.region_name == "England"
        assert bet_history.selection_name == "Starter For Ten"
        assert bet_history.sport_name == "Horse Racing"
        assert bet_history.stake == 5.0

    def test_active_bets_request(self):
        active_bets_requests = resources.ActiveBetRequests(
            bets=[], bets_active=10, last_page=10, total_bets=20
        )

        assert active_bets_requests.bets == []
        assert active_bets_requests.bets_active == 10
        assert active_bets_requests.last_page == 10
        assert active_bets_requests.total_bets == 20

    def test_bet_history_request(self):
        bet_history_request = resources.BetHistoryRequest(
            bets=[], last_page=10, total_bets=20
        )
        assert bet_history_request.bets == []
        assert bet_history_request.last_page == 10
        assert bet_history_request.total_bets == 20

    def test_selections_for_market(self):
        selections_for_market = resources.SelectionsForMarket(
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
        assert selections_for_market.source_fixture_id == "8757185"
        assert selections_for_market.source_market_id == "102347567"
        assert selections_for_market.source_market_type_id == "6"
        assert selections_for_market.trading_status == "Trading"
        assert selections_for_market.name == "Starter For Ten"
        assert selections_for_market.competitor_id == "1207634"
        assert isinstance(selections_for_market.ut, datetime)
        assert selections_for_market.order == 0
        assert selections_for_market.max_price == 3.25
        for p in selections_for_market.prices:
            assert isinstance(p, resources.Price)

    def test_viewed(self):
        viewed = resources.Viewed(
            prev="0f6efaa7-ffc3-45e9-8cf5-aa07e8ef5369",
            next="0f6efaa7-ffc3-45e9-8cf5-aa07e8ef5589",
        )

        assert viewed.prev == UUID("0f6efaa7-ffc3-45e9-8cf5-aa07e8ef5369")
        assert viewed.next == UUID("0f6efaa7-ffc3-45e9-8cf5-aa07e8ef5589")

    def test_bet_request_match_more(self):
        bet_request_match_more = resources.BetRequestMatchMore(
            matched=True,
            available=True,
            viewed={
                "prev": "0f6efaa7-ffc3-45e9-8cf5-aa07e8ef5369",
                "next": "0f6efaa7-ffc3-45e9-8cf5-aa07e8ef5589",
            },
        )
        assert bet_request_match_more.matched
        assert bet_request_match_more.available
        assert isinstance(bet_request_match_more, resources.BetRequestMatchMore)

    def test_bet_request_stop(self):
        bet_request_stop = resources.BetRequestStop(pending=False)
        assert bet_request_stop.pending is False

    def test_my_active_bet(self):
        my_active_bet = resources.MyActiveBet(
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
        assert isinstance(my_active_bet.actioned_at, datetime)
        assert my_active_bet.adjustment is None
        assert my_active_bet.adjustment_type is None
        assert my_active_bet.bet_created == 1
        assert my_active_bet.bet_request_id == UUID(
            "a575ba8b-2264-4f14-8f59-9eeb805e5a37"
        )
        assert my_active_bet.bet_request_status_id == 1
        assert my_active_bet.bet_request_user_id == UUID(
            "a6a1eb91-6217-4e0c-b759-fbcaa2b7a8ac"
        )
        assert my_active_bet.bet_type_name == "Win"
        assert my_active_bet.competition_name == "Hamilton Park"
        assert my_active_bet.count_in_place is None
        assert my_active_bet.customer_order_ref is None
        assert my_active_bet.customer_strategy_ref is None
        assert my_active_bet.each_way_factor is None
        assert my_active_bet.fill_percentage == 0.0
        assert my_active_bet.fixture_name == "Hamilton Park"
        assert isinstance(my_active_bet.fixture_start_date, datetime)
        assert my_active_bet.handicap is None
        assert my_active_bet.market_name == "Race Winner"
        assert my_active_bet.matched_stake == 0
        assert isinstance(my_active_bet.price, resources.Price)
        assert my_active_bet.profit == 0
        assert my_active_bet.profit_loss is None
        assert my_active_bet.region_iso == "scotland"
        assert my_active_bet.region_name == "Scotland"
        assert my_active_bet.selection_name == "Misty Ayr"
        assert my_active_bet.sport_external_id == 14
        assert my_active_bet.sport_name == "Horse Racing"
        assert my_active_bet.sport_slug == "horse-racing"
        assert my_active_bet.stake == 1000
        assert my_active_bet.status_name == "Active"
        assert my_active_bet.status_slug == "active"
        assert my_active_bet.sub_account_id is None

        # Each Way Bet
        my_active_bet = resources.MyActiveBet(
            actioned_at="2022-01-16 11:43:16",
            bet_created=1,
            bet_request_id="9983e005-8301-4ef4-bbe9-ce441a3f491b",
            bet_request_status_id=1,
            bet_request_user_id="91358194-70a7-4d51-bb40-3f3ffeb386d6",
            bet_type_name="Each Way (1/5 odds 1-2-3)",
            competition_name="Southwell",
            count_in_place=None,
            customer_order_ref=None,
            customer_strategy_ref=None,
            each_way_factor=5,
            fill_percentage=0,
            fixture_name="Southwell",
            fixture_startdate="2022-01-16 16:00:00",
            handicap=None,
            market_name="Race Winner",
            matched_stake=0,
            price={"decimal": "6.0", "fraction": {"denominator": 1, "numerator": 5}},
            profit=0,
            region_iso="england",
            region_name="England",
            selection_name="Asadjumeirah",
            sport_external_id=14,
            sport_name="Horse Racing",
            sport_slug="horse-racing",
            stake=500,
            status_name="Active",
            status_slug="active",
            sub_account_id=None,
        )
        assert my_active_bet.bet_type_name == "Each Way (1/5 odds 1-2-3)"
        assert my_active_bet.each_way_factor == 5

        # Partially matched handicap bet
        my_active_bet = resources.MyActiveBet(
            actioned_at="2022-01-17 15:39:30",
            bet_created=1,
            bet_request_id="9613dbd6-fe44-437f-a64e-04b2f05701e9",
            bet_request_status_id=1,
            bet_request_user_id="91358194-70a7-4d51-bb40-3f3ffeb386d6",
            bet_type_name=None,
            competition_name="NFL",
            count_in_place=None,
            customer_order_ref=None,
            customer_strategy_ref=None,
            each_way_factor=None,
            fill_percentage=40,
            fixture_name="Los Angeles Rams v Arizona Cardinals",
            fixture_startdate="2022-01-18 01:15:00",
            handicap="-3.5",
            market_name="Point Spread",
            matched_stake=200,
            price={"decimal": "1.333", "fraction": {"denominator": 3, "numerator": 1}},
            profit=66,
            region_iso="us",
            region_name="United States of America",
            selection_name="Asadjumeirah",
            sport_external_id=17,
            sport_name="American Football",
            sport_slug="american-football",
            stake=500,
            status_name="Active",
            status_slug="active",
            sub_account_id=None,
        )
        assert my_active_bet.bet_type_name is None
        assert my_active_bet.each_way_factor is None
        assert my_active_bet.fill_percentage == 40
        assert my_active_bet.handicap == "-3.5"
        assert my_active_bet.matched_stake == 200
        assert my_active_bet.profit == 66

    def test_customer_order_ref(self):
        customer_order_ref_gen = resources.CustomerOrderRef.generate_random_order_ref()
        customer_order_ref = resources.CustomerOrderRef(
            customer_order_ref=customer_order_ref_gen
        )
        assert customer_order_ref.customer_order_ref == customer_order_ref_gen
        assert str(customer_order_ref) == customer_order_ref_gen

        with pytest.raises(exceptions.BetRequestInvalidCustomerOrderRefFormatException):
            resources.CustomerOrderRef(
                customer_order_ref="111111111111111111111111111111111111111111111111111"
            )

        # test customer order ref generate random UUID
        assert isinstance(
            UUID(resources.CustomerOrderRef.generate_random_order_ref()), UUID
        )

        customer_order_ref = resources.CustomerOrderRef.create_customer_order_ref(
            customer_order_ref="12344"
        )
        assert customer_order_ref.customer_order_ref == "12344"

        with pytest.raises(exceptions.BetRequestInvalidCustomerOrderRefFormatException):
            resources.CustomerOrderRef.create_customer_order_ref(customer_order_ref="")

        with pytest.raises(exceptions.BetRequestInvalidCustomerOrderRefFormatException):
            resources.CustomerOrderRef.create_customer_order_ref(
                customer_order_ref="11111111111111111111111111111111111111111"
            )

    def test_customer_strategy_ref(self):
        customer_strategy_ref_value = "best_strategy"
        customer_strategy_ref = resources.CustomerStrategyRef(
            customer_strategy_ref=customer_strategy_ref_value
        )
        assert (
            customer_strategy_ref.customer_strategy_ref == customer_strategy_ref_value
        )
        assert str(customer_strategy_ref) == customer_strategy_ref_value

        with pytest.raises(
            exceptions.BetRequestInvalidCustomerStrategyRefFormatException
        ):
            resources.CustomerStrategyRef(
                customer_strategy_ref="111111111111111111111111111111111111111111111111111"
            )

        customer_stratey_ref = (
            resources.CustomerStrategyRef.create_customer_strategy_ref("1234")
        )
        assert customer_stratey_ref.customer_strategy_ref == "1234"
        customer_stratey_ref = (
            resources.CustomerStrategyRef.create_customer_strategy_ref("123 4")
        )
        assert customer_stratey_ref.customer_strategy_ref == "1234"

        with pytest.raises(
            exceptions.BetRequestInvalidCustomerStrategyRefFormatException
        ):
            resources.CustomerStrategyRef.create_customer_strategy_ref(
                "12343333333333333333333333"
            )

        with pytest.raises(
            exceptions.BetRequestInvalidCustomerStrategyRefFormatException
        ):
            resources.CustomerStrategyRef.create_customer_strategy_ref("")

    def test_line_markets_selections_for_market(self):
        line_markets = resources.LineMarketsSelectionsForMarket(
            name="Over/Under (1.5)",
            display_name="Over/Under (1.5)",
            handicap="1.5",
            line_data=[
                {
                    "source_fixture_id": "8172709",
                    "source_market_id": "102340516",
                    "source_market_type_id": "259",
                    "source_selection_id": "308656048",
                    "trading_status": "Trading",
                    "name": "Over 1.5",
                    "outcome": "Over",
                    "ut": "2021-12-19 04:56:46.590564",
                    "handicap": 1.5,
                    "order": 1,
                    "prices": [
                        {
                            "price": "6.00",
                            "numerator": "5",
                            "denominator": "1",
                            "bookmakers": [
                                {"id": "6006", "name": "Coral"},
                                {"id": "17", "name": "Ladbrokes"},
                            ],
                        }
                    ],
                }
            ],
        )
        assert line_markets.name == "Over/Under (1.5)"
        assert line_markets.display_name == "Over/Under (1.5)"
        assert line_markets.handicap == "1.5"
        assert isinstance(line_markets.line_data, list)
        for market in line_markets.line_data:
            assert isinstance(market, resources.SelectionsForMarket)
