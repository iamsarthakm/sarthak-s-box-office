import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.controllers.book import router as booking_router
from app.controllers.event import router as event_router
from app.controllers.hold import router as hold_router
from app.core.database import init_db
from app.core.log import setup_logger
from app.worker import release_expired_holds_worker

logger = setup_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database on startup
    logger.info("Starting application...")
    init_db()
    logger.info("Database initialized successfully!")

    # Start worker
    task = asyncio.create_task(release_expired_holds_worker())
    yield

    # On shutdown, cancel worker
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        pass


app = FastAPI(
    title="Sarthak'sBox Office APP API",
    lifespan=lifespan,
    default_response_class=JSONResponse,
    json_dumps_params={
        "ensure_ascii": False
    },  # Preserve Unicode characters in responses
)


# router for event, hold, booking (here router and controller are same)
app.include_router(event_router, prefix="/api/event", tags=["event"])
app.include_router(hold_router, prefix="/api/hold", tags=["hold"])
app.include_router(booking_router, prefix="/api/book", tags=["booking"])
