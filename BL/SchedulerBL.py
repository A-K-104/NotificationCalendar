from uuid import uuid1 as generate_uuid

from BL.NotifierBL import NotifierBL
from Common.Utiles.config import scheduler
from Common.decorators.cron_date_passed import cron_date_passed
from Model.EventModel import EventModel
from Model.SchedulerMappingModel import SchedulerMappingModel


class SchedulerBL:

    def __init__(self):
        self.scheduler = scheduler
        self.scheduler_mapping_model = SchedulerMappingModel()
        self.event_model = EventModel()

        scheduler_mappings = self.scheduler_mapping_model.get_all()
        self.set_many(scheduler_mappings)

    def set_many(self, scheduler_mappings: list):
        for scheduler_map in scheduler_mappings:
            self.create_job(scheduler_map.cron_id, scheduler_map.cron_date, scheduler_map.element_id)

    def create_one(self, event_id: str, run_date):
        job_id = generate_uuid()
        scheduler_mapping = self.save_scheduler_in_db(event_id, job_id, run_date)

        self.create_job(str(job_id), run_date, scheduler_mapping.element_id)

    @cron_date_passed
    def create_job(self, job_id: str, run_date, element_id: int):
        self.scheduler.add_job(SchedulerBL.execute, args=[self, element_id], run_date=run_date,
                               id=str(job_id))

    def save_scheduler_in_db(self, event_id, job_id, run_date):
        return self.scheduler_mapping_model.create_one(cron_date=run_date, event=event_id,
                                                       cron_id=job_id)

    def delete_many(self, event_id: str):

        scheduler_mapping: list = self.scheduler_mapping_model.get_by_event_id(event_id)

        for mapping in scheduler_mapping:
            self.scheduler.remove_job(mapping.cron_id)
            self.scheduler_mapping_model.delete_one(mapping.element_id)

    def execute(self, scheduler_mapping_id: int):
        scheduler_mapp = self.scheduler_mapping_model.get_one(scheduler_mapping_id)
        self.scheduler_mapping_model.delete_one(scheduler_mapping_id)

        event = self.event_model.get_one(scheduler_mapp.event_id)
        NotifierBL.notify(event)
