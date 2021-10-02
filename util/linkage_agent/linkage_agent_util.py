from pymongo import MongoClient
import validate as val
import match as m


def validate(config):
    val.validate(config)


def drop(config):
    client = MongoClient(config.mongo_uri)
    database = client.linkage_agent
    database.match_groups.drop()
    database.household_match_groups.drop()
    print("Database cleared.")


def match(config):
    m.match(config)