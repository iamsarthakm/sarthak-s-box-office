from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.core.config import Config
from app.core.database import execute_query, init_db
from app.core.log import setup_logger

logger = setup_logger(__name__)

app = FastAPI(
    title="Sarthak'sBox Office APP API",
    description="API for performing image analysis on cotton, rice, maize, chilli crops.",
    version="1.0.0",
    default_response_class=JSONResponse,
    json_dumps_params={
        "ensure_ascii": False
    },  # Preserve Unicode characters in responses
)


def main():
    print(f"Setting up {Config.APP_NAME}")

    # Initialize SQLite database
    init_db()

    # Test a simple query
    try:
        result = execute_query("SELECT sqlite_version()")
        print(f"SQLite version: {result[0][0]}")
        print("SQLite database is working!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
