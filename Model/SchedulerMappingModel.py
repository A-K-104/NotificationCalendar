from Common.Entities.SchedulerMapping import SchedulerMapping
from Common.Exceptions.NotFoundException import NotFoundException
from Common.decorators.db_session_decorator import with_db_session_decorator
from Common.decorators.to_dto_decorator import to_dto_decorator
from Model.ModelBase import ModelBase


class SchedulerMappingModel(ModelBase):
    def __init__(self):
        super().__init__(SchedulerMapping)

    @with_db_session_decorator
    @to_dto_decorator
    def get_by_event_id(self, session, event_id: str):
        scheduler_mappings = session.query(SchedulerMapping).filter_by(event=event_id).all()
        if scheduler_mappings is not None:
            return scheduler_mappings
        raise NotFoundException
