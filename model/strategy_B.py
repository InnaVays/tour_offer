import random

def generate_offer(hotels, excursions):
    """
    Generates travel offers using the best discount strategy.
    
    Args:
        hotels (list): List of available hotel offers.
        excursions (list): List of available excursions.
    
    Returns:
        list: A list of travel offers, each containing a hotel and an excursion.
    """
    if not hotels or not excursions:
        return []

    # Sort hotels by the highest discount percentage
    hotels_sorted = sorted(hotels, key=lambda h: h["discount"], reverse=True)[:3]

    # Sort excursions by the lowest price (to complement high-discount hotels)
    excursions_sorted = sorted(excursions, key=lambda e: e["price"])[:3]

    offers = []
    for i in range(len(hotels_sorted)):
        offer = {
            "hotel": {
                "name": hotels_sorted[i]["hotel_name"],
                "final_price": hotels_sorted[i]["final_price"],
                "discount": hotels_sorted[i]["discount"],
                "currency": hotels_sorted[i]["currency"]
            },
            "excursion": {
                "name": excursions_sorted[i]["name"],
                "duration_hours": excursions_sorted[i]["duration_hours"],
                "price": excursions_sorted[i]["price"]
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
