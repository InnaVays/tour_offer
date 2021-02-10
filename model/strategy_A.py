import random

def generate_offer(hotels, excursions):
    """
    Generates travel offers using a random selection strategy.
    
    Args:
        hotels (list): List of available hotel offers.
        excursions (list): List of available excursions.
    
    Returns:
        list: A list of travel offers, each containing a hotel and an excursion.
    """
    if not hotels or not excursions:
        return []

    selected_hotels = random.sample(hotels, min(3, len(hotels)))
    selected_excursions = random.sample(excursions, min(3, len(excursions)))

    offers = []
    for i in range(len(selected_hotels)):
        offer = {
            "hotel": {
                "name": selected_hotels[i]["hotel_name"],
                "final_price": selected_hotels[i]["final_price"],
                "discount": selected_hotels[i]["discount"],
                "currency": selected_hotels[i]["currency"]
            },
            "excursion": {
                "name": selected_excursions[i]["name"],
                "duration_hours": selected_excursions[i]["duration_hours"],
                "price": selected_excursions[i]["price"]
            }
        }
        offers.append(offer)

    return offers

# Example Usage
if __name__ == "__main__":
    # Sample Data for Testing
    mock_hotels = [
        {"hotel_name": "Hotel A", "final_price": 800, "discount": 20, "currency": "USD"},
        {"hotel_name": "Hotel B", "final_price": 600, "discount": 15, "currency": "USD"},
        {"hotel_name": "Hotel C", "final_price": 1000, "discount": 10, "currency": "USD"},
    ]

    mock_excursions = [
        {"name": "Louvre Tour", "duration_hours": 3, "price": 50},
        {"name": "Eiffel Tower VIP", "duration_hours": 2, "price": 70},
        {"name": "Seine River Cruise", "duration_hours": 1.5, "price": 40},
    ]

    print(generate_offer(mock_hotels, mock_excursions))
