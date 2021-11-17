import json
from datetime import datetime
import pickle
from typing import List
from betconnect import resources as bc_resources

def json_converter(o):
    if isinstance(o,datetime):
        return o.isoformat()

def dump_to_json(file_path, data):
    with open(file_path, 'a') as f:
        json.dump(data, f, default=json_converter)


def calculate_book_percentage(market_selections: List[bc_resources.SelectionsForMarket]):
    book_value = 0
    for selection in market_selections:
        if selection.trading_status == 'Trading':
            if selection.max_price:
                if selection.max_price > 1.01:
                    book_value += (1/selection.max_price)
    return book_value
