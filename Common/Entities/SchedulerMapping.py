from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from Common.Utiles.config import Base as sqlAlchemyEntityBase


class SchedulerMapping(sqlAlchemyEntityBase):
    __tablename__ = 'scheduler_mapping'
    id = Column(Integer, primary_key=True)
    cron_date = Column(DateTime(), nullable=False)
    event = Column(Integer, ForeignKey('event.id'), nullable=False)
    cron_id = Column(String, nullable=False)
    created_on = Column(DateTime(), default=datetime.now)

    def to_dto(self):
        from Common.Extensions.dto_extensions import scheduler_mapping_to_dto
        return scheduler_mapping_to_dto(self)
