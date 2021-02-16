import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime

DB_PATH = "database/user_events.db"
CSV_OUTPUT_PATH = "data/processed_results.csv"

def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM user_events", conn)
    conn.close()
    return df

def process_user_events():

    df = load_data()

    if df.empty:
        print("No data available in user_events.db")
        return

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Define "high interest" events
    high_interest_events = ["email", "request_call", 'message_operator', 'book']

    summary = df.groupby("session_id").agg(
        user_id=("user_id", "first"),
        strategy=("strategy", "first"),
        clicks=("event_type", lambda x: (x == "click").sum()),
        high_interest=("event_type", lambda x: x.isin(high_interest_events).sum()),
        session_length=("timestamp", lambda x: (x.max() - x.min()).total_seconds())
    ).reset_index()

def save_csv(df):
    if not df.empty:
        df.to_csv(CSV_OUTPUT_PATH, index=False)
        print(f"Processed data saved to {CSV_OUTPUT_PATH}")

if __name__ == "__main__":
    raw_data = load_data()
    processed_data = process_data(raw_data)
    save_csv(processed_data)
