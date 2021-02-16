import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

DB_PATH = "database/user_events.db"

@st.cache_data
def load_data():
    """
        Load user interaction data from the SQLite database.
    """
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM user_events", conn)
    conn.close()
    return df

# Load data
df = load_data()

# Sidebar Filters
st.sidebar.title("Experiment Filters")
selected_strategy = st.sidebar.selectbox("Filter by Strategy", ["All"] + df["strategy"].unique().tolist())

if selected_strategy != "All":
    df = df[df["strategy"] == selected_strategy]

# Calculate Metrics
strategy_summary = df.groupby("strategy")["event_type"].value_counts().unstack(fill_value=0)

# Clicks on Offer per Strategy
clicks_df = strategy_summary.get("click", pd.Series(dtype=int)).reset_index()
clicks_df.columns = ["Strategy", "Clicks"]

# Interest per Strategy (email OR request a call)
df["interest"] = df["event_type"].apply(lambda x: 1 if x in ["email", "request_call"] else 0)
interest_df = df.groupby("strategy")["interest"].sum().reset_index()
interest_df.columns = ["Strategy", "Interest"]

# Display Metrics
st.title("Travel Offer Experiment Dashboard")

st.subheader("Clicks on Offer per Strategy")
fig_clicks = px.bar(clicks_df, x="Strategy", y="Clicks", title="Clicks on Offer by Strategy")
st.plotly_chart(fig_clicks)

st.subheader("Interest (Email or Call Request) per Strategy")
fig_interest = px.bar(interest_df, x="Strategy", y="Interest", title="User Interest by Strategy")
st.plotly_chart(fig_interest)

st.subheader("User Event Logs")
st.dataframe(df)
