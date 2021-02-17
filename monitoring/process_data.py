import sqlite3
import pandas as pd
from datetime import datetime

DB_PATH = "database/user_events.db"
CSV_OUTPUT_PATH = "data/processed_experiment_results.csv"

def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM user_events", conn)
    conn.close()
    return df

def process_user_events():

    df = load_data()

    if df.empty:
        print("⚠️ No data available in user_events.db")
        return

    # Convert timestamp to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    high_interest_events = ["email", "request_call", 'message_operator', 'book']

    grouped = df.groupby("session_id")

    user_id = grouped["user_id"].first()
    strategy = grouped["strategy"].first()

    clicks = grouped["event_type"].apply(lambda x: (x == "click").sum())

    high_interest = grouped["event_type"].apply(lambda x: x.isin(high_interest_events).sum())

    session_length = grouped["timestamp"].agg(lambda x: (x.max() - x.min()).total_seconds())

    summary = pd.DataFrame({
        "session_id": grouped.size().index,  
        "user_id": user_id,
        "strategy": strategy,
        "clicks": clicks,
        "high_interest": high_interest,
        "session_length": session_length
    })

    # Save to CSV
    summary.to_csv(CSV_OUTPUT_PATH, index=False)


if __name__ == "__main__":
    process_user_events()
