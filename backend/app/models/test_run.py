from sqlalchemy import Column, Integer, String
from app.db.base import Base

class TestRun(Base):
    __tablename__ = "test_runs"

    id = Column(Integer, primary_key=True)
    test_name = Column(String)
    status = Column(String)