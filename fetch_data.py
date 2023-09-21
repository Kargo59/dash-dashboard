import json
import os
from data_source import fetch_weatherstation_temp, fetch_weatherstation_precipitation, fetch_weatherstation_luminosity, fetch_weatherstation_humidity, fetch_weatherstation_wind_speed, fetch_weatherstation_air_pressure
import pandas as pd
from dotenv import load_dotenv

load_dotenv()



# Fetch data
df_weatherstation = fetch_weatherstation_temp() #Temperature
df_weatherstation_precipitation = fetch_weatherstation_precipitation()
df_weatherstation_luminosity = fetch_weatherstation_luminosity()
df_weatherstation_humidity = fetch_weatherstation_humidity()
df_weatherstation_wind_speed = fetch_weatherstation_wind_speed()
df_weatherstation_air_pressure = fetch_weatherstation_air_pressure()

# Convert dataframes to dictionaries (or lists of dictionaries)
weatherstation_data = df_weatherstation.to_dict()
weatherstation_data_precipitation = df_weatherstation_precipitation.to_dict()
weatherstation_data_luminosity = df_weatherstation_luminosity.to_dict()
weatherstation_data_humidity = df_weatherstation_humidity.to_dict()
weatherstation_data_wind_speed = df_weatherstation_wind_speed.to_dict()
weatherstation_data_air_pressure = df_weatherstation_air_pressure.to_dict()

# Store data in a combined dictionary
combined_data = {
    'weatherstation': weatherstation_data,
    'weatherstation_precipitation': weatherstation_data_precipitation,
    'weatherstation_luminosity': weatherstation_data_luminosity,
    'weatherstation_humidity': weatherstation_data_humidity,
    'weatherstation_wind_speed': weatherstation_data_wind_speed,
    'weatherstation_air_pressure': weatherstation_data_air_pressure,

}

def convert_to_iso(o):
    if isinstance(o, pd.Timestamp):
        return o.isoformat()
    raise TypeError(f"Object of type {type(o).__name__} is not JSON serializable")

# Write data to a JSON file
with open('data/data.json', 'w') as file:
    json.dump(combined_data, file, default=convert_to_iso)

