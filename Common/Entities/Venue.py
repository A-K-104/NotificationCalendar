from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from Common.Utiles.config import Base


class Venue(Base):
    __tablename__ = 'venue'
    id = Column(Integer, primary_key=True)
    room_name = Column(String(255), nullable=False, unique=True)
    notes = Column(String(255), nullable=True)
    events = relationship('Event', backref='venue_backref')
    created_on = Column(DateTime(), default=datetime.now)

    @staticmethod
    def create(session, **kwargs):
        new_venue = Venue(**kwargs)
        session.add(new_venue)
        session.commit()
        return new_venue

    def update(self, session, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'room_name': self.room_name,
            'notes': self.notes,
            'created_on': self.created_on.isoformat() if self.created_on else None
        }
