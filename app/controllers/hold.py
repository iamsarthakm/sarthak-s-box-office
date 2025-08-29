import uuid
from datetime import datetime, timedelta

from cachetools import TTLCache
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.event import Event
from app.models.hold import Hold
from app.schemas import CreateHoldRequest, GenericApiResponseWrapper

router = APIRouter()

hold_cache = TTLCache(maxsize=100, ttl=60 * 60 * 24)


@router.post(
    "/hold/",
    description="Create Hold",
    status_code=status.HTTP_200_OK,
)
async def create_hold(payload: CreateHoldRequest, db: Session = Depends(get_db)):
    payment_token = str(uuid.uuid4())
    # check if the event has enough seats left

    event = (
        db.query(Event).filter(Event.id == payload.event_id).with_for_update().first()
    )
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found",
        )
    if event.seats < payload.qty:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Event does not have enough seats left",
        )

    event.seats -= payload.qty
    hold = Hold(
        seats_held=payload.qty,
        event_id=payload.event_id,
        payment_token=payment_token,
        expires_at=datetime.now() + timedelta(minutes=2),
    )

    db.add(hold)
    db.commit()
    db.refresh(hold)
    hold_response = {
        "id": hold.id,
        "payment_token": hold.payment_token,
        "expires_at": hold.expires_at,
    }
    return GenericApiResponseWrapper(success=True, data=hold_response)
