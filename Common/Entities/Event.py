from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from Common.Utiles.config import Base as sqlAlchemyEntityBase


class Event(sqlAlchemyEntityBase):
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

    def to_dto(self):
        from Common.Extensions.dto_extensions import event_to_dto
        return event_to_dto(self)
