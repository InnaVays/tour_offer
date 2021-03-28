# Travel Offer Experiment – A/B Testing for Travel Recommendations  

## Project Overview  
This project simulates and analyzes **A/B testing strategies** for travel offer generation.  
Users are assigned different recommendation strategies, and **their interactions are tracked** to determine the most effective approach.  

- **Supports both Simulation & Production Modes**  
- **Dynamic Travel Offer Generation** (Hotels + Excursions)  
- **Real-time Monitoring Dashboard**  
- **Statistical Analysis & Decision-Making**  

---

## Features  
- ** Travel Offer Engine** – Generates personalized offers based on hotels & excursions.  
- ** A/B Testing & Experiment Tracking** – Logs user interactions & evaluates strategies.  
- ** Simulation Mode** – Generates **mock data** for testing.  
- ** Production Mode** – Connects to **real Amadeus API & private excursion data**.  
- ** Real-Time Dashboard** – Monitors experiment results & live user activity.  

---

## Installation & Setup  

### **1️ Clone the Repository**  

```
git clone https://github.com/InnaVays/tour_offer.git
cd tour_offer
```

### **2 Create Virtual Environment (Python 3.8)

```
python3.8 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r env/requirements.txt
```

### **3 Run the APIs & Dashboard

```
chmod +x run_api.sh
./run_api.sh
```

### **4 Start the Experiment (Choose Mode)

```
# Simulation Mode (Simulated Data)
python run.py --simulation  

# Production Mode 
python run.py --production
```

### Experiment Strategies
- Strategy A	Random Travel Offers
- Strategy B	Cheapest Available Combination
- Strategy C	Largest Discount Offers
- Strategy 0	No Offer (Control Group)
User activity is tracked & analyzed to determine which strategy performs best in terms of clicks, interest, and conversions.

### Running in Docker (Optional)

```
# Build the Docker Image
docker build -t travel_offer_experiment .

# Run the Container
docker run -p 5003:5003 travel_offer_experiment
```

### Viewing the Dashboard
Once the APIs are running, open the dashboard in your browser:
http://localhost:8501