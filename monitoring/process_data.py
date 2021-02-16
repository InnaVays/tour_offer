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

def process_data(df):
    if df.empty:
        print("No data found in the database.")
        return pd.DataFrame()

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    session_duration = df.groupby(["session_id"])["timestamp"].agg(["min", "max"])
    session_duration["session_length"] = (session_duration["max"] - session_duration["min"]).dt.total_seconds()
    session_duration = session_duration[["session_length"]]


    df_summary = df_summary.merge(session_duration, on="session_id", how="left")

    return df_summary

def save_csv(df):
    if not df.empty:
        df.to_csv(CSV_OUTPUT_PATH, index=False)
        print(f"Processed data saved to {CSV_OUTPUT_PATH}")

if __name__ == "__main__":
    raw_data = load_data()
    processed_data = process_data(raw_data)
    save_csv(processed_data)
