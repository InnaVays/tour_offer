import requests
import random
import time
from config import EVENT_COLLECTOR_URL, MODE

if MODE != "SIMULATION":
    raise RuntimeError("User Simulator should only run in SIMULATION mode!")

# Conversion probabilities per strategy
CONVERSION_RATES = {
    "strategy_0": {"clicks": 0.10, "interest": 0.02, "session_length": 120},
    "strategy_A": {"clicks": 0.11, "interest": 0.05, "session_length": 140},
    "strategy_B": {"clicks": 0.20, "interest": 0.08, "session_length": 160},
    "strategy_C": {"clicks": 0.05, "interest": 0.01, "session_length": 100}
}

STRATEGIES = list(CONVERSION_RATES.keys())
EVENTS = ["click", "email", "request_call"]

def simulate_user_activity():
    """
        Generates simulated user behavior based on conversion rates.
    """
    
    for _ in range(2000):  # Simulate n users
        session_id = f"S{random.randint(1000, 9999)}"
        user_id = f"U{random.randint(1000, 9999)}"
        strategy = random.choice(STRATEGIES)
        start_time = time.time()

        # Simulate clicks
        if random.random() < CONVERSION_RATES[strategy]["clicks"]:
            requests.post(EVENT_COLLECTOR_URL, json={"user_id": user_id, "session_id": session_id, "strategy": strategy, "event_type": "click", "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")})

        # Simulate interest actions (email or request call)
        if random.random() < CONVERSION_RATES[strategy]["interest"]:
            event_type = random.choice(EVENTS[1:])  # Either "email" or "request_call"
            requests.post(EVENT_COLLECTOR_URL, json={"user_id": user_id, "session_id": session_id, "strategy": strategy, "event_type": event_type, "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")})

        # Simulate session length
        session_length = CONVERSION_RATES[strategy]["session_length"] + random.randint(-20, 20)
        time.sleep(session_length / 1000)  # Simulate session duration

if __name__ == "__main__":
    simulate_user_activity()
