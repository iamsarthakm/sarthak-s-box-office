from datetime import datetime

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.event import Event
from app.schemas import CreateEvent, CreateEventResponse, GenericApiResponseWrapper

router = APIRouter()


@router.post(
    "/",
    description="Create Event",
    status_code=status.HTTP_200_OK,
)
async def create_event(event: CreateEvent, db: Session = Depends(get_db)):
    event = Event(name=event.name, seats=event.seats, created_at=datetime.now())
    db.add(event)
    db.commit()
    return GenericApiResponseWrapper(
        success=True,
        data=CreateEventResponse(id=event.id, name=event.name, seats=event.seats),
    )


@router.get(
    "/",
    description="Get Events",
    status_code=status.HTTP_200_OK,
)
async def get_events(db: Session = Depends(get_db)):
    events = db.query(Event).all()
    return GenericApiResponseWrapper(success=True, data=events)
