import os
from influxdb_client import InfluxDBClient
from queries import execute_and_process_query

# Define constants
host_url = os.environ.get("INFLUXDB_HOST_URL", "default_host_url")
org = os.environ.get("INFLUXDB_ORG", "default_org")
token = os.environ.get("INFLUXDB_TOKEN", "default_token")

# Sanity checks
if not all([host_url, org, token]):
    raise EnvironmentError("Not all required environment variables are set.")


#weather station querie
def fetch_weatherstation_temp():
    client = InfluxDBClient(url=host_url, token=token, org=org)
    df = execute_and_process_query(client, org, "weatherstation_temp")
    print("This displays temperature data:")
    print(df)
    client.__del__()  # Close the client
    return df

def fetch_weatherstation_precipitation():
    client = InfluxDBClient(url=host_url, token=token, org=org)
    df = execute_and_process_query(client, org, "weatherstation_precipitation")
    client.__del__()  # Close the client
    return df

def fetch_weatherstation_luminosity():
    client = InfluxDBClient(url=host_url, token=token, org=org)
    df = execute_and_process_query(client, org, "weatherstation_luminosity")
    client.__del__()  # Close the client
    return df

def fetch_weatherstation_humidity():
    client = InfluxDBClient(url=host_url, token=token, org=org)
    df = execute_and_process_query(client, org, "weatherstation_humidity")
    client.__del__()  # Close the client
    return df

def fetch_weatherstation_wind_speed():
    client = InfluxDBClient(url=host_url, token=token, org=org)
    df = execute_and_process_query(client, org, "weatherstation_wind_speed")
    client.__del__()  # Close the client
    return df

def fetch_weatherstation_air_pressure():
    client = InfluxDBClient(url=host_url, token=token, org=org)
    df = execute_and_process_query(client, org, "weatherstation_air_pressure")
    client.__del__()  # Close the client
    return df

#soil sensors queries
def fetch_soil_water_1():
    client = InfluxDBClient(url=host_url, token=token, org=org)
    df = execute_and_process_query(client, org, "soil_water_1")
    client.__del__()  # Close the client
    return df

def fetch_soil_water_2():
    client = InfluxDBClient(url=host_url, token=token, org=org)
    df = execute_and_process_query(client, org, "soil_water_2")
    client.__del__()  # Close the client
    return df

def fetch_soil_water_3():
    client = InfluxDBClient(url=host_url, token=token, org=org)
    df = execute_and_process_query(client, org, "soil_water_3")
    client.__del__()  # Close the client
    return df

def fetch_soil_water_4():
    client = InfluxDBClient(url=host_url, token=token, org=org)
    df = execute_and_process_query(client, org, "soil_water_4")

    client.__del__()  # Close the client
    return df

def fetch_soil_water_5():
    client = InfluxDBClient(url=host_url, token=token, org=org)
    df = execute_and_process_query(client, org, "soil_water_5")
    print("This displays sensor soil 2 data:")
    print(df)
    client.__del__()  # Close the client
    return df