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

@app.route('/api/collect-event', methods=['POST'])
def collect_event():
    """
        API to collect user interactions.
    """
    data = request.json
    user_id = data.get("user_id")
    session_id = data.get("session_id")
    event_type = data.get("event_type")
    timestamp = data.get("timestamp", time.strftime("%Y-%m-%d %H:%M:%S"))

    if not user_id or not session_id or not event_type:
        return jsonify({"error": "Missing required fields"}), 400

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_events VALUES (?, ?, ?, ?)", 
                   (user_id, session_id, event_type, timestamp))
    conn.commit()
    conn.close()

    return jsonify({"message": "Event logged successfully"}), 200

if __name__ == '__main__':
    setup_database()
    app.run(debug=True, port=5004)
