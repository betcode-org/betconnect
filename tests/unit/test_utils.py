from betconnect import utils
import pytest
from uuid import UUID
from betconnect import exceptions

class TestUtils:

    def test_is_valid_uuid(self):
        assert utils.is_valid_uuid(uuid_to_test='123243') is False
        assert utils.is_valid_uuid('c9bf9e57-1685-4c89-bafb-ff5af830be8a')

    def test_calculate_book_percentage(self):
        raise NotImplementedError

    def test_parse_bet_request_id(self):
        assert isinstance(utils.parse_bet_request_id('c9bf9e57-1685-4c89-bafb-ff5af830be8a'), UUID)
        with pytest.raises(Exception) as e:
            utils.parse_bet_request_id('c9bf9e57-1685-4c89-bafb-ff5a')

    def test_create_customer_strategy_ref(self):
        customer_stratey_ref = utils.create_customer_strategy_ref('1234')
        assert customer_stratey_ref.customer_strategy_ref == '1234'
        customer_stratey_ref = utils.create_customer_strategy_ref('123 4')
        assert customer_stratey_ref.customer_strategy_ref == '1234'

        with pytest.raises(exceptions.BetRequestInvalidCustomerStrategyRefFormatException):
            utils.create_customer_strategy_ref('12343333333333333333333333')

        with pytest.raises(exceptions.BetRequestInvalidCustomerStrategyRefFormatException):
            utils.create_customer_strategy_ref('')

    def test_customer_order_ref(self):

        customer_order_ref = utils.create_customer_order_ref(customer_order_ref='12344')
        assert customer_order_ref.customer_order_ref == '12344'

        with pytest.raises(exceptions.BetRequestInvalidCustomerOrderRefFormatException):
            utils.create_customer_order_ref(customer_order_ref='')

        with pytest.raises(exceptions.BetRequestInvalidCustomerOrderRefFormatException):
            utils.create_customer_order_ref(customer_order_ref='11111111111111111111111111111111111111111')