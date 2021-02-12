from flask import Flask, request, jsonify
import sqlite3
import time

DB_PATH = "database/user_events.db"

# Initialize Flask app
app = Flask(__name__)

def setup_database():
    """
        Creates the user events database table if it doesn't exist.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_events (
            user_id TEXT,
            session_id TEXT,
            event_type TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    setup_database()
    app.run(debug=True, port=5004)
