from sqlalchemy import Column, ForeignKey, Integer

from app.core.database import Base


class Booking(Base):
    __tablename__ = "event_bookings"
    id = Column(Integer, primary_key=True)
    hold_id = Column(Integer, ForeignKey("event_holds.id"))
