from uuid import uuid1 as generate_uuid

from BL.NotifierBL import NotifierBL
from Common.Utiles.config import scheduler
from Model.EventModel import EventModel
from Model.SchedulerMappingModel import SchedulerMappingModel


class SchedulerBL:

    def __init__(self):
        self.scheduler = scheduler
        self.scheduler_mapping_model = SchedulerMappingModel()
        self.scheduler_mapping_model = SchedulerMappingModel()
        self.event_model = EventModel()

    def create_one(self, run_date, event_id: str):
        job_id = generate_uuid()
        scheduler_mapping = self.scheduler_mapping_model.create_one(cron_date=run_date, event=event_id,
                                                                    cron_id=str(job_id))

        self.scheduler.add_job(SchedulerBL.execute, args=[self, scheduler_mapping.el_id], run_date=run_date,
                               id=str(job_id))

    def delete_one(self, event):

        scheduler_mapping: list = self.scheduler_mapping_model.get_by_event_id(event.el_id)

        for mapping in scheduler_mapping:
            job = self.scheduler.get_job(mapping.cron_id)
            if job.run_date == mapping.date:
                self.scheduler.remove_job(mapping.cron_id)

    def execute(self, scheduler_mapping_id: int):
        scheduler_mapp = self.scheduler_mapping_model.get_one(scheduler_mapping_id)
        self.scheduler_mapping_model.delete_one(scheduler_mapping_id)

        event = self.event_model.get_one(scheduler_mapp.event_id)
        NotifierBL.notify(event)
