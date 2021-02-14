import pandas as pd
import sqlite3

DB_PATH = "database/user_events.db"

@st.cache_data
def load_data():
    """Load user interaction data from the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM user_events", conn)
    conn.close()
    return df

# Load data
df = load_data()