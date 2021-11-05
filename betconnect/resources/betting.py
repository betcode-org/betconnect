from .baseresource import BaseResource
from pydantic import BaseModel, Field, validator
from typing import List, Union
from datetime import datetime


class ActiveBookmakers(BaseResource):
    name: str
    bookmaker_id: int
    order: int
    active: int

    def __repr__(self):
        return f"Bookmaker: {self.name} ({self.bookmaker_id}), Active: {self.active}"


class ActiveSports(BaseResource):
    id: int
    sport_id: int
    name: str
    display_name: str
    slug: str
    order: int
    active: int
    rate: float
    bets_available: int = Field(default=None)

    def __repr__(self):
        return f"Sport: {self.display_name} ({self.id})"


class ActiveRegion(BaseResource):
    name: str
    region_id: int
    iso: str = Field(default=None)
    order: int

    def __repr__(self):
        return 'Region: {}({})'.format(self.name, self.region_id)


class ActiveCompetitions(BaseResource):
    name: str
    display_name: str
    competition_id: int
    active: int
    order: int

    def __repr__(self):
        return f"Competition: {self.name}({self.competition_id})"


class ActiveMarketTypes(BaseResource):
    market_type_id: int
    name: str
    active: int

    def __repr__(self):
        return f"Market Type: {self.name}({self.market_type_id})"


class ActiveMarkets(BaseResource):
    name: str
    display_name: str
    trading_status: str
    is_handicap: str
    market_type_id: int
    order: int
    handicap: str = None

    def __repr__(self):
        return f"Market: {self.name} {self.trading_status}"


class Balance(BaseResource):
    balance: float

    def __repr__(self):
        return f"Balance: {self.balance}"


class PricesBookmaker(BaseResource):
    id: str
    name: str


class Price(BaseResource):
    price: str
    numerator: str
    denominator: str
    bookmakers: List[PricesBookmaker] = Field(default=[])

    @classmethod
    def create_from_dict(cls, d):
        return [cls.parse_obj(data) for data in d['prices']]

    def __repr__(self):
        return f"Price: {self.price}, Bookmakers #:{len(self.bookmakers)}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Price):
            return other.price == self.price
        return False


class ActiveSelections(BaseResource):
    name: str
    trading_status: str
    selection_id: int
    ut: str
    competitor: str

    def __eq__(self, other) -> bool:
        if isinstance(other, ActiveSelections):
            return other.selection_id == self.selection_id
        return False

    def __repr__(self):
        return f"Selection: {self.name} ({self.selection_id})"


class ActiveFixtures(BaseResource):
    fixture_id: int
    display_name: str
    startdate: str
    time: str
    selections: List[ActiveSelections] = Field(default=[])

    def _add_selection(self, selection: ActiveSelections):
        if selection not in self.selections:
            self.selections.append(selection)

    def add_selections(self, selections: Union[ActiveSelections, List[ActiveSelections]]) -> None:
        if isinstance(selections, ActiveSelections):
            self._add_selection(selection=selections)
        elif isinstance(selections, list):
            [self._add_selection(selection=s) for s in selections if isinstance(s, ActiveSelections)]

    def __repr__(self):
        return f"Fixture: {self.display_name}({self.fixture_id}) {self.startdate}"


class BackersStats(BaseResource):
    strike_rate: float
    roi: float
    bet_requests: str
    recent_performance: str = Field(default=None)


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
    bet_request_id: str
    bet_type: str
    requested_stake: float
    liability: float
    backer_stats: BackersStats
    others_viewing_bet: str

    @validator('backer_stats', pre=True)
    def stats_parser(cls, v):
        if isinstance(v, dict):
            return BackersStats.create_from_dict(v)
        else:
            raise TypeError(f"Expected value of dict")

    @validator('price', pre=True)
    def price_parser(cls, v):
        if isinstance(v, dict):
            return Price(
                price=v['decimal'],
                numerator=v['fraction']['numerator'],
                denominator=v['fraction']['denominator'],
            )
        else:
            raise TypeError(f"Expected value of dict")

    @validator('start_time_utc', pre=True)
    def date_parser(cls, v):
        if isinstance(v, str):
            return datetime.fromisoformat(v)
        elif isinstance(v, datetime):
            return v
        else:
            raise TypeError(f"Expected value of type str or datetime")


class BetRequestCreate(BaseResource):
    bet_request_id: str
    created: datetime
    debit_stake: float
    debit_commission: float

    @validator('created', pre=True)
    def date_parser(cls, v):
        if isinstance(v, str):
            return datetime.fromisoformat(v)
        elif isinstance(v, datetime):
            return v
        else:
            raise TypeError(f"Expected value of type str or datetime")


class BetRequestMatch(BaseResource):
    matched: bool
    available: bool
    bet_request_id: str = Field(default=None)
    bet_id: str = Field(default=None)
    bet_status: str = Field(default=None)
    amount_matched: float = Field(default=None)
    viewed: dict = Field(default=None)


class BetHistory(BaseResource):
    bet_request_id: str
    bet_request_status: str
    bet_type_name: str
    competition_name: str
    create_at: datetime = Field(default=None)
    each_way_factor: str = Field(default=None)
    fill_percentage: float
    fixture_name: str
    fixture_start_date: datetime = Field(alias='fixture_startdate')
    handicap: float = Field(default=None)
    market_name: str
    matched_stake: float
    price: float
    price_denominator: int
    price_numerator: int
    region_iso: str = Field(default=None)
    region_name: str
    selection_name: str
    sport_name: str
    stake: float

    @validator('create_at', 'fixture_start_date', pre=True)
    def date_parser(cls, v):
        if isinstance(v, str):
            return datetime.fromisoformat(v)
        elif isinstance(v, datetime):
            return v
        else:
            raise TypeError(f"Expected value of type str or datetime")

class ActiveBets(BaseResource):
    bet_request_id: str
    bet_type_name: str
    competition_name: str
    created_at: datetime
    each_way_factor: float = Field(default=None)
    fill_percentage: float
    fixture_name: str
    fixture_start_date: datetime = Field(alias='fixture_startdate')
    handicap: float = Field(default=None)
    market_name: str
    matched_stake: float
    price: float
    price_denominator: int
    selection_name: str
    sport_name: str
    stake: float
    status_name: str

    @validator('created_at', 'fixture_start_date', pre=True)
    def date_parser(cls, v):
        if isinstance(v, str):
            return datetime.fromisoformat(v)
        elif isinstance(v, datetime):
            return v
        else:
            raise TypeError(f"Expected value of type str or datetime")

class ActiveBetsRequest(BaseResource):
    bets: List[ActiveBets]
    bets_active: int
    last_page: int
    total_bets: int

class BetHistoryRequest(BaseResource):
    bets: List[BetHistory]
    last_page: int
    total_bets: int

class SelectionsForMarket(BaseResource):
    source_fixture_id: str
    source_market_id: str
    source_market_type_id: str
    source_selection_id: str
    trading_status: str
    name: str
    competitor_id: str
    ut: datetime
    order: int
    max_price: float
    prices: List[Price]

    @validator('ut', pre=True)
    def date_parser(cls, v):
        if isinstance(v, str):
            return datetime.fromisoformat(v)
        elif isinstance(v, datetime):
            return v
        else:
            raise TypeError(f"Expected value of type str or datetime")

class Viewed(BaseResource):
    prev: str
    next: str

class BetRequestMatchMore(BaseResource):
    matched: bool
    available: bool
    viewed: Viewed