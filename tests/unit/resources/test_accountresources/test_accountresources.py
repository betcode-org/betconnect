from betconnect import resources
from datetime import datetime


class TestAccountResources:
    def test_token(self):
        token = resources.Token(token="123456")
        assert token.token == "123456"

    def test_login(self):
        login = resources.Login(message="Login Successful", data={"token": "12345"})
        assert login.message == "Login Successful"
        assert isinstance(login.data, resources.Token)

    def test_account_preferences(self):

        account_preferences = resources.AccountPreferences(
            address_created="2021-06-16 05:52:24",
            address_line_1="1 London Road",
            address_line_3="London",
            address_updated="2021-06-16 05:52:24",
            admin_area="London",
            betconnect_pro=10,
            building="1",
            can_set_custom_odds=0,
            city="London",
            contact_number="11111111111",
            country="United Kingdom",
            country_iso2="GB",
            country_iso3="GBR",
            created="2021-06-16 05:52:24",
            default_home_page="dashboard",
            dob="2000-01-01",
            email="testemail@gmail.com",
            forename="Jim",
            full_name="Jim Bob",
            gamstop_result="N",
            kyc_result=1,
            last_login="2021-12-18 12:10:57",
            locality="London",
            marketing_terms_accepted=0,
            odds_format_decimal=0,
            page_size=25,
            pending_withdrawal=0,
            postcode="N1",
            seed_pro=0,
            surname="Bob",
            thoroughfare="London Road",
            user_category_id=1,
            user_id="a6a1gb91-6217-4e0d-b759-fbcaasb7a8ac",
            username="jbob",
            is_premium_subscriber=0,
        )
        assert isinstance(account_preferences.address_created, datetime)
        assert account_preferences.address_line_1 == "1 London Road"
        assert account_preferences.address_line_2 is None
        assert account_preferences.address_line_3 == "London"
        assert isinstance(account_preferences.address_updated, datetime)
        assert account_preferences.admin_area == "London"
        assert account_preferences.betconnect_pro == 10
        assert account_preferences.building == "1"
        assert account_preferences.can_set_custom_odds == 0
        assert account_preferences.city == "London"
        assert account_preferences.contact_number == "11111111111"
        assert account_preferences.country == "United Kingdom"
        assert account_preferences.country_iso2 == "GB"
        assert account_preferences.country_iso3 == "GBR"
        assert isinstance(account_preferences.created, datetime)
        assert account_preferences.default_home_page == "dashboard"
        assert account_preferences.display_name is None
        assert account_preferences.dob == "2000-01-01"
        assert account_preferences.email == "testemail@gmail.com"
        assert account_preferences.forename == "Jim"
        assert account_preferences.full_name == "Jim Bob"
        assert account_preferences.gamstop_result == "N"
        assert account_preferences.kyc_result == 1
        assert isinstance(account_preferences.last_login, datetime)
        assert account_preferences.locality == "London"
        assert account_preferences.kyc_result == 1
        assert account_preferences.odds_format_decimal == 0
        assert account_preferences.page_size == 25
        assert account_preferences.pending_withdrawal == 0
        assert account_preferences.pending_withdrawal_amount is None
        assert account_preferences.postcode == "N1"
        assert account_preferences.premise is None
        assert account_preferences.seed_pro == 0
        assert account_preferences.surname == "Bob"
        assert account_preferences.thoroughfare == "London Road"
        assert account_preferences.user_category_id == 1
        assert account_preferences.user_id == "a6a1gb91-6217-4e0d-b759-fbcaasb7a8ac"
        assert account_preferences.username == "jbob"
        assert account_preferences.is_premium_subscriber == 0

        account_preferences = resources.AccountPreferences(
            address_created="2021-06-16 05:52:24",
            address_line_1="1 London Road",
            address_updated="2021-06-16 05:52:24",
            admin_area=None,
            betconnect_pro=10,
            can_set_custom_odds=0,
            contact_number="11111111111",
            country="United Kingdom",
            country_iso2="GB",
            country_iso3="GBR",
            created="2021-06-16 05:52:24",
            default_home_page="dashboard",
            dob="2000-01-01",
            email="testemail@gmail.com",
            forename="Jim",
            full_name="Jim Bob",
            gamstop_result="N",
            kyc_result=1,
            last_login="2021-12-18 12:10:57",
            locality=None,
            marketing_terms_accepted=0,
            odds_format_decimal=0,
            page_size=25,
            pending_withdrawal=0,
            postcode="N1",
            seed_pro=0,
            surname="Bob",
            user_category_id=1,
            user_id="a6a1gb91-6217-4e0d-b759-fbcaasb7a8ac",
            username="jbob",
            is_premium_subscriber=0,
        )
        assert account_preferences.address_line_2 is None
        assert account_preferences.address_line_3 is None
        assert account_preferences.admin_area is None
        assert account_preferences.locality is None
        assert account_preferences.city is None
        assert account_preferences.thoroughfare is None
        assert account_preferences.building is None
