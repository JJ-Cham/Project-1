import os
from pathlib import Path

import requests
from dotenv import load_dotenv

ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(ENV_PATH)


def get_climatiq_api_key():
    load_dotenv(ENV_PATH)
    return os.getenv("CLIMATIQ_API_KEY")

ESTIMATE_URL = "https://api.climatiq.io/data/v1/estimate"

ACTIVITY_IDS = {
    "car": "passenger_vehicle-vehicle_type_car-fuel_source_na-engine_size_na-vehicle_age_na-vehicle_weight_na",
    "bus": "passenger_vehicle-vehicle_type_bus-fuel_source_na-distance_na-engine_size_na",
}

def estimate_emissions(activity_id, distance_km):
    api_key = get_climatiq_api_key()
    if not api_key:
        print("Missing CLIMATIQ_API_KEY. Set it as an environment variable.")
        return None

    headers = {"Authorization": f"Bearer {api_key}"}

    payload = {
        "emission_factor": {
            "activity_id": activity_id,
            "data_version": "^6",
        },
        "parameters": {
            "distance": distance_km,
            "distance_unit": "km",
        },
    }

    try:
        response = requests.post(ESTIMATE_URL, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"Carbon request failed: {error}")
        return None

    data = response.json()
    #return data.get("co2e")
    return data.get("co2e") or data.get("result", {}).get("co2e")


def carbon_saved(action_type, distance_km):
    car_emissions = estimate_emissions(ACTIVITY_IDS["car"], distance_km)

    if car_emissions is None:
        return None

    if action_type in ("bike", "walk"):
        return round(car_emissions, 3)

    if action_type == "bus":
        bus_emissions = estimate_emissions(ACTIVITY_IDS["bus"], distance_km)
        if bus_emissions is None:
            return None
        return round(max(car_emissions - bus_emissions, 0), 3)

    return None


if __name__ == "__main__":
    print(estimate_emissions(ACTIVITY_IDS["car"], 10))
    print(carbon_saved("bike", 10))
