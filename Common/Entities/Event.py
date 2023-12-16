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

    # todo: organizer=user_id,

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'date': self.date,
            'organizer': self.organizer,
            'guests': self.guests,
            'location': self.location,
            'venue': self.venue,
            'link': self.link,
            'notifications': self.notifications,
            'description': self.description,
            'created_on': self.created_on.isoformat() if self.created_on else None
        }
