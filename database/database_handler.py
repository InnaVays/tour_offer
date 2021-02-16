import sqlite3

DB_PATH = "database/user_events.db"

def setup_database():
    """Creates the database and the necessary tables if they don't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create table for storing user events
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_events (
            user_id TEXT,
            session_id TEXT,
            strategy TEXT,
            event_type TEXT,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
    print("Database initialized successfully.")
