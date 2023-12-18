from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import declarative_base

Base = declarative_base()
scheduler = BackgroundScheduler()
scheduler.start()
