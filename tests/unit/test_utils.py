from betconnect import utils
import pytest
from uuid import UUID
from betconnect import resources


class TestUtils:
    def test_is_valid_uuid(self):
        assert utils.is_valid_uuid(uuid_to_test="123243") is False
        assert utils.is_valid_uuid("c9bf9e57-1685-4c89-bafb-ff5af830be8a")

    def test_calculate_book_percentage(self, mock_selections_for_market_response):
        all_selections = [
            resources.SelectionsForMarket.create_from_dict(s)
            for s in mock_selections_for_market_response[1]["data"]
        ]
        assert (
            utils.calculate_book_percentage(market_selections=all_selections) == 1.222
        )

    def test_parse_bet_request_id(self):
        assert isinstance(
            utils.parse_bet_request_id("c9bf9e57-1685-4c89-bafb-ff5af830be8a"), UUID
        )
        with pytest.raises(Exception):
            utils.parse_bet_request_id("c9bf9e57-1685-4c89-bafb-ff5a")
