from flask import Flask, request, jsonify
from hotel_api import fetch_hotels_with_discounts
from excursion_api import get_mock_excursions
from strategies.strategy_random import generate_random_offer
from strategies.strategy_best_discount import generate_discount_offer
from strategies.strategy_lowest_price import generate_lowest_price_offer

app = Flask(__name__)

@app.route('/api/get-offers', methods=['POST'])
def get_offers():
    """API endpoint to fetch travel offers based on user search criteria."""
    data = request.json
    city = data.get("destination_city")
    strategy = data.get("strategy", "A")  # Default to random offers

    if not city:
        return jsonify({"error": "Missing required parameter: destination_city"}), 400

    # Generate offers based on strategy
    if strategy == "A":
        offers = generate_random_offer(city)
    elif strategy == "B":
        offers = generate_discount_offer(city)
    elif strategy == "C":
        offers = generate_lowest_price_offer(city)
    else:
        return jsonify({"error": "Invalid strategy"}), 400

    return jsonify({"city": city, "strategy": strategy, "offers": offers}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5003)
