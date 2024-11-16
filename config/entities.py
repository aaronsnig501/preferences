from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    uri: str

@dataclass
class Config:
    database: DatabaseConfig
