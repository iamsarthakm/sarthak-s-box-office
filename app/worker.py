import asyncio
from datetime import datetime

from app.core.database import SessionLocal
from app.models.book import Booking
from app.models.event import Event
from app.models.hold import Hold


async def release_expired_holds_worker():
    """Worker that periodically checks for expired holds and releases seats."""
    while True:
        db = SessionLocal()

        # Find expired holds
        print("Checking for expired holds")
        # query to get holds which are not in Book table and are expired
        expired_holds = (
            db.query(Hold)
            .filter(Hold.is_deleted == False)
            .filter(Hold.expires_at < datetime.now())
            .filter(Hold.id.notin_(db.query(Booking.hold_id).filter(Booking.hold_id != None)))  # noqa: E711
            .all()
        )

        for hold in expired_holds:
            # Release seats back to event
            event = db.query(Event).filter(Event.id == hold.event_id).first()
            if event:
                event.seats += hold.seats_held
                hold.is_deleted = True
                db.commit()
                db.refresh(hold)

                print(f"Released {hold.seats_held} seats for event {hold.event_id}")

        db.commit()

        await asyncio.sleep(5)
