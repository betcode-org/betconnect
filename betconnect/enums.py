from enum import Enum


class Environment(Enum):
    PRODUCTION = "Production"
    STAGING = "Staging"


class BetSide(Enum):
    BACK = "back"
    LAY = "lay"


class BetRequestStatus(Enum):
    ACTIVE = "active"
    SETTLED = "settled"


class MarketStatus(Enum):
    OPEN = "Open"
    SUSPENDED = "Suspended"
    CLOSED = "Closed"


class TradingStatus(Enum):
    OPEN = "Open"
    ACTIVE = "Active"
    CLOSED = "Closed"
    NON_RUNNER = "NonRunner"


class BetStatus(Enum):
    RECEIVED = "received"
    CANCELLED = "cancelled"
    REJECTED = "rejected"
    VOIDED_BY_PRO = "voided_by_pro"
    VOIDED_BY_ADMIN = "voided_by_admit"
    MATCHED = "matched"
    MATCHED_MORE = "matched_more"
    EXPIRED = "expired"
