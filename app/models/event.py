from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    seats = Column(Integer)
    created_at = Column(DateTime)
    holds = relationship("Hold", back_populates="event")
