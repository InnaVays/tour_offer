import requests
import random
import time
import numpy as np
from config import EVENT_COLLECTOR_URL, MODE

if MODE != "SIMULATION":
    raise RuntimeError("User Simulator should only run in SIMULATION mode!")

# Conversion probabilities per strategy
METRIC_DISTRIBUTION = {
    "strategy_0": {"clicks": 0.10, "interest": 0.02, "session_length": 120},
    "strategy_A": {"clicks": 0.11, "interest": 0.05, "session_length": 140},
    "strategy_B": {"clicks": 0.20, "interest": 0.08, "session_length": 160},
    "strategy_C": {"clicks": 0.05, "interest": 0.01, "session_length": 100}
}

STRATEGIES = list(METRIC_DISTRIBUTION.keys())
EVENTS = ["click", "email", "request_call"]

def simulate_user_activity():
    """
    Generates simulated ONE user behavior using normal distributions.
    """

    session_id = f"S{random.randint(1000, 9999)}"
    user_id = f"U{random.randint(1000, 9999)}"
    strategy = random.choice(STRATEGIES)

    # Sample from normal distributions (ensuring non-negative values)
    clicks = max(0, int(np.random.normal(*METRIC_DISTRIBUTION[strategy]["clicks"])))  
    interest = max(0, int(np.random.normal(*METRIC_DISTRIBUTION[strategy]["interest"])))  
    session_length = max(1, int(np.random.normal(*METRIC_DISTRIBUTION[strategy]["session_length"])))  

    #start_time = time.time()
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")

    # Start Session Event
    requests.post(EVENT_COLLECTOR_URL, json={
        "user_id": user_id,
        "session_id": session_id,
        "strategy": strategy,
        "event_type": "start_session",
        "timestamp": formatted_time
    })

    # Simulate Click Events
    for _ in range(clicks):
        time.sleep(random.uniform(0.5, 2))  # Simulate delay between actions
        requests.post(EVENT_COLLECTOR_URL, json={
            "user_id": user_id,
            "session_id": session_id,
            "strategy": strategy,
            "event_type": "click",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })

    # Simulate Interest Events (email OR request_call)
    for _ in range(interest):
        time.sleep(random.uniform(1, 3))  # Simulate user decision delay
        event_type = random.choice(["email", "request_call", 'message_operator', 'book'])
        requests.post(EVENT_COLLECTOR_URL, json={
            "user_id": user_id,
            "session_id": session_id,
            "strategy": strategy,
            "event_type": event_type,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })

    # ⏳ Simulate session length by sleeping (optional for debugging)
    time.sleep(session_length / 1000)  

    # End Session Event
    requests.post(EVENT_COLLECTOR_URL, json={
        "user_id": user_id,
        "session_id": session_id,
        "strategy": strategy,
        "event_type": "end_session",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    })


if __name__ == "__main__":
    simulate_user_activity()
