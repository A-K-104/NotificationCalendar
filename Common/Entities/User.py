from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from Common.Utiles.config import Base


class User(Base):
    __tablename__ = 'user'  # todo: add to config
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False, unique=True)
    role = Column(String(100), nullable=False)
    events = relationship('Event', backref='user_backref')
    created_on = Column(DateTime(), default=datetime.now)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role,
            'created_on': self.created_on.isoformat() if self.created_on else None
        }
