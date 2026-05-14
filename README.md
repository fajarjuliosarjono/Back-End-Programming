# Weather Monitoring Dashboard

A Flask-based weather monitoring application that tracks the 7-day forecast for Jakarta and stores it in a SQLite database.

## Features
- **Weekly Monitoring**: Automatically fetches 7-day forecast from Open-Meteo API.
- **SQLite Integration**: Persists weather data locally.
- **Modern UI**: Premium design with glassmorphism and dark mode.
- **Responsive**: Works on desktop and mobile devices.

## Setup Instructions

1. **Create and activate virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

3. **Access the dashboard**:
   Open your browser and go to `http://127.0.0.1:5001`.
   Click the **Refresh Data** button to fetch the initial weather data.

## Project Structure
- `app.py`: Main application logic and routes.
- `models.py`: Database schema definition.
- `static/css/style.css`: UI styling.
- `templates/index.html`: Dashboard template.
- `instance/weather.db`: SQLite database (auto-generated).

## Program Flow

1. **Data Fetching**: The application retrieves weather data from the [Open-Meteo API](https://api.open-meteo.com/v1/forecast).
2. **API Specification**: Detailed documentation for location parameters and other API features can be found at [Open-Meteo Docs](https://open-meteo.com/en/docs).
3. **Database Storage**: Fetched data is stored in a SQLite database with the following schema:

   ```sql
   CREATE TABLE weather_forecast (
       id INTEGER NOT NULL PRIMARY KEY, 
       date DATE NOT NULL UNIQUE, 
       temp_min FLOAT NOT NULL, 
       temp_max FLOAT NOT NULL, 
       condition_code INTEGER NOT NULL, 
       precipitation FLOAT NOT NULL, 
       created_at DATETIME
   );
   ```

4. **Jakarta Location Configuration**: To track Jakarta, the following parameters are used:
   - **Latitude**: -6.2088
   - **Longitude**: 106.8456
   - **Daily Data**: `weathercode`, `temperature_2m_max`, `temperature_2m_min`, `precipitation_sum`
   - **Timezone**: `Asia/Bangkok`

5. **Web Interface**: The dashboard is rendered using Python's Flask framework.

---
*Created for Back-End Programming course.*
