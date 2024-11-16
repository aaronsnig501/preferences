from os import environ
from .entities import Config, DatabaseConfig


def load_config():
    db_config: DatabaseConfig = DatabaseConfig(
        uri=environ["MARIA_DB_URI"]
    )
    return Config(database=db_config)
