import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

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

# Calculate Metrics
total_events = df.shape[0]
ctr = round(df[df["event_type"] == "click"].shape[0] / total_events * 100, 2) if total_events > 0 else 0
conversion_rate = round(df[df["event_type"] == "book"].shape[0] / total_events * 100, 2) if total_events > 0 else 0

# Sidebar Filters
st.sidebar.title("🔍 Experiment Filters")
selected_event = st.sidebar.selectbox("Filter by Event Type", ["All"] + df["event_type"].unique().tolist())

if selected_event != "All":
    df = df[df["event_type"] == selected_event]

# Display Metrics
st.title("📊 Travel Offer Experiment Dashboard")
st.metric("Total Events Logged", total_events)
st.metric("Click-Through Rate (CTR)", f"{ctr}%")
st.metric("Booking Rate", f"{conversion_rate}%")

# Event Distribution Chart
st.subheader("📈 Event Distribution")
fig_event = px.histogram(df, x="event_type", title="User Actions Distribution")
st.plotly_chart(fig_event)

# Display Data Table
st.subheader("📋 User Event Logs")
st.dataframe(df)

# Refresh every 30 seconds
st.experimental_rerun()
