from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from Commons.Utiles.config import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False, unique=True)
    role = Column(String(100), nullable=False)
    events = relationship('Event', backref='user_backref')
    created_on = Column(DateTime(), default=datetime.now)

    @staticmethod
    def create(session, username, role):
        new_user = User(username=username, role=role)
        session.add(new_user)
        session.commit()
        return new_user

    def update(self, session, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        session.commit()
