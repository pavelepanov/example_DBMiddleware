from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def create_db_engine(settings: str) -> Engine:
    return create_engine(settings)