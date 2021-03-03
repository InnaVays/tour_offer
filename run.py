import argparse
import os

def set_mode(mode):
    """Dynamically update config.py to set the experiment mode."""
    with open("config.py", "r") as file:
        lines = file.readlines()

    with open("config.py", "w") as file:
        for line in lines:
            if line.startswith("MODE = "):
                file.write(f"MODE = \"{mode}\"\n")
            else:
                file.write(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Travel Offer Experiment")
    parser.add_argument("--simulation", action="store_true", help="Run in simulation mode")
    parser.add_argument("--production", action="store_true", help="Run in production mode")
    args = parser.parse_args()

    if args.simulation:
        set_mode("SIMULATION")
        print("Running in SIMULATION mode...")
        os.system("python simulation/user_simulator.py")
    elif args.production:
        set_mode("PRODUCTION")
        print("Running in PRODUCTION mode...")
        print("Ensure real data sources are connected!")
    else:
        print("Please specify --simulation or --production")
