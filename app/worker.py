import asyncio
from datetime import datetime

from app.core.database import SessionLocal
from app.models.event import Event
from app.models.hold import Hold


async def release_expired_holds_worker():
    """Worker that periodically checks for expired holds and releases seats."""
    while True:
        db = SessionLocal()

        # Find expired holds
        print("Checking for expired holds")
        expired_holds = db.query(Hold).filter(Hold.expires_at < datetime.now()).all()

        for hold in expired_holds:
            # Release seats back to event
            event = db.query(Event).filter(Event.id == hold.event_id).first()
            if event:
                event.seats += hold.seats_held

            # Delete the expired hold
            db.delete(hold)

        db.commit()

        await asyncio.sleep(5)
