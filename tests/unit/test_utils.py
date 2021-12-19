from betconnect import utils
import pytest
from uuid import UUID


class TestUtils:
    def test_is_valid_uuid(self):
        assert utils.is_valid_uuid(uuid_to_test="123243") is False
        assert utils.is_valid_uuid("c9bf9e57-1685-4c89-bafb-ff5af830be8a")

    def test_calculate_book_percentage(self):
        raise NotImplementedError

    def test_parse_bet_request_id(self):
        assert isinstance(
            utils.parse_bet_request_id("c9bf9e57-1685-4c89-bafb-ff5af830be8a"), UUID
        )
        with pytest.raises(Exception):
            utils.parse_bet_request_id("c9bf9e57-1685-4c89-bafb-ff5a")
