from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    status = Column(String, default="open")
    source = Column(String, default="operator")
    created_at = Column(DateTime, default=datetime.utcnow)
