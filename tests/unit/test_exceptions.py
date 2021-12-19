from betconnect import exceptions
import pytest
from betconnect import enums


class TestExceptions:
    def test_invalid_personalised_production_url(self):
        exception = exceptions.InValidPersonalisedProductionURL(url="test.com")
        assert exception.url == "test.com"

        with pytest.raises(exceptions.InValidPersonalisedProductionURL):
            raise exceptions.InValidPersonalisedProductionURL(url="test.com")

    def test_unknown_betconnect_environment(self):
        exception = exceptions.UnknownBetConnectEnvironment(
            environment=enums.Environment.PRODUCTION
        )
        assert exception.environment == enums.Environment.PRODUCTION

        with pytest.raises(exceptions.UnknownBetConnectEnvironment):
            raise exceptions.UnknownBetConnectEnvironment(
                environment=enums.Environment.PRODUCTION
            )

    def test_login_missing_token_in_response(self):
        exception = exceptions.LoginMissingTokenInResponse()
        assert str(exception) == f"Missing login token in response data"

        with pytest.raises(exceptions.LoginMissingTokenInResponse):
            raise exceptions.LoginMissingTokenInResponse()

    def test_failed_login(self):
        exception = exceptions.FailedLogin(username="test_username")
        assert exception.username == "test_username"

        with pytest.raises(exceptions.FailedLogin):
            raise exceptions.FailedLogin("test_username")

    def test_unexpected_response_status_code(self):
        exception = exceptions.UnexpectedResponseStatusCode(
            status_code=12345, url="betconnect.com"
        )
        assert exception.status_code == 12345
        assert exception.url == "betconnect.com"

        with pytest.raises(exceptions.UnexpectedResponseStatusCode):
            raise exceptions.UnexpectedResponseStatusCode(
                status_code=12345, url="betconnect.com"
            )

    def test_gamstop_exception(self):
        exception = exceptions.GamStopException()
        assert (
            str(exception)
            == "API access if strictly forbidden for users with a Gamstop ban against their account."
        )

        with pytest.raises(exceptions.GamStopException):
            raise exceptions.GamStopException()

    def test_missing_user_preferences(self):
        exception = exceptions.MissingUserPerferences()
        assert (
            str(exception)
            == "Unable to get user_id via get_user_preferences. Please supply a value or speak to your account manager"
        )

        with pytest.raises(exceptions.MissingUserPerferences):
            raise exceptions.MissingUserPerferences()

    def test_min_odds(self):
        exception = exceptions.MinOddException(min_odds=0)
        assert exception.min_odds == 0

        with pytest.raises(exceptions.MinOddException):
            raise exceptions.MinOddException(min_odds=0)

    def test_bet_request_stale_size(self):
        exception = exceptions.BetRequestIDStakeSizeException(stake_size=9)
        assert exception.stake_size == 9

        with pytest.raises(exceptions.BetRequestIDStakeSizeException):
            raise exceptions.BetRequestIDStakeSizeException(stake_size=9)

    def test_bet_request_invalid_customer_order_ref(self):
        exception = exceptions.BetRequestInvalidCustomerOrderRefFormatException(
            customer_order_ref="1234"
        )
        assert exception.customer_order_ref == "1234"

        with pytest.raises(exceptions.BetRequestInvalidCustomerOrderRefFormatException):
            raise exceptions.BetRequestInvalidCustomerOrderRefFormatException(
                customer_order_ref="1234"
            )

    def test_bet_request_invalid_customer_strategy_ref(self):
        exception = exceptions.BetRequestInvalidCustomerStrategyRefFormatException(
            customer_strategy_ref=""
        )
        assert exception.customer_strategy_ref == ""

        with pytest.raises(
            exceptions.BetRequestInvalidCustomerStrategyRefFormatException
        ):
            raise exceptions.BetRequestInvalidCustomerStrategyRefFormatException(
                customer_strategy_ref=""
            )

    def test_api_error(self):
        exceptions.APIError(response=None, uri="betconnect.com")
        with pytest.raises(exceptions.APIError):
            raise exceptions.APIError(response=None, uri="betconnect.com")
