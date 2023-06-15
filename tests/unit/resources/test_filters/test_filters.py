from betconnect import resources
import pytest
from betconnect import exceptions


class TestFilters:
    def test_filter(self):
        request_filter = resources.Filter()
        assert isinstance(request_filter, resources.Filter)

    # noinspection SpellCheckingInspection
    def test_get_bet_request_filter(self):
        request_filter = resources.GetBetRequestFilter(sport_id=1)
        assert request_filter.sport_id == 1
        assert request_filter.bookmakers == []
        assert request_filter.horse_racing_regions == []
        assert request_filter.min_odds == 1.01
        assert request_filter.max_odds == 1000
        assert request_filter.accept_each_way == True
        assert request_filter.bet_request_id is None

        # test length == 36
        with pytest.raises(exceptions.BetRequestIDFormatException):
            resources.GetBetRequestFilter(bet_request_id="invalid bet request length")

        # test uuid format
        with pytest.raises(exceptions.BetRequestIDFormatException):
            resources.GetBetRequestFilter(
                bet_request_id="c9bf9e575168554c895bafb5ff5af830be8a"
            )
        # test min odds validation
        with pytest.raises(exceptions.MinOddException):
            resources.GetBetRequestFilter(min_odds=1)

    def test_create_bet_request_by_selection_filter(self):
        request_filter = resources.CreateBetRequestBySelectionFilter(
            selection_id=123,
            price=10,
            stake=50,
            bet_type="WIN",
        )
        assert request_filter.selection_id == 123
        assert request_filter.price == 10
        assert request_filter.stake == 50
        assert request_filter.bet_type == "WIN"
        assert request_filter.handicap is None
        assert request_filter.customer_strategy_ref is None
        assert request_filter.customer_order_ref is None

        # test min stake validation
        with pytest.raises(exceptions.BetRequestIDStakeSizeException):
            resources.CreateBetRequestBySelectionFilter(
                selection_id=123,
                price=10,
                stake=0.99,
                bet_type="WIN",
            )

        # test customer_strategy_ref length
        with pytest.raises(
            exceptions.BetRequestInvalidCustomerStrategyRefFormatException
        ):
            resources.CreateBetRequestBySelectionFilter(
                selection_id=123,
                price=10,
                stake=10,
                bet_type="WIN",
                customer_strategy_ref="11111111111111111111111111111111111",
            )

        # test validate_customer_order_ref length
        with pytest.raises(exceptions.BetRequestInvalidCustomerOrderRefFormatException):
            resources.CreateBetRequestBySelectionFilter(
                selection_id=123,
                price=10,
                stake=10,
                bet_type="WIN",
                customer_order_ref="1111111111111111111111111111111111111111111111111111",
            )

    def test_create_bet_request_by_competitor_filter(self):
        request_filter = resources.CreateBetRequestByCompetitorFilter(
            fixture_id=1,
            market_type_id=1,
            competitor="123",
            price=10,
            stake=50,
            bet_type="WIN",
        )
        assert request_filter.fixture_id == 1
        assert request_filter.market_type_id == 1
        assert request_filter.competitor == "123"
        assert request_filter.price == 10
        assert request_filter.stake == 50
        assert request_filter.bet_type == "WIN"
        assert request_filter.handicap is None
        assert request_filter.customer_strategy_ref is None
        assert request_filter.customer_order_ref is None

        # test min stake validation
        with pytest.raises(exceptions.BetRequestIDStakeSizeException):
            resources.CreateBetRequestByCompetitorFilter(
                fixture_id=1,
                market_type_id=1,
                competitor="123",
                price=10,
                stake=0.99,
                bet_type="WIN",
            )

        # test customer_strategy_ref length
        with pytest.raises(
            exceptions.BetRequestInvalidCustomerStrategyRefFormatException
        ):
            resources.CreateBetRequestByCompetitorFilter(
                fixture_id=1,
                market_type_id=1,
                competitor="123",
                price=10,
                stake=10,
                bet_type="WIN",
                customer_strategy_ref="11111111111111111111111111111111111",
            )

        # test validate_customer_order_ref length
        with pytest.raises(exceptions.BetRequestInvalidCustomerOrderRefFormatException):
            resources.CreateBetRequestByCompetitorFilter(
                fixture_id=1,
                market_type_id=1,
                competitor="123",
                price=10,
                stake=10,
                bet_type="WIN",
                customer_order_ref="1111111111111111111111111111111111111111111111111111",
            )

    def test_create_bet_request_filter_alias_working(self):
        request_filter = resources.CreateBetRequestFilter(
            fixture_id=1,
            market_type_id=1,
            competitor="123",
            price=10,
            stake=50,
            bet_type="WIN",
        )
        assert request_filter.fixture_id == 1
        assert request_filter.market_type_id == 1
        assert request_filter.competitor == "123"
        assert request_filter.price == 10
        assert request_filter.stake == 50
        assert request_filter.bet_type == "WIN"
        assert request_filter.handicap is None
        assert request_filter.customer_strategy_ref is None
        assert request_filter.customer_order_ref is None
        assert isinstance(request_filter, resources.CreateBetRequestByCompetitorFilter)
