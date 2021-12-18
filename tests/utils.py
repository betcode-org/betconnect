import json
import pickle
import os

# noinspection SpellCheckingInspection
basepath = os.path.dirname(__file__)


def build_path(path):
    return basepath + "/" + path


def save_json_to_file(file_location, data):
    with open(file_location, "w") as f:
        json.dump(data, f)


def save_data_to_pickle_file(file_location, data):
    with open(file_location, "wb") as f:
        pickle.dump(data, f)


def load_json(file_name):
    with open(file_name, "r") as f:
        data = f.read()
        return json.loads(data)


def load_pickle(file_name):
    with open(file_name, "rb") as f:
        data = f.read()
        return pickle.loads(data)
