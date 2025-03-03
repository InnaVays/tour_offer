import requests
import json
from flask import Flask, jsonify
from config import MODE, AMADEUS_API_HOTELS, AMADEUS_API_HOTEL_LIST, AMADEUS_API_AUTH, AMADEUS_API_KEY, AMADEUS_API_SECRET, MOCK_HOTELS_FILE


def get_access_token():
    """
        Obtain an access token from Amadeus API. 
    """
    response = requests.post(
        AMADEUS_API_AUTH,
        data={
            "grant_type": "client_credentials",
            "client_id": AMADEUS_API_KEY,
            "client_secret": AMADEUS_API_SECRET,
        },
    )
    
    if response.status_code == 200:
        return response.json().get("access_token")
    
    print(f"Error getting token: {response.status_code} - {response.text}")
    return None

def fetch_hotels_in_city(city_code):
    """
        Fetch a list of hotels in a given city.
    """
    token = get_access_token()
    if not token:
        return []

    headers = {"Authorization": f"Bearer {token}"}
    params = {"cityCode": city_code}

    response = requests.get(AMADEUS_API_HOTEL_LIST, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Error fetching hotel list: {response.status_code} - {response.text}")
        return []

    hotels = response.json().get("data", [])
    hotel_ids = [hotel["hotelId"] for hotel in hotels]

    return hotel_ids

def fetch_hotels_with_discounts(city_code, check_in, check_out, adults=2):
    
    """
        Fetch hotels from real API (PRODUCTION) or return mock data (SIMULATION).
    """
    
    if MODE == "SIMULATION":
        with open(MOCK_HOTELS_FILE, "r") as file:
            return jsonify(json.load(file))
    
    token = get_access_token()

    if not token:
        return []

    headers = {"Authorization": f"Bearer {token}"}
    hotel_ids = fetch_hotels_in_city(city_code)
    if not hotel_ids:
        print(f"No hotels found in {city_code}.")
        return []

    discounted_hotels = []
    for hotel_id in hotel_ids:
        params = {
            "hotelIds": hotel_id,
            "checkInDate": check_in,
            "checkOutDate": check_out,
            "adults": adults
        }

        response = requests.get(AMADEUS_API_HOTELS, headers=headers, params=params)

        if response.status_code == 200:
            for offer in response.json().get("data", []):
                hotel = offer.get("hotel", {})
                base_price = float(offer["offers"][0]["price"]["variations"]["average"].get("base", 0))
                total_price = float(offer["offers"][0]["price"].get("total", 0))
                discount = max(0, base_price - total_price)

                if discount > 0:
                    discounted_hotels.append({
                        "hotel_id": hotel.get("hotelId", "N/A"),
                        "hotel_name": hotel.get("name", "Unknown Hotel"),
                        "base_price": base_price,
                        "final_price": total_price,
                        "discount": discount,
                        "currency": offer["offers"][0]["price"].get("currency", "N/A"),
                    })

    return discounted_hotels

# Example Usage
if __name__ == "__main__":
    city_code = "PAR"  # Paris
    check_in = "2021-06-01"
    check_out = "2021-06-08"

    hotel_data = fetch_hotels_with_discounts(city_code, check_in, check_out)

    
    if hotel_data:
        print(f"Hotels with Discounts in {city_code}")
        for hotel in hotel_data:
            print(f"{hotel['hotel_name']} | Final Price: {hotel['final_price']} {hotel['currency']} | Discount: {hotel['discount']} {hotel['currency']}")
    else:
        print("No hotel data available.")
