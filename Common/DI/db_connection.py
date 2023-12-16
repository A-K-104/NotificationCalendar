from sqlalchemy import create_engine, Engine, URL
from sqlalchemy.orm import sessionmaker, Session

from Common.Utiles import secrets
from EntryPoint.Config import config


def get_engine() -> Engine:
    url = URL.create(
        drivername="postgresql",
        username=secrets.db_username,
        password=secrets.db_password,
        host=config.db_host,
        port=config.db_port,
        database=config.db_table
    )
    return create_engine(url)


def get_db_session() -> Session:
    session = sessionmaker(bind=get_engine())
    return session()
