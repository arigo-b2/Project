import requests
import pandas as pd

api_key = 'LATER ALLIGATOR GIT IGNORE'
start_date = '2025-01-01'
end_date = '2025-01-07'

url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}"

response = requests.get(url)
data = response.json()

# Extracting information
asteroids = data['near_earth_objects']

all_asteroids = []
for date, asteroid_list in asteroids.items():
    for asteroid in asteroid_list:
        all_asteroids.append({
            'name': asteroid['name'],
            'date': date,
            'miss_distance_km': float(asteroid['close_approach_data'][0]['miss_distance']['kilometers']),
            'velocity_km_s': float(asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_second']),
            'diameter_m': float(asteroid['estimated_diameter']['meters']['estimated_diameter_max'])
        })

# Convert to DataFrame
df_asteroids = pd.DataFrame(all_asteroids)
print(df_asteroids.head())
