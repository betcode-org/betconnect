import uuid
from datetime import datetime
from typing import List, Optional
from pydantic import Field, validator
from .baseresource import BaseResource
from uuid import UUID
import logging
from betconnect import config
from betconnect import utils
from betconnect import exceptions

logger = logging.getLogger(__name__)


class CustomerOrderRef(BaseResource):
    customer_order_ref: Optional[str] = Field(default=None)

    @staticmethod
    def generate_random_order_ref() -> str:
        return str(uuid.uuid4())

    @staticmethod
    def is_valid_customer_order_ref(customer_order_ref: str) -> bool:
        if (len(customer_order_ref) < config.MIN_CUSTOMER_ORDER_REF_LENGTH) or (
            len(customer_order_ref) > config.MAX_CUSTOMER_ORDER_REF_LENGTH
        ):
            return False
        return True

    @classmethod
    def create_customer_order_ref(cls, customer_order_ref: str):
        if cls.is_valid_customer_order_ref(customer_order_ref=customer_order_ref):
            return cls(customer_order_ref=customer_order_ref)
        raise exceptions.BetRequestInvalidCustomerOrderRefFormatException(
            customer_order_ref=customer_order_ref
        )

    @validator("customer_order_ref", pre=True)
    def validate_customer_order_ref(cls, v: str) -> Optional[str]:
        if v:
            assert isinstance(v, str)
            if " " in v:
                v = v.replace(" ", "")
                logger.warning(
                    f"customer_order_ref contains spaces. These have been removed"
                )
            if cls.is_valid_customer_order_ref(v):
                return v
            else:
                raise exceptions.BetRequestInvalidCustomerOrderRefFormatException(
                    customer_order_ref=v
                )

    def __repr__(self) -> str:
        return f"Customer order ref: {self.customer_order_ref}"

    def __str__(self) -> str:
        return self.customer_order_ref


class CustomerStrategyRef(BaseResource):
    customer_strategy_ref: Optional[str] = Field(default=None)

    @staticmethod
    def is_valid_customer_strategy_ref(customer_strategy_ref: str) -> bool:
        if (len(customer_strategy_ref) < config.MIN_CUSTOMER_STRATEGY_REF_LENGTH) or (
            len(customer_strategy_ref) > config.MAX_CUSTOMER_STRATEGY_REF_LENGTH
        ):
            return False
        return True

    @classmethod
    def create_customer_strategy_ref(
        cls, customer_strategy_ref: str, hash_value: bool = False
    ):
        if cls.is_valid_customer_strategy_ref(
            customer_strategy_ref=customer_strategy_ref
        ):
            if hash_value:
                return cls(
                    customer_strategy_ref=utils.create_cheap_hash(
                        txt=customer_strategy_ref, length=15
                    )
                )
            else:
                return cls(customer_strategy_ref=customer_strategy_ref)
        raise exceptions.BetRequestInvalidCustomerStrategyRefFormatException(
            f"customer_strategy_ref ({customer_strategy_ref}) should be between 1-15 characters. Supplied length = {len(customer_strategy_ref)}"
        )

    # noinspection PyMethodParameters
    @validator("customer_strategy_ref", pre=True)
    def validate_customer_strategy_ref(cls, v: str) -> str:
        if v:
            assert isinstance(v, str)
            if " " in v:
                v = v.replace(" ", "")
                logger.warning(
                    f"customer_strategy_ref contains spaces. These have been removed"
                )
            if cls.is_valid_customer_strategy_ref(customer_strategy_ref=v):
                return v

            raise exceptions.BetRequestInvalidCustomerStrategyRefFormatException(
                customer_strategy_ref=v
            )

    def __str__(self) -> str:
        return self.customer_strategy_ref

    def __repr__(self) -> str:
        return f"Customer strategy ref: {self.customer_strategy_ref}"


class ActiveBookmaker(BaseResource):
    name: str
    bookmaker_id: int
    order: int
    active: int

    def __repr__(self) -> str:
        return f"Bookmaker: {self.name} ({self.bookmaker_id}), Active: {self.active}"


class ActiveSport(BaseResource):
    id: int
    sport_id: int
    name: str
    display_name: str
    slug: str
    order: int
    active: int
    rate: float
    bets_available: Optional[int] = Field(default=None)

    def __repr__(self) -> str:
        return f"Sport: {self.display_name} ({self.id})"


class ActiveRegion(BaseResource):
    name: str
    region_id: int
    iso: Optional[str] = Field(default=None)
    order: int

    def __repr__(self) -> str:
        return "Region: {}({})".format(self.name, self.region_id)


class ActiveCompetition(BaseResource):
    name: str
    display_name: str
    competition_id: int
    active: int
    order: int

    # waiting on sport_id: int
    # waiting on region_id: int

    def __repr__(self) -> str:
        return f"Competition: {self.name}({self.competition_id})"


class ActiveMarketType(BaseResource):
    market_type_id: int
    name: str
    active: int

    def __repr__(self) -> str:
        return f"Market Type: {self.name}({self.market_type_id})"


class ActiveMarket(BaseResource):
    name: str
    display_name: str
    trading_status: str
    is_handicap: str
    source_market_id: str
    market_type_id: int
    order: int
    handicap: Optional[str] = Field(default=None)
    bet_types: List[str] = []

    # waiting on fixture_id: int

    def __repr__(self) -> str:
        return f"Market: {self.name} {self.trading_status}"


class Balance(BaseResource):
    balance: int

    @property
    def balance_uk_pounds(self) -> float:
        try:
            return round(self.balance / 100, 3)
        except ZeroDivisionError:
            return 0

    def __repr__(self) -> str:
        return f"Balance: {self.balance}"


class PricesBookmaker(BaseResource):
    id: str
    name: str

    def __repr__(self) -> str:
        return f"Bookie Name: {self.name} ({self.id})"


class Price(BaseResource):
    price: str
    numerator: str
    denominator: str
    bookmakers: List[PricesBookmaker] = Field(default=[])

    @classmethod
    def create_from_dict(cls, d):
        return [cls.parse_obj(data) for data in d["prices"]]

    def __repr__(self) -> str:
        return f"Price: {self.price}, Bookmakers #:{len(self.bookmakers)}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Price):
            return other.price == self.price
        return False


class ActiveSelection(BaseResource):
    name: str
    trading_status: str
    selection_id: str
    ut: datetime
    competitor: str

    # waiting on fixture_id: int

    # noinspection PyMethodParameters
    @validator("ut", pre=True)
    def date_parser(cls, v):
        if isinstance(v, str):
            return datetime.fromisoformat(v)
        elif isinstance(v, datetime):
            return v
        else:
            raise TypeError(f"Expected value of type str or datetime")

    def __eq__(self, other) -> bool:
        if isinstance(other, ActiveSelection):
            return other.selection_id == self.selection_id
        return False

    def __repr__(self) -> str:
        return f"Selection: {self.name} ({self.selection_id})"


class ActiveFixture(BaseResource):
    fixture_id: int
    display_name: str
    start_date: datetime = Field(alias="startdate")
    time: str
    each_way_active: Optional[str] = Field(default=None)

    # waiting on sport_id: int ?
    # waiting on region_id: int ?
    # waiting on competition_id: int ?

    # noinspection PyMethodParameters
    @validator("start_date", pre=True)
    def date_parser(cls, v) -> datetime:
        if isinstance(v, str):
            return datetime.fromisoformat(v)
        elif isinstance(v, datetime):
            return v
        else:
            raise TypeError(f"Expected value of type str or datetime")

    def __repr__(self) -> str:
        return f"Fixture: {self.display_name}({self.fixture_id}) {self.start_date}"


class BackersStats(BaseResource):
    strike_rate: float
    roi: float
    bet_requests: str
    recent_performance: Optional[str] = Field(default=None)

    def __repr__(self) -> str:
        return f"Strike Rate: {self.strike_rate}, ROI: {self.roi}, Recent: {self.recent_performance}"


class BetRequest(BaseResource):
    sport_name: str
    sport_id: str
    competition_name: str
    region_name: str
    start_time_utc: datetime
    fixture_name: str
    market_name: str
    selection_name: str
    price: Price
    fixture_id: int
    market_type_id: int
    competitor: str
    bet_request_id: UUID
    bet_type: Optional[str] = Field(default=None)
    requested_stake: float
    liability: float
    locked_stake: float
    backer_stats: BackersStats
    others_viewing_bet: int
    lockable: bool
    # waiting on customer_order_ref: str = Field(default=None)
    # waiting on customer_strategy_ref: str = Field(default=None)

    # noinspection PyMethodParameters
    @validator("backer_stats", pre=True)
    def stats_parser(cls, v) -> BackersStats:
        if isinstance(v, dict):
            return BackersStats.create_from_dict(v)
        else:
            raise TypeError(f"Expected value of dict")

    # noinspection PyMethodParameters
    @validator("price", pre=True)
    def price_parser(cls, v) -> Price:
        if isinstance(v, dict):
            return Price(
                price=v["decimal"],
                numerator=v["fraction"]["numerator"],
                denominator=v["fraction"]["denominator"],
            )
        else:
            raise TypeError(f"Expected value of dict")

    # noinspection PyMethodParameters
    @validator("start_time_utc", pre=True)
    def date_parser(cls, v) -> datetime:
        if isinstance(v, str):
            return datetime.fromisoformat(v)
        elif isinstance(v, datetime):
            return v
        else:
            raise TypeError(f"Expected value of type str or datetime")

    def __hash__(self):
        return hash(
            f"{self.fixture_name}-{self.selection_name}-{self.start_time_utc.isoformat()}"
        )


class BetRequestCreate(BaseResource):
    bet_request_id: UUID
    created: datetime
    debit_stake: float
    debit_commission: float

    # noinspection PyMethodParameters
    @validator("created", pre=True)
    def date_parser(cls, v) -> datetime:
        if isinstance(v, str):
            return datetime.fromisoformat(v)
        elif isinstance(v, datetime):
            return v
        else:
            raise TypeError(f"Expected value of type str or datetime")

    def __repr__(self) -> str:
        return f"Bet: {str(self.bet_request_id)}, Debited Stake: {self.debit_stake}"


class BetRequestMatch(BaseResource):
    matched: bool
    available: bool
    bet_request_id: Optional[UUID] = Field(default=None)
    bet_id: Optional[str] = Field(default=None)
    bet_status: Optional[str] = Field(default=None)
    amount_matched: Optional[float] = Field(default=None)
    viewed: Optional[dict] = Field(default=None)

    def __repr__(self) -> str:
        return f"Bet: {str(self.bet_request_id)}, Matched: {self.matched}, Available: {self.available}"


class BetHistory(BaseResource):
    bet_request_id: UUID
    bet_request_status: str
    bet_type_name: Optional[str] = Field(default=None)
    competition_name: str
    create_at: Optional[datetime] = Field(default=None)
    each_way_factor: Optional[str] = Field(default=None)
    fill_percentage: float
    fixture_name: str
    fixture_start_date: datetime = Field(alias="fixture_startdate")
    handicap: Optional[float] = Field(default=None)
    market_name: str
    matched_stake: float
    price: float
    price_denominator: int
    price_numerator: int
    region_iso: Optional[str] = Field(default=None)
    region_name: str
    selection_name: str
    sport_name: str
    stake: float

    # noinspection PyMethodParameters
    @validator("create_at", "fixture_start_date", pre=True)
    def date_parser(cls, v) -> datetime:
        if isinstance(v, str):
            return datetime.fromisoformat(v)
        elif isinstance(v, datetime):
            return v
        else:
            raise TypeError(f"Expected value of type str or datetime")

    def __repr__(self) -> str:
        return f"Bet: {str(self.bet_request_id)}, Competition: {self.competition_name}, Selection: {self.selection_name},Price: {self.price}, Stake: {self.stake}"


class MyActiveBet(BaseResource):
    actioned_at: datetime
    adjustment: Optional[str] = Field(default=None)  # TODO check type
    adjustment_type: Optional[str] = Field(default=None)  # TODO check type
    bet_created: int
    bet_request_id: UUID
    bet_request_status_id: int
    bet_request_user_id: UUID
    bet_type_name: Optional[str] = Field(default=None)
    competition_name: str
    count_in_place: Optional[int] = Field(default=None)  # TODO check type
    customer_order_ref: Optional[CustomerOrderRef] = Field(default=None)
    customer_strategy_ref: Optional[CustomerStrategyRef] = Field(default=None)
    each_way_factor: Optional[int] = Field(default=None)
    fill_percentage: float
    fixture_name: str
    fixture_start_date: datetime = Field(alias="fixture_startdate")
    handicap: Optional[str] = Field(default=None)
    market_name: str
    matched_stake: int
    price: Price
    profit: int
    profit_loss: Optional[int] = Field(default=None)
    region_iso: Optional[str] = Field(default=None)
    region_name: str
    result_type_name: Optional[str] = Field(default=None)
    selection_name: str
    sport_external_id: int
    sport_name: str
    sport_slug: str
    stake: int
    status_name: str
    status_slug: str
    sub_account_id: Optional[str] = Field(default=None)  # TODO check type

    # noinspection PyMethodParameters
    @validator("actioned_at", "fixture_start_date", pre=True)
    def date_parser(cls, v) -> datetime:
        if isinstance(v, str):
            return datetime.fromisoformat(v)
        elif isinstance(v, datetime):
            return v
        else:
            raise TypeError(f"Expected value of type str or datetime")

    # noinspection PyMethodParameters
    @validator("customer_order_ref", pre=True)
    def parse_customer_order_ref(cls, v) -> Optional[CustomerOrderRef]:
        if v:
            return CustomerOrderRef(customer_order_ref=v)

    # noinspection PyMethodParameters
    @validator("customer_strategy_ref", pre=True)
    def parse_customer_strategy_ref(cls, v) -> Optional[CustomerStrategyRef]:
        if v:
            return CustomerStrategyRef(customer_strategy_ref=v)

    # noinspection PyMethodParameters
    @validator("price", pre=True)
    def price_parser(cls, v) -> Price:
        if isinstance(v, dict):
            return Price(
                price=v["decimal"],
                numerator=v["fraction"]["numerator"],
                denominator=v["fraction"]["denominator"],
            )
        else:
            raise TypeError(f"Expected value of dict")

    def __repr__(self) -> str:
        return f"Bet: {str(self.bet_request_id)}, Competition: {self.competition_name}, Selection: {self.selection_name},Price: {self.price}, Stake: {self.stake}, Profit: {self.profit}"


class BetRequestStop(BaseResource):
    pending: bool

    def __repr__(self) -> str:
        return f"Pending: {self.pending}"


class MyBetsBetRequests(BaseResource):
    bets: List[MyActiveBet]
    bets_active: int
    last_page: int
    total_bets: int

    def __repr__(self) -> str:
        return f"Bets Active: {self.bets_active}"


class ActiveBet(BaseResource):
    bet_request_id: UUID
    bet_type_name: Optional[str] = Field(default=None)
    competition_name: str
    created_at: datetime
    customer_order_ref: Optional[CustomerOrderRef] = Field(default=None)
    customer_strategy_ref: Optional[CustomerStrategyRef] = Field(default=None)
    each_way_factor: Optional[float] = Field(default=None)
    fill_percentage: float
    fixture_id: Optional[int] = Field(default=None)
    fixture_name: str
    fixture_start_date: datetime = Field(alias="fixture_startdate")
    handicap: Optional[float] = Field(default=None)
    market_name: str
    matched_stake: float
    price: float
    price_denominator: int
    price_numerator: int
    selection_name: str
    sport_name: str
    stake: float
    status_name: str

    # noinspection PyMethodParameters
    @validator("customer_order_ref", pre=True)
    def parse_customer_order_ref(cls, v) -> Optional[CustomerOrderRef]:
        if v:
            return CustomerOrderRef(customer_order_ref=v)

    # noinspection PyMethodParameters
    @validator("customer_strategy_ref", pre=True)
    def parse_customer_strategy_ref(cls, v) -> Optional[CustomerStrategyRef]:
        if v:
            return CustomerStrategyRef(customer_strategy_ref=v)

    # noinspection PyMethodParameters
    @validator("created_at", "fixture_start_date", pre=True)
    def date_parser(cls, v) -> datetime:
        if isinstance(v, str):
            return datetime.fromisoformat(v)
        elif isinstance(v, datetime):
            return v
        else:
            raise TypeError(f"Expected value of type str or datetime")

    def __repr__(self) -> str:
        return f"Bet: {str(self.bet_request_id)}, Competition: {self.competition_name}, Selection: {self.selection_name}, Price: {self.price}, Stake: {self.stake}"


class ActiveBetRequests(BaseResource):
    bets: List[ActiveBet]
    bets_active: int
    last_page: int
    total_bets: int

    def __repr__(self) -> str:
        return f"Bets Active: {self.bets_active}"


class BetHistoryRequest(BaseResource):
    bets: List[BetHistory]
    last_page: int
    total_bets: int

    def __repr__(self) -> str:
        return f"Bets #: {len(self.bets)}"


class SelectionsForMarket(BaseResource):
    source_fixture_id: str
    source_market_id: str
    source_market_type_id: str
    source_selection_id: str
    trading_status: str
    name: str
    competitor_id: Optional[str] = Field(default=None)
    ut: datetime
    order: int
    max_price: Optional[float] = Field(default=None)
    prices: List[Price]

    # noinspection PyMethodParameters
    @validator("ut", pre=True)
    def date_parser(cls, v) -> datetime:
        if isinstance(v, str):
            return datetime.fromisoformat(v)
        elif isinstance(v, datetime):
            return v
        else:
            raise TypeError(f"Expected value of type str or datetime")


class LineMarketsSelectionsForMarket(BaseResource):
    name: str
    display_name: str
    handicap: str
    line_data: List[SelectionsForMarket]


class Viewed(BaseResource):
    prev: UUID
    next: UUID

    def __repr__(self) -> str:
        return f"Prev: {self.prev}->Next: {self.next}"


class BetRequestMatchMore(BaseResource):
    matched: bool
    available: bool
    viewed: Viewed

    def __repr__(self) -> str:
        return f"Matched: {self.matched}, Available: {self.available}"


class LockBet(BaseResource):
    pass
