import ssl

import toml
from pymongo import MongoClient

DATABASE_CONNECTION_STRING = toml.load(
    "config.toml")["database"]["connection_string"]


def get_client() -> MongoClient:
    # FIXME ssl.CERT_NONE must be removed on production
    return MongoClient(DATABASE_CONNECTION_STRING, ssl_cert_reqs=ssl.CERT_NONE)
