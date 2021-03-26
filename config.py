# Global Configuration for Experiment

# Two mode configuration
MODE = "SIMULATION"  # Change to "PRODUCTION" for real API connections

# API Endpoints (Production Mode)
AMADEUS_API_HOTELS = "https://test.api.amadeus.com/v2/shopping/hotel-offers"
AMADEUS_API_AUTH = "https://test.api.amadeus.com/v1/security/oauth2/token"
AMADEUS_API_HOTEL_LIST = "https://test.api.amadeus.com/v2/reference-data/locations/hotels/by-city"

AMADEUS_API_KEY = ""
AMADEUS_API_SECRET = ""

# File paths for local data Prod mode:
PROD_EXCURSIONS_FILE = ""  # Production dataset SENSITVE

# File paths for local data Simulation mode:
MOCK_HOTELS_FILE = "data/mock_hotels.json"
MOCK_EXCURSIONS_FILE = "data/mock_excursions.json"

# Database
MOCK_DATABASE_PATH = "database/user_events.db"
PROD_DATABASE_PATH = ""     # Production database

# Event Collector API (Production or Simulation)
EVENT_COLLECTOR_URL = "http://127.0.0.1:5004/api/collect-event"
BASE_URL = "http://127.0.0.1:5003/api"