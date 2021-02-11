import random

def generate_offer(hotels, excursions):
    """
    Generates a travel offer with the lowest price .
    
    Args:
        hotels (list): List of available hotel offers.
        excursions (list): List of available excursions.
    
    Returns:
        dict: A travel offer hptel+excursion.
    """
    if not hotels or not excursions:
        return {}

    # Select the cheapest hotel
    cheapest_hotel = min(hotels, key=lambda h: h["final_price"])

    # Select an affordable excursion that pairs well with a budget-friendly trip
    matching_excursion = min(excursions, key=lambda e: e["price"])

    return {
        "hotel": {
            "name": cheapest_hotel["hotel_name"],
            "final_price": cheapest_hotel["final_price"],
            "discount": cheapest_hotel["discount"],
            "currency": cheapest_hotel["currency"]
        },
        "excursion": {
            "name": matching_excursion["name"],
            "duration_hours": matching_excursion["duration_hours"],
            "price": matching_excursion["price"]
        }
    }

# Example Usage
if __name__ == "__main__":
    # Sample Data for Testing
    mock_hotels = [
        {"hotel_name": "Hotel A", "final_price": 800, "discount": 20, "currency": "USD"},
        {"hotel_name": "Hotel B", "final_price": 600, "discount": 15, "currency": "USD"},
        {"hotel_name": "Hotel C", "final_price": 1000, "discount": 10, "currency": "USD"},
    ]

    mock_excursions = [
        {"name": "Exc A", "duration_hours": 3, "price": 50},
        {"name": "Exc B", "duration_hours": 2, "price": 70},
        {"name": "Exc C", "duration_hours": 1.5, "price": 40},
    ]

    print(generate_offer(mock_hotels, mock_excursions))