import json
from datetime import datetime
import pickle

def json_converter(o):
    if isinstance(o,datetime):
        return o.isoformat()

def dump_to_json(file_path, data):
    with open(file_path, 'a') as f:
        json.dump(data, f, default=json_converter)
