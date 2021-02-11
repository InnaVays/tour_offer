import random

def generate_offer(hotels, excursions):
    """
    Generates a travel offer using the best discount strategy.
    
    Args:
        hotels (list): List of available hotel offers.
        excursions (list): List of available excursions.
    
    Returns:
        dict: A travel offer hptel+excursion.
    """
    if not hotels or not excursions:
        return {}

    # Select the hotel with the highest discount
    best_hotel = max(hotels, key=lambda h: h["discount"])

    # Select the most affordable excursion to complement the best-discounted hotel
    best_excursion = min(excursions, key=lambda e: e["price"])

    return {
        "hotel": {
            "name": best_hotel["hotel_name"],
            "final_price": best_hotel["final_price"],
            "discount": best_hotel["discount"],
            "currency": best_hotel["currency"]
        },
        "excursion": {
            "name": best_excursion["name"],
            "duration_hours": best_excursion["duration_hours"],
            "price": best_excursion["price"]
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
