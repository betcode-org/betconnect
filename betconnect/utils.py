from __future__ import annotations
import hashlib
from typing import List, Union, TYPE_CHECKING
from uuid import UUID

if TYPE_CHECKING:
    from betconnect.resources import SelectionsForMarket

# "https://stackoverflow.com/questions/19989481/how-to-determine-if-a-string-is-a-valid-v4-uuid"
def is_valid_uuid(uuid_to_test, version=4):
    """
    Check if uuid_to_test is a valid UUID.

     Parameters
    ----------
    uuid_to_test : str
    version : {1, 2, 3, 4}

     Returns
    -------
    `True` if uuid_to_test is a valid UUID, otherwise `False`.

     Examples
    --------
    >>> is_valid_uuid('c9bf9e57-1685-4c89-bafb-ff5af830be8a')
    True
    >>> is_valid_uuid('c9bf9e58')
    False
    """

    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test


def calculate_book_percentage(market_selections: List[SelectionsForMarket]) -> float:
    """
    Calculates the book % for a given market and runner
    :param List[SelectionsForMarket] market_selections: List of available selections for the market
    :return: A float value. Anything close to 1.0 is good. Anything 1.1-1.15 is a large markup
    """

    book_value = 0
    for selection in market_selections:
        if selection.trading_status == "Trading":
            if selection.max_price:
                if selection.max_price > 1.01:
                    book_value += 1 / selection.max_price
    return round(book_value, 3)


def parse_bet_request_id(bet_request_id: Union[str, UUID]) -> UUID:
    """
    Parses a string or UUID to a UUID
    :param bet_request_id: a string or UUID
    :return: a UUID valid for a bet_request_id
    """
    if isinstance(bet_request_id, UUID):
        return bet_request_id
    elif isinstance(bet_request_id, str):
        return UUID(bet_request_id)


def create_cheap_hash(txt: str, length: int = 15) -> str:
    # This is just a hash for debugging purposes.
    #    It does not need to be unique, just fast and short.
    # https://stackoverflow.com/questions/14023350
    hash_ = hashlib.sha1()
    hash_.update(txt.encode())
    return hash_.hexdigest()[:length]
