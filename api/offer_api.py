from flask import Flask, request, jsonify
from config import MODE
import logging

from api.hotel_api import fetch_hotels_with_discounts
from api.excursion_api import get_excursions

# Import strategy models
from model.strategy_A import generate_offer as generate_offer_A
from model.strategy_B import generate_offer as generate_offer_B
from model.strategy_C import generate_offer as generate_offer_C

# Initialize Flask app
app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)

@app.route('/api/get-offers', methods=['POST'])
def get_offers():
    """API endpoint to fetch travel offers based on user search criteria."""
    data = request.json

    # Extract parameters from request
    city = data.get("destination_city")
    strategy = data.get("strategy", "A")  # Default to strategy A
    check_in = data.get("check_in_date", "2021-06-01")
    check_out = data.get("check_out_date", "2021-06-08")
    adults = data.get("adults", 2)

    if not city:
        return jsonify({"error": "Missing required parameter: destination_city"}), 400

    # Fetch hotels (Mock API in SIMULATION, Amadeus API in PRODUCTION)
    logging.info(f"[{MODE}] Fetching hotels for city: {city}")
    hotels = fetch_hotels_with_discounts(city, check_in, check_out, adults)

    # Fetch excursions (Mock API in SIMULATION, Private Excursions in PRODUCTION)
    logging.info(f"[{MODE}] Fetching excursions for city: {city}")
    excursions = get_excursions(city)

    # Ensure data exists
    if not hotels or not excursions:
        return jsonify({"error": "No hotels or excursions available for the selected city."}), 404

    # Generate offers based on strategy
    if strategy == "A":
        offers = generate_offer_A(hotels, excursions)
    elif strategy == "B":
        offers = generate_offer_B(hotels, excursions)
    elif strategy == "C":
        offers = generate_offer_C(hotels, excursions)
    else:
        return jsonify({"error": "Invalid strategy"}), 400

    response = {"mode": MODE, "city": city, "strategy": strategy, "offers": offers}
    logging.info(f"[{MODE}] Generated {len(offers)} offers for {city} using strategy {strategy}")

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True, port=5003)

