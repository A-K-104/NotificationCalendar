from datetime import datetime


class SchedulerMappingDTO:

    def __init__(self,
                 element_id: int,
                 cron_date,
                 event_id: int,
                 cron_id: str,
                 created_on: datetime
                 ):
        self.element_id = element_id
        self.cron_date = cron_date
        self.event_id = event_id
        self.cron_id = cron_id
        self.created_on = created_on

    def to_dict(self):
        return {
            "element_id": self.element_id,
            "cron_date": self.cron_date,
            "event_id": self.event_id,
            "cron_id": self.cron_id,
            "created_on": self.created_on
        }
