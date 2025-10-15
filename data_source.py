import os
from influxdb_client import InfluxDBClient
from queries import execute_and_process_query
import pandas as pd
import numpy as np
from datetime import datetime, timedelta



###############################################         dummy data, see the version below for influxdb version       #########################################################


# Generate dummy data with realistic timestamps
def generate_dummy_timeseries(num_points=100):
    """Generate timestamps for the last N days"""
    end_time = datetime.now()
    start_time = end_time - timedelta(days=30)
    return pd.date_range(start=start_time, end=end_time, periods=num_points)

def generate_smooth_data(timestamps, base_value, amplitude, noise_level=0.5):
    """Generate smooth sinusoidal data with slight noise"""
    x = np.linspace(0, 4 * np.pi, len(timestamps))
    sine_wave = amplitude * np.sin(x)
    noise = np.random.normal(0, noise_level, len(timestamps))
    return base_value + sine_wave + noise

# Weather station queries
def fetch_weatherstation_temp():
    timestamps = generate_dummy_timeseries()
    df = pd.DataFrame({
        'time': timestamps,
        'value': generate_smooth_data(timestamps, base_value=22, amplitude=5, noise_level=0.3)
    })
    print("This displays temperature data:")
    print(df)
    return df

def fetch_weatherstation_precipitation():
    timestamps = generate_dummy_timeseries()
    df = pd.DataFrame({
        'time': timestamps,
        'value': generate_smooth_data(timestamps, base_value=15, amplitude=8, noise_level=0.5)
    })
    return df

def fetch_weatherstation_luminosity():
    timestamps = generate_dummy_timeseries()
    df = pd.DataFrame({
        'time': timestamps,
        'value': generate_smooth_data(timestamps, base_value=50000, amplitude=20000, noise_level=1000)
    })
    return df

def fetch_weatherstation_humidity():
    timestamps = generate_dummy_timeseries()
    df = pd.DataFrame({
        'time': timestamps,
        'value': generate_smooth_data(timestamps, base_value=60, amplitude=15, noise_level=0.5)
    })
    return df

def fetch_weatherstation_wind_speed():
    timestamps = generate_dummy_timeseries()
    df = pd.DataFrame({
        'time': timestamps,
        'value': generate_smooth_data(timestamps, base_value=10, amplitude=5, noise_level=0.3)
    })
    return df

def fetch_weatherstation_air_pressure():
    timestamps = generate_dummy_timeseries()
    df = pd.DataFrame({
        'time': timestamps,
        'value': generate_smooth_data(timestamps, base_value=1013, amplitude=8, noise_level=0.2)
    })
    return df

# Soil sensors queries
def fetch_soil_water_1():
    timestamps = generate_dummy_timeseries()
    df = pd.DataFrame({
        'time': timestamps,
        'value': generate_smooth_data(timestamps, base_value=40, amplitude=12, noise_level=0.5)
    })
    return df

def fetch_soil_water_2():
    timestamps = generate_dummy_timeseries()
    df = pd.DataFrame({
        'time': timestamps,
        'value': generate_smooth_data(timestamps, base_value=42, amplitude=10, noise_level=0.5)
    })
    print("test 2")
    print(df)
    return df

def fetch_soil_water_3():
    timestamps = generate_dummy_timeseries()
    df = pd.DataFrame({
        'time': timestamps,
        'value': generate_smooth_data(timestamps, base_value=38, amplitude=12, noise_level=0.5)
    })
    return df

def fetch_soil_water_4():
    timestamps = generate_dummy_timeseries()
    df = pd.DataFrame({
        'time': timestamps,
        'value': generate_smooth_data(timestamps, base_value=45, amplitude=8, noise_level=0.5)
    })
    return df

def fetch_soil_water_5():
    timestamps = generate_dummy_timeseries()
    df = pd.DataFrame({
        'time': timestamps,
        'value': generate_smooth_data(timestamps, base_value=41, amplitude=11, noise_level=0.5)
    })
    print("This displays sensor soil 2 data:")
    print(df)
    return df


###############################################         dummy data, see the version below for influxdb version       #########################################################



# # Define constants
# host_url = os.environ.get("INFLUXDB_HOST_URL", "default_host_url")
# org = os.environ.get("INFLUXDB_ORG", "default_org")
# token = os.environ.get("INFLUXDB_TOKEN", "default_token")

# # Sanity checks
# if not all([host_url, org, token]):
#     raise EnvironmentError("Not all required environment variables are set.")


# #weather station querie
# def fetch_weatherstation_temp():
#     client = InfluxDBClient(url=host_url, token=token, org=org)
#     df = execute_and_process_query(client, org, "weatherstation_temp")
#     print("This displays temperature data:")
#     print(df)
#     client.__del__()  # Close the client
#     return df

# def fetch_weatherstation_precipitation():
#     client = InfluxDBClient(url=host_url, token=token, org=org)
#     df = execute_and_process_query(client, org, "weatherstation_precipitation")
#     client.__del__()  # Close the client
#     return df

# def fetch_weatherstation_luminosity():
#     client = InfluxDBClient(url=host_url, token=token, org=org)
#     df = execute_and_process_query(client, org, "weatherstation_luminosity")
#     client.__del__()  # Close the client
#     return df

# def fetch_weatherstation_humidity():
#     client = InfluxDBClient(url=host_url, token=token, org=org)
#     df = execute_and_process_query(client, org, "weatherstation_humidity")
#     client.__del__()  # Close the client
#     return df

# def fetch_weatherstation_wind_speed():
#     client = InfluxDBClient(url=host_url, token=token, org=org)
#     df = execute_and_process_query(client, org, "weatherstation_wind_speed")
#     client.__del__()  # Close the client
#     return df

# def fetch_weatherstation_air_pressure():
#     client = InfluxDBClient(url=host_url, token=token, org=org)
#     df = execute_and_process_query(client, org, "weatherstation_air_pressure")
#     client.__del__()  # Close the client
#     return df

# #soil sensors queries
# def fetch_soil_water_1():
#     client = InfluxDBClient(url=host_url, token=token, org=org)
#     df = execute_and_process_query(client, org, "soil_water_1")
#     client.__del__()  # Close the client
#     return df

# def fetch_soil_water_2():
#     client = InfluxDBClient(url=host_url, token=token, org=org)
#     df = execute_and_process_query(client, org, "soil_water_2")
#     print("test 2")
#     print(df)
#     client.__del__()  # Close the client
#     return df

# def fetch_soil_water_3():
#     client = InfluxDBClient(url=host_url, token=token, org=org)
#     df = execute_and_process_query(client, org, "soil_water_3")
#     client.__del__()  # Close the client
#     return df

# def fetch_soil_water_4():
#     client = InfluxDBClient(url=host_url, token=token, org=org)
#     df = execute_and_process_query(client, org, "soil_water_4")

#     client.__del__()  # Close the client
#     return df

# def fetch_soil_water_5():
#     client = InfluxDBClient(url=host_url, token=token, org=org)
#     df = execute_and_process_query(client, org, "soil_water_5")
#     print("This displays sensor soil 2 data:")
#     print(df)
#     client.__del__()  # Close the client
#     return df


