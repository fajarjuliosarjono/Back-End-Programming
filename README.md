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

## Alur Program
- Grab data dari api https://api.open-meteo.com/v1/forecast
- data di simpan di database sqlite dengan struktur table dibawah ini
``` id INTEGER NOT NULL, 
	date DATE NOT NULL, 
	temp_min FLOAT NOT NULL, 
	temp_max FLOAT NOT NULL, 
	condition_code INTEGER NOT NULL, 
	precipitation FLOAT NOT NULL, 
	created_at DATETIME, 
	PRIMARY KEY (id), 
	UNIQUE (date)
   ```

- untuk parameter mendapatkan wilayah jakarta menggunakan parameter berikut ini : 

      
       "latitude": -6.2088,
        "longitude": 106.8456,
        "daily": ["weathercode", "temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
        "timezone": "Asia/Bangkok"
      

- Web di tampilkan dengan flask pada python

# Back-End-Programming


