from .baseresource import BaseResource
from pydantic import Field, validator
from typing import Union, List, Optional
import logging
from betconnect import resources
from betconnect.utils import is_valid_uuid
from betconnect import config, exceptions
from uuid import UUID

logger = logging.getLogger(__name__)


class Filter(BaseResource):
    def generate_request_data(self, *args, **kwargs) -> dict:
        raise NotImplementedError

    def validate_stake(v: float) -> float:
        if v < config.SITE_MINIMUM_STAKE_SIZE:
            raise exceptions.BetRequestIDStakeSizeException(stake_size=v)
        else:
            return v


class GetBetRequestFilter(Filter):
    sport_id: Optional[int] = Field(default=None)
    bookmakers: Optional[List[int]] = Field(default=[])
    horse_racing_regions: List[int] = Field(default=[], alias="horseRacingRegions")
    min_odds: Optional[float] = Field(default=1.01)
    max_odds: Optional[float] = Field(default=1000)
    accept_each_way: Optional[bool] = Field(default=True)
    bet_request_id: Optional[UUID] = Field(default=None)

    # noinspection PyMethodParameters
    @validator("min_odds", pre=True)
    def validate_min_odds(cls, v: Optional[float]) -> Union[float, None]:
        if v:
            if v < 1.01:
                raise exceptions.MinOddException(min_odds=v)
        return v

    # noinspection PyMethodParameters
    @validator("bet_request_id", pre=True)
    def validate_bet_request_id(cls, v: Union[UUID, Optional[str]]) -> Optional[UUID]:
        if isinstance(v, UUID):
            return v
        elif v:
            if is_valid_uuid(v):
                return UUID(v)
            else:
                raise exceptions.BetRequestIDFormatException(bet_request_id=v)

    def generate_request_data(self, *args, **kwargs) -> dict:
        data = self.dict(exclude=kwargs["exclude"])
        if "bet_request_id" in data:
            data["bet_request_id"] = str(data["bet_request_id"])
        return data


class CreateBetRequestBySelectionFilter(Filter):
    selection_id: int
    price: float
    stake: float
    handicap: Optional[float] = Field(default=None)
    bet_type: str
    customer_strategy_ref: Optional[resources.CustomerStrategyRef] = Field(default=None)
    customer_order_ref: Optional[resources.CustomerOrderRef] = Field(default=None)

    # inherited size validator
    _size = validator("stake", allow_reuse=True)(Filter.validate_stake)

    @validator("customer_strategy_ref", pre=True)
    def parse_customer_strategy_ref(
        cls, v: Union[str, resources.CustomerStrategyRef]
    ) -> resources.CustomerStrategyRef:
        if isinstance(v, resources.CustomerStrategyRef):
            return v
        return resources.CustomerStrategyRef.create_customer_strategy_ref(
            customer_strategy_ref=v
        )

    @validator("customer_order_ref", pre=True)
    def parse_customer_order_ref(
        cls, v: Union[str, resources.CustomerOrderRef]
    ) -> resources.CustomerOrderRef:
        if isinstance(v, resources.CustomerOrderRef):
            return v
        return resources.CustomerOrderRef.create_customer_order_ref(
            customer_order_ref=v
        )

    def generate_request_data(self, *args, **kwargs) -> dict:
        data = self.dict(exclude_none=kwargs["exclude_none"])
        if "customer_order_ref" in data:
            data["customer_order_ref"] = data["customer_order_ref"][
                "customer_order_ref"
            ]
        if "customer_strategy_ref" in data:
            data["customer_strategy_ref"] = data["customer_strategy_ref"][
                "customer_strategy_ref"
            ]

        return data


class CreateBetRequestByCompetitorFilter(Filter):
    fixture_id: int
    market_type_id: int
    competitor: str
    price: float
    stake: float
    handicap: Optional[float] = Field(default=None)
    bet_type: str
    customer_strategy_ref: Optional[resources.CustomerStrategyRef] = Field(default=None)
    customer_order_ref: Optional[resources.CustomerOrderRef] = Field(default=None)

    # inherited size validator
    _size = validator("stake", allow_reuse=True)(Filter.validate_stake)

    @validator("customer_strategy_ref", pre=True)
    def parse_customer_strategy_ref(
        cls, v: Union[str, resources.CustomerStrategyRef]
    ) -> resources.CustomerStrategyRef:
        if isinstance(v, resources.CustomerStrategyRef):
            return v
        return resources.CustomerStrategyRef.create_customer_strategy_ref(
            customer_strategy_ref=v
        )

    @validator("customer_order_ref", pre=True)
    def parse_customer_order_ref(
        cls, v: Union[str, resources.CustomerOrderRef]
    ) -> resources.CustomerOrderRef:
        if isinstance(v, resources.CustomerOrderRef):
            return v
        return resources.CustomerOrderRef.create_customer_order_ref(
            customer_order_ref=v
        )

    def generate_request_data(self, *args, **kwargs) -> dict:
        data = self.dict(exclude_none=kwargs["exclude_none"])
        if "customer_order_ref" in data:
            data["customer_order_ref"] = data["customer_order_ref"][
                "customer_order_ref"
            ]
        if "customer_strategy_ref" in data:
            data["customer_strategy_ref"] = data["customer_strategy_ref"][
                "customer_strategy_ref"
            ]

        return data


# alias for backward compatibility
CreateBetRequestFilter = CreateBetRequestByCompetitorFilter
