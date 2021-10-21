from .baseresource import BaseResource
from pydantic import Field
from typing import Union

class Filter(BaseResource):
    pass

class GetBetRequestFilter(Filter):
    sport_id: int = Field(default=None)
    bookmakers: str = Field(default=None)
    min_odds: float = Field(default=1.01)
    max_odds: float = Field(default=1000)
    accept_each_way: int = Field(default=None)
    bet_request_id: str = Field(default=None)

class CreateBetRequestFilter(Filter):
    fixture_id: int
    market_type_id: int
    competitor: Union[int, str]
    price: float
    stake: int
    bet_type: str
    handicap: float = Field(default=None)
