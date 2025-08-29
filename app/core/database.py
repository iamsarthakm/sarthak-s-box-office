import sqlite3

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./boxoffice.db"

Base = declarative_base()

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # needed for FastAPI threads
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    with SessionLocal() as db:
        yield db


def init_db():
    """Initialize database and create all tables"""
    # Import all models to ensure they are registered with Base
    # These imports are needed to register models with Base.metadata
    # noqa: F401 - these imports are required for SQLAlchemy model registration
    import app.models.book  # noqa: F401
    import app.models.event  # noqa: F401
    import app.models.hold  # noqa: F401

    # Create all tables
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully!")
    print("All tables created automatically!")


def execute_query(query, params=None):
    """Execute a SQL query and return results"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        if query.strip().upper().startswith("SELECT"):
            return cursor.fetchall()
        else:
            conn.commit()
            return cursor.rowcount


def get_db_connection():
    """Get a SQLite database connection"""
    return sqlite3.connect("./boxoffice.db")


def init_db_old():
    """Initialize the SQLite database file"""
    db_path = "./boxoffice.db"
    # Create the database file if it doesn't exist
    conn = sqlite3.connect(db_path)
    conn.close()
    print(f"SQLite database initialized at: {db_path}")
