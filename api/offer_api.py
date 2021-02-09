from flask import Flask, request, jsonify
from hotel_api import fetch_hotels_with_discounts
from excursion_api import get_excursions
from model.strategy_A import generate_offer as generate_offer_A
from model.strategy_B import generate_offer as generate_offer_B
from model.strategy_C import generate_offer as generate_offer_C

# Initialize Flask app
app = Flask(__name__)


@app.route('/api/get-offers', methods=['POST'])
def get_offers():
    """API endpoint to fetch travel offers based on user search criteria."""
    data = request.json

    # Extract parameters from request
    city = data.get("destination_city")
    strategy = data.get("strategy", "A")  # Default to random offers
    check_in = data.get("check_in_date", "2025-06-01")
    check_out = data.get("check_out_date", "2025-06-08")
    adults = data.get("adults", 2)

    if not city:
        return jsonify({"error": "Missing required parameter: destination_city"}), 400

    # Fetch hotels with discounts
    hotels = fetch_hotels_with_discounts(city, check_in, check_out, adults)

    # Fetch excursions
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

    response = {"city": city, "strategy": strategy, "offers": offers}

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True, port=5003)

