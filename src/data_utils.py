import os
import requests
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NASA_API_KEY", "LATER ALLIGATOR GIT IGNORE")
NASA_API_URL = "https://api.nasa.gov/neo/rest/v1/feed"

def fetch_neo_data(start_date: str, end_date: str, api_key: str = API_KEY) -> dict:
    """
    Fetch Near-Earth Object data from NASA's NeoWs API.
    """
    params = {
        "start_date": start_date,
        "end_date": end_date,
        "api_key": api_key
    }
    response = requests.get(NASA_API_URL, params=params)
    response.raise_for_status()
    return response.json()

def flatten_neo_data(raw_json: dict) -> pd.DataFrame:
    """
    Flatten NEO JSON data from NASA API into a DataFrame.
    """
    asteroids = raw_json.get("near_earth_objects", {})
    all_asteroids = []

    for date, asteroid_list in asteroids.items():
        for asteroid in asteroid_list:
            try:
                approach = asteroid.get("close_approach_data", [{}])[0]
                diameter_data = asteroid.get("estimated_diameter", {}).get("kilometers", {})

                asteroid_entry = {
                    "name": asteroid.get("name"),
                    "id": asteroid.get("id"),
                    "absolute_magnitude_h": asteroid.get("absolute_magnitude_h"),
                    "is_hazardous": asteroid.get("is_potentially_hazardous_asteroid"),
                    "diameter_min_km": diameter_data.get("estimated_diameter_min"),
                    "diameter_max_km": diameter_data.get("estimated_diameter_max"),
                    "velocity_km_s": float(approach.get("relative_velocity", {}).get("kilometers_per_second", 0.0)),
                    "miss_distance_km": float(approach.get("miss_distance", {}).get("kilometers", 0.0)),
                    "orbiting_body": approach.get("orbiting_body"),
                    "approach_date": approach.get("close_approach_date")
                }

                all_asteroids.append(asteroid_entry)

            except Exception as e:
                print(f"⚠️ Skipping malformed entry due to error: {e}")
                continue

    return pd.DataFrame(all_asteroids)

def save_data_to_excel(df: pd.DataFrame, path: str):
    """
    Save a DataFrame to CSV file.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_excel(path, index=False)
    print(f"✅ Data saved to {path}")

# Test
if __name__ == "__main__":
    today = datetime.today().date()
    next_week = today + timedelta(days=7)

    print("📡 Fetching data from NASA API...")
    raw_data = fetch_neo_data(str(today), str(next_week))
    df = flatten_neo_data(raw_data)
    print(df)

    save_data_to_excel(df, "data/raw/neo_data.xlsx")
