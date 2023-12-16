from sqlalchemy import create_engine, Engine, URL
from sqlalchemy.orm import sessionmaker, Session

from EntryPoint.Config import secrets, config_base


def get_engine() -> Engine:
    url = URL.create(
        drivername="postgresql",
        username=secrets.db_username,
        password=secrets.db_password,
        host=config_base.db_host,
        port=config_base.db_port,
        database=config_base.db_table
    )
    return create_engine(url)


def get_db_session() -> Session:
    session = sessionmaker(bind=get_engine())
    return session()
