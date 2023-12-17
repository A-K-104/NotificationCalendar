from datetime import datetime
from functools import wraps



def cron_date_passed(func):
    @wraps(func)
    def wrapper(self, job_id: str, run_date, element_id: int):
        if run_date < datetime.now():
            return self.execute(element_id)
        else:
            return func(self, job_id, run_date, element_id)

    return wrapper
