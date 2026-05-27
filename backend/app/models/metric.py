from sqlalchemy import Column, Integer, Float
from app.db.base import Base

class Metric(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True)
    latency = Column(Float)