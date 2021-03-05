import time
from simulation.user_simulator import simulate_user_activity

def run_fast_simulation(num_users=2000):

    print(f"Running test simulation: {num_users} users (1 user every 0.05 sec)...")

    for i in range(num_users):
        simulate_user_activity()
        time.sleep(0.05)  # Simulate a fast-paced user flow

    print("Test simulation completed.")

if __name__ == "__main__":
    run_fast_simulation()
