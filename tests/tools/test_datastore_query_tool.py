import json
import os


def get_datastore_config():
    datastore = {}
    with open(os.path.join("tests", "data", "test_datastore.json")) as f:
        datastore = json.load(f)
    return datastore


def test_datastore_query_tool():
    datastore = get_datastore_config()
    