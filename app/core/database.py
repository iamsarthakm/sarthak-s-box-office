import sqlite3

from .config import Config


def get_db_connection():
    """Get a SQLite database connection"""
    return sqlite3.connect(Config.DATABASE_PATH)


def init_db():
    """Initialize the SQLite database file"""
    db_path = Config.DATABASE_PATH
    db_path.parent.mkdir(exist_ok=True)

    # Create the database file if it doesn't exist
    conn = sqlite3.connect(db_path)
    conn.close()
    print(f"SQLite database initialized at: {db_path}")


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
