import requests
from config import MODE, BASE_URL


def test_get_offers():
    """Test the offer generation API in simulation mode."""
    if MODE != "SIMULATION":
        print("Skipping test as it's not in SIMULATION mode.")
        return

    response = requests.post(f"{BASE_URL}/get-offers", json={
        "destination_city": "Paris",
        "strategy": "A",
        "check_in_date": "2025-05-01",
        "check_out_date": "2025-05-07",
        "adults": 2
    })

    assert response.status_code == 200
    data = response.json()
    assert "offers" in data
    assert len(data["offers"]) > 0