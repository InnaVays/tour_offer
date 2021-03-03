import argparse
import config

def set_mode(mode):
    """Dynamically set mode in config.py"""
    with open("config.py", "r") as file:
        lines = file.readlines()

    with open("config.py", "w") as file:
        for line in lines:
            if line.startswith("MODE = "):
                file.write(f"MODE = \"{mode}\"\n")
            else:
                file.write(line)

if __name__ == "__main__":

    if args.simulation:
        set_mode("SIMULATION")
        print("Running in SIMULATION mode...")
    elif args.production:
        set_mode("PRODUCTION")
        print("Running in PRODUCTION mode...")
    else:
        print("⚠️ Please specify --simulation or --production")