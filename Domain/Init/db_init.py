from Common.Utiles.config import Base
from EntryPoint.Config import db_connection


def create_db():
    Base.metadata.create_all(db_connection.get_engine())
