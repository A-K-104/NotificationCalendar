from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from Common.Utiles.config import Base as sqlAlchemyEntityBase


class User(sqlAlchemyEntityBase):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False, unique=True)
    role = Column(String(100), nullable=False)
    events = relationship('Event', backref='user_backref')
    created_on = Column(DateTime(), default=datetime.now)

    def to_dto(self):
        from Common.Extensions.dto_extensions import user_to_dto
        return user_to_dto(self)
