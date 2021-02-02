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

def simulate_user_activity(num_users=2000, simulation_speed = 1):
    """
        Generates simulated user behavior using normal distributions.
    """
    
    for _ in range(num_users):  
        session_id = f"S{random.randint(1000, 9999)}"
        user_id = f"U{random.randint(1000, 9999)}"
        strategy = random.choice(STRATEGIES)

        # Sample from normal distribution
        clicks = max(0, int(np.random.normal(METRIC_DISTRIBUTION[strategy]["clicks"])))  
        interest = max(0, int(np.random.normal(METRIC_DISTRIBUTION[strategy]["interest"])))  
        session_length = max(1, int(np.random.normal(METRIC_DISTRIBUTION[strategy]["session_length"])))  

        # Send Click events
        for _ in range(clicks):
            requests.post(EVENT_COLLECTOR_URL, json={"user_id": user_id, "session_id": session_id, "strategy": strategy, "event_type": "click", "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")})

        # Send Interest actions (email or request call)
        for _ in range(interest):
            event_type = random.choice(EVENTS[1:])  # Either "email" or "request_call"
            requests.post(EVENT_COLLECTOR_URL, json={"user_id": user_id, "session_id": session_id, "strategy": strategy, "event_type": event_type, "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")})

        # Simulate session duration
        time.sleep( simulation_speed )  # Simulate in seconds

if __name__ == "__main__":
    simulate_user_activity()
