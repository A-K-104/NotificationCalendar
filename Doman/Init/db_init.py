from Commons.DI import db_connection
from Commons.Utiles.config import Base


def create_db():
    Base.metadata.create_all(db_connection.get_engine())