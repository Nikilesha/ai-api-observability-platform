from app.db.session import engine
from app.db.base import Base

from app.models.user import User
from app.models.test_run import TestRun
from app.models.metric import Metric
from app.models.logs import Log

Base.metadata.create_all(bind=engine)

print("Tables created")