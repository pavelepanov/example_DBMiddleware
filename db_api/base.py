from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


def create_all(db_engine: Engine) -> None:
    Base.metadata.create_all(bind=db_engine)


def drop_all(db_engine: Engine) -> None:
    Base.metadata.drop_all(db_engine)