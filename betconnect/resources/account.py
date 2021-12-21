from .baseresource import BaseResource
from datetime import datetime
from pydantic import validator, Field


class Token(BaseResource):
    token: str

    def __repr__(self):
        return f"Token: {self.token}"


class Login(BaseResource):
    message: str
    data: Token

    def __repr__(self) -> str:
        return f"Login Message: {self.message}"


class AccountPreferences(BaseResource):
    address_created: datetime
    address_line_1: str
    address_line_2: str = Field(default=None)
    address_line_3: str = Field(default=None)
    address_updated: datetime
    admin_area: str
    betconnect_pro: int
    building: int
    can_set_custom_odds: int
    city: str
    contact_number: str
    country: str
    country_iso2: str
    country_iso3: str
    created: datetime
    default_home_page: str
    display_name: str = Field(default=None)
    dob: str
    email: str
    forename: str
    full_name: str = Field(alias="fullname")
    gamstop_result: str
    kyc_result: int
    last_login: datetime
    locality: str
    marketing_terms_accepted: int
    odds_format_decimal: int
    page_size: int
    pending_withdrawal: int
    pending_withdrawal_amount: float = Field(default=None)
    postcode: str
    premise: str = Field(default=None)
    seed_pro: int
    surname: str
    thoroughfare: str
    user_category_id: int
    user_id: str
    username: str
    is_premium_subscriber: int

    # noinspection PyMethodParameters
    @validator("address_created", "address_updated", "created", pre=True)
    def date_parser(cls, v) -> datetime:
        if isinstance(v, str):
            return datetime.fromisoformat(v)
        elif isinstance(v, datetime):
            return v
        else:
            raise TypeError(f"Expected value of type str or datetime")

    def __repr__(self) -> str:
        return f"Username: {self.username} ({self.user_id})"