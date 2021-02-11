import random

def generate_offer(hotels, excursions):
    """
    Generates travel offer using a random selection strategy.
    
    Args:
        hotels (list): List of available hotel offers.
        excursions (list): List of available excursions.
    
    Returns:
        dict: A travel offer hptel+excursion.
    """
    if not hotels or not excursions:
        return []

    selected_hotel = random.sample(hotels, 1)
    selected_excursion = random.sample(excursions, 1)

    return {
            "hotel": {
                "name": selected_hotel["hotel_name"],
                "final_price": selected_hotel["final_price"],
                "discount": selected_hotel["discount"],
                "currency": selected_hotel["currency"]
            },
            "excursion": {
                "name": selected_excursion["name"],
                "duration_hours": selected_excursion["duration_hours"],
                "price": selected_excursion["price"]
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
