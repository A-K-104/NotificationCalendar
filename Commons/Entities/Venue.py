from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from Commons.Utiles.config import Base


class Venue(Base):
    __tablename__ = 'venue'
    id = Column(Integer, primary_key=True)
    room_name = Column(String(255), nullable=False, unique=True)
    notes = Column(String(255), nullable=True)
    events = relationship('Event', backref='venue_backref')
    created_on = Column(DateTime(), default=datetime.now)
