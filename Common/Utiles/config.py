from sqlalchemy.orm import declarative_base


Base = declarative_base()

from BL.SchedulerBL import SchedulerBL
scheduler_bl = SchedulerBL()

