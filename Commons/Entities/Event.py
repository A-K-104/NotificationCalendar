from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from Commons.Utiles.config import Base


class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    date = Column(DateTime(), nullable=False)
    organizer = Column(Integer, ForeignKey('user.id'))
    guests = Column(String(100))
    location = Column(String(255))
    venue = Column(Integer, ForeignKey('venue.id'))
    link = Column(String(255))
    notifications = Column(String(100))
    description = Column(String(255))
    created_on = Column(DateTime(), default=datetime.now)
