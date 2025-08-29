from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Hold(Base):
    __tablename__ = "event_holds"
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    seats_held = Column(Integer)
    payment_token = Column(String, unique=True)
    expires_at = Column(DateTime)

    event = relationship("Event", back_populates="holds")
