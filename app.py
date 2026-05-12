import requests
from flask import Flask, render_template, redirect, url_for, jsonify
from models import db, WeatherForecast
from datetime import datetime, date
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# WMO Weather interpretation codes (WW)
WEATHER_INTERPRETATION = {
    0: ("Clear sky", "☀️"),
    1: ("Mainly clear", "🌤️"),
    2: ("Partly cloudy", "⛅"),
    3: ("Overcast", "☁️"),
    45: ("Fog", "🌫️"),
    48: ("Depositing rime fog", "🌫️"),
    51: ("Light drizzle", "🌧️"),
    53: ("Moderate drizzle", "🌧️"),
    55: ("Dense drizzle", "🌧️"),
    61: ("Slight rain", "🌦️"),
    63: ("Moderate rain", "🌧️"),
    65: ("Heavy rain", "🌧️"),
    71: ("Slight snow", "❄️"),
    73: ("Moderate snow", "❄️"),
    75: ("Heavy snow", "❄️"),
    95: ("Thunderstorm", "⛈️"),
}

def get_weather_info(code):
    return WEATHER_INTERPRETATION.get(code, ("Unknown", "❓"))

@app.route('/')
def index():
    # Get forecasts from database
    forecasts = WeatherForecast.query.order_by(WeatherForecast.date.asc()).all()
    
    # Enrich data with icons and descriptions
    enriched_forecasts = []
    for f in forecasts:
        desc, icon = get_weather_info(f.condition_code)
        enriched_forecasts.append({
            'date': f.date.strftime('%A, %d %b'),
            'temp_min': f.temp_min,
            'temp_max': f.temp_max,
            'desc': desc,
            'icon': icon,
            'precip': f.precipitation
        })
        
    return render_template('index.html', forecasts=enriched_forecasts)

@app.route('/update')
def update_weather():
    # Open-Meteo API for Jakarta
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": -6.2088,
        "longitude": 106.8456,
        "daily": ["weathercode", "temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
        "timezone": "Asia/Bangkok"
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        daily = data['daily']
        for i in range(len(daily['time'])):
            day_str = daily['time'][i]
            day_date = datetime.strptime(day_str, '%Y-%m-%d').date()
            
            # Check if exists
            forecast = WeatherForecast.query.filter_by(date=day_date).first()
            if not forecast:
                forecast = WeatherForecast(date=day_date)
                db.session.add(forecast)
            
            forecast.temp_max = daily['temperature_2m_max'][i]
            forecast.temp_min = daily['temperature_2m_min'][i]
            forecast.condition_code = daily['weathercode'][i]
            forecast.precipitation = daily['precipitation_sum'][i]
            
        db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Initial update if empty
        if not WeatherForecast.query.first():
            print("Fetching initial data...")
            # We can't really call the route directly easily here without a request context
            # but we can call the logic. I'll just let the user click update or trigger it.
            pass 
    app.run(host='0.0.0.0', debug=True, port=5001)
