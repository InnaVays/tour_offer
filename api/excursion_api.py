import json

# Path to private excursions dataset
MOCK_EXCURSIONS_FILE = "data/mock_excursions.json"

def get_excursions(city, EXCURSIONS_JSON=MOCK_EXCURSIONS_FILE):
    """
        Fetches excursions for a given city (safe for simulations).
    """
    try:
        with open(EXCURSIONS_JSON, "r") as file:
            all_excursions = json.load(file)
    except FileNotFoundError:
        print(f"Error: {EXCURSIONS_JSON} not found.")
        return []

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
