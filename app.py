from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

WEATHER_CODES = {
    0: ("Clear sky", "☀️"),
    1: ("Mainly clear", "🌤️"),
    2: ("Partly cloudy", "⛅"),
    3: ("Overcast", "☁️"),
    45: ("Fog", "🌫️"),
    48: ("Depositing rime fog", "🌫️"),
    51: ("Light drizzle", "🌦️"),
    53: ("Moderate drizzle", "🌦️"),
    55: ("Dense drizzle", "🌦️"),
    61: ("Slight rain", "🌧️"),
    63: ("Moderate rain", "🌧️"),
    65: ("Heavy rain", "🌧️"),
    71: ("Slight snow", "🌨️"),
    73: ("Moderate snow", "🌨️"),
    75: ("Heavy snow", "❄️"),
    80: ("Rain showers", "🌦️"),
    81: ("Moderate rain showers", "🌧️"),
    82: ("Violent rain showers", "⛈️"),
    95: ("Thunderstorm", "⛈️"),
    96: ("Thunderstorm w/ hail", "⛈️"),
    99: ("Thunderstorm w/ heavy hail", "⛈️"),
}


def describe_weather(code):
    return WEATHER_CODES.get(code, ("Unknown", "❓"))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/weather")
def get_weather():
    city = request.args.get("city", "").strip()
    if not city:
        return jsonify({"error": "Please provide a city name."}), 400

    # 1. Geocode the city name to lat/lon
    geo_resp = requests.get(
        GEOCODE_URL, params={"name": city, "count": 1, "language": "en", "format": "json"}
    )
    geo_data = geo_resp.json()
    results = geo_data.get("results")
    if not results:
        return jsonify({"error": f"Could not find a location named '{city}'."}), 404

    place = results[0]
    lat, lon = place["latitude"], place["longitude"]
    label = ", ".join(
        filter(None, [place.get("name"), place.get("admin1"), place.get("country")])
    )

    # 2. Fetch current weather + short forecast
    weather_resp = requests.get(
        WEATHER_URL,
        params={
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,relative_humidity_2m,apparent_temperature,"
                       "wind_speed_10m,weather_code",
            "daily": "weather_code,temperature_2m_max,temperature_2m_min",
            "timezone": "auto",
            "forecast_days": 5,
        },
    )
    w = weather_resp.json()
    current = w.get("current", {})
    daily = w.get("daily", {})

    desc, icon = describe_weather(current.get("weather_code"))

    forecast = []
    for i in range(len(daily.get("time", []))):
        d_desc, d_icon = describe_weather(daily["weather_code"][i])
        forecast.append({
            "date": daily["time"][i],
            "max": daily["temperature_2m_max"][i],
            "min": daily["temperature_2m_min"][i],
            "icon": d_icon,
            "description": d_desc,
        })

    return jsonify({
        "location": label,
        "current": {
            "temperature": current.get("temperature_2m"),
            "feels_like": current.get("apparent_temperature"),
            "humidity": current.get("relative_humidity_2m"),
            "wind_speed": current.get("wind_speed_10m"),
            "description": desc,
            "icon": icon,
        },
        "forecast": forecast,
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)