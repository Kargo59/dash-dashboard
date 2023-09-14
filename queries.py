import pandas as pd

query_soil_temp = '''
from(bucket: "Kusel")
    |> range(start: -1d)
    |> filter(fn: (r) => 
        r._measurement == "mqtt_consumer" and
        (r._field == "temp_SOIL") and
        r.device == "eui-a84041b721876064" 
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

def execute_and_process_query(client, org, query_name):
    if query_name == "soil_temp":
        result = client.query_api().query(org=org, query=query_soil_temp)
    elif query_name == "weatherstation_temp":
        result = client.query_api().query(org=org, query=query_weatherstation_temp)
    elif query_name == "weatherstation_precipitation":
        result = client.query_api().query(org=org, query=query_weatherstation_precipitation)
    else:
        raise ValueError(f"Unknown query name: {query_name}")

    # serialize to JSON
    output = result.to_values(columns=['_time', '_value'])

    # transform into a pandas dataframe
    df = pd.DataFrame(output, columns=['time', 'value'])

    # convert UTC to CET
    df['time'] = df['time'].dt.tz_convert('Etc/GMT-2')

    return df
