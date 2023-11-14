import pandas as pd

query_water_1 = '''
from(bucket: "Kusel")
    |> range(start: -1d)
    |> filter(fn: (r) => 
        r._measurement == "mqtt_consumer" and
        (r._field == "water_SOIL") and
        r.device == "eui-a84041b721876064" 
    )
'''

query_water_2 = '''
from(bucket: "Kusel")
    |> range(start: -1d)
    |> filter(fn: (r) => 
        r._measurement == "mqtt_consumer" and
        (r._field == "water_SOIL") and
        r.device == "eui-a84041eff18827d1" 
    )
'''

query_water_3 = '''
from(bucket: "Kusel")
    |> range(start: -1d)
    |> filter(fn: (r) => 
        r._measurement == "mqtt_consumer" and
        (r._field == "water_SOIL") and
        r.device == "eui-a8404109118827b3" 
    )
'''

query_water_4 = '''
from(bucket: "Kusel")
    |> range(start: -1d)
    |> filter(fn: (r) => 
        r._measurement == "mqtt_consumer" and
        (r._field == "water_SOIL") and
        r.device == "eui-a840416eb18827cb" 
    )
'''

query_water_5 = '''
from(bucket: "Kusel")
    |> range(start: -1d)
    |> filter(fn: (r) => 
        r._measurement == "mqtt_consumer" and
        (r._field == "water_SOIL") and
        r.device == "eui-a840411b518827d3" 
    )
'''

query_weatherstation_temp = '''
from(bucket: "Kusel")
  |> range(start: -1d)
  |> filter(fn: (r) =>
      r._measurement == "mqtt_consumer" and
      r._field == "measurementValue" and
      r.device == "eui-2cf7f1c0443003da" and
      r.type == "Air Temperature"
  )

'''

query_weatherstation_precipitation = '''
from(bucket: "Kusel")
  |> range(start: -1d)
  |> filter(fn: (r) =>
      r._measurement == "mqtt_consumer" and
      r._field == "measurementValue" and
      r.device == "eui-2cf7f1c0443003da" and
      r.type == "Rain Gauge"
  )

'''

query_weatherstation_luminosity = '''
from(bucket: "Kusel")
  |> range(start: -1d)
  |> filter(fn: (r) =>
      r._measurement == "mqtt_consumer" and
      r._field == "measurementValue" and
      r.device == "eui-2cf7f1c0443003da" and
      r.type == "Light Intensity"
  )

'''

query_weatherstation_humidity = '''
from(bucket: "Kusel")
  |> range(start: -1d)
  |> filter(fn: (r) =>
      r._measurement == "mqtt_consumer" and
      r._field == "measurementValue" and
      r.device == "eui-2cf7f1c0443003da" and
      r.type == "Air Humidity"
  )

'''

query_weatherstation_wind_speed = '''
from(bucket: "Kusel")
  |> range(start: -1d)
  |> filter(fn: (r) =>
      r._measurement == "mqtt_consumer" and
      r._field == "measurementValue" and
      r.device == "eui-2cf7f1c0443003da" and
      r.type == "Wind Speed"
  )

'''

query_weatherstation_air_pressure = '''
from(bucket: "Kusel")
  |> range(start: -1d)
  |> filter(fn: (r) =>
      r._measurement == "mqtt_consumer" and
      r._field == "measurementValue" and
      r.device == "eui-2cf7f1c0443003da" and
      r.type == "Barometric Pressure"
  )

'''



def execute_and_process_query(client, org, query_name):
    if query_name == "soil_water_1":
        result = client.query_api().query(org=org, query=query_water_1)
    elif query_name == "soil_water_2":
        result = client.query_api().query(org=org, query=query_water_2)
    elif query_name == "soil_water_3":
        result = client.query_api().query(org=org, query=query_water_3)
    elif query_name == "soil_water_4":
        result = client.query_api().query(org=org, query=query_water_4)
    elif query_name == "soil_water_5":
        result = client.query_api().query(org=org, query=query_water_5)
    elif query_name == "weatherstation_temp":
        result = client.query_api().query(org=org, query=query_weatherstation_temp)
    elif query_name == "weatherstation_precipitation":
        result = client.query_api().query(org=org, query=query_weatherstation_precipitation)
    elif query_name == "weatherstation_humidity":
        result = client.query_api().query(org=org, query=query_weatherstation_humidity)
    elif query_name == "weatherstation_luminosity":
        result = client.query_api().query(org=org, query=query_weatherstation_luminosity)
    elif query_name == "weatherstation_air_pressure":
        result = client.query_api().query(org=org, query=query_weatherstation_air_pressure)
    elif query_name == "weatherstation_wind_speed":
        result = client.query_api().query(org=org, query=query_weatherstation_wind_speed)
    else:
        raise ValueError(f"Unknown query name: {query_name}")

    # serialize to JSON
    output = result.to_values(columns=['_time', '_value'])

    # transform into a pandas dataframe
    df = pd.DataFrame(output, columns=['time', 'value'])

    # convert UTC to CET (only if there are values in the time column, so only if the sensor is working)
    if not df['time'].empty:
        df['time'] = df['time'].dt.tz_convert('Etc/GMT-2')

    return df
