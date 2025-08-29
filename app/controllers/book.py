from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.book import Booking
from app.models.hold import Hold
from app.schemas import BookRequest, GenericApiResponseWrapper

router = APIRouter()


@router.post("/", description="Book", status_code=status.HTTP_200_OK)
async def book(payload: BookRequest, db: Session = Depends(get_db)):
    hold = (
        db.query(Hold)
        .filter(Hold.id == payload.hold_id)
        .with_for_update()
        .first()
    )
    if not hold:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hold not found",
        )
    if hold.expires_at < datetime.now():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Hold expired",
        )
    if hold.payment_token != payload.payment_token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid payment token",
        )

    check_hold = db.query(Booking).filter(Booking.hold_id == payload.hold_id).first()
    if check_hold:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Hold already booked",
        )

    booking = Booking(
        hold_id=hold.id,
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)
    booking_response = {
        "id": booking.id,
    }
    return GenericApiResponseWrapper(success=True, data=booking_response)
