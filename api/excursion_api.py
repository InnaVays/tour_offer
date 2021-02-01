import json
from flask import Flask, jsonify
from config import MODE, MOCK_EXCURSIONS_FILE, PROD_EXCURSIONS_FILE

# Path to private excursions dataset
MOCK_EXCURSIONS_FILE = "data/mock_excursions.json"

def get_excursions(city):
    """
        Fetch excursions from private database (PRODUCTION) or mock data (SIMULATION).
    """
    
    file_path = PROD_EXCURSIONS_FILE if MODE == "PRODUCTION" else MOCK_EXCURSIONS_FILE

    with open(file_path, "r") as file:
        return jsonify(json.load(file))

    return [
        {
            "excursion_id": excursion["excursion_id"],
            "city": excursion["city"],
            "name": excursion["name"],
            "duration_hours": excursion["duration_hours"],
            "price": excursion["price"]
        }
        for excursion in all_excursions if excursion["city"].lower() == city.lower()
    ]

# Example Usage
if __name__ == "__main__":
    city = "Paris"
    excursions = get_excursions(city, MOCK_EXCURSIONS_FILE)

    if excursions:
        print(f"Excursions available in {city}:")
        for ex in excursions:
            print(f"{ex['name']} | Duration: {ex['duration_hours']}h | Price: {ex['price']} USD")
    else:
        print(f"No excursions found for {city}.")
