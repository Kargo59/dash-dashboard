# Python Dash Dashboard

A real-time IoT data visualization dashboard built with Python Dash and Plotly. Display sensor data from weather stations and soil moisture sensors with smooth, interactive charts.

## Features

- Real-time Data Visualization - Interactive charts powered by Plotly
- Responsive Design - Clean, modern UI with Bootstrap styling
- InfluxDB Ready - Toggle between dummy data and live InfluxDB connection

### Installation

1. Clone the repository
```bash
git clone https://github.com/Kargo59/dash-dashboard.git
cd dash-dashboard
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
python app.py
```

4. Open in browser

Navigate to `http://localhost:8050` in your web browser

## Configuration

### Using Dummy Data (Default)

The dashboard currently uses smooth, realistic dummy data for demonstration. No setup required!

### Using InfluxDB (Live Data)

To connect to a live InfluxDB instance:

1. Set environment variables:
```bash
set INFLUXDB_HOST_URL=your_host_url
set INFLUXDB_ORG=your_org
set INFLUXDB_TOKEN=your_token
```

2. Uncomment the InfluxDB code in the relevant data fetching functions

3. Restart the application

The InfluxDB integration code is included and commented out for reference.

## License

This project is open source and available under the MIT License.
