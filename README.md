# 🌦️ Weather Dashboard

A simple and responsive weather dashboard built with **Python (Flask)**, **HTML**, **CSS**, and **JavaScript**. Search any city to get real-time weather information and a 5-day forecast using the free Open-Meteo API.
> Note: For simplicity, all frontend code (HTML, CSS, and JavaScript) is contained within a single `index.html` file.

## ✨ Features

- 🔍 Search weather by city name
- 🌡️ Current temperature and feels-like temperature
- 💧 Humidity information
- 💨 Wind speed details
- ☁️ Weather condition descriptions and icons
- 📅 5-day weather forecast
- 🔑 No API key required

## 🛠️ Tech Stack

- **Backend:** Python, Flask, Requests
- **Frontend:** HTML with inline CSS and JavaScript
- **API:** Open-Meteo Geocoding & Forecast APIs

## 📂 Project Structure

```text
weather-dashboard/
│
├── app.py
├── requirements.txt
│
└── templates/
    └── index.html
       ├── HTML
       ├── Inline CSS
       └── Inline JavaScript
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/weather-dashboard.git
cd weather-dashboard
```

### 2. Create a virtual environment (optional)

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in browser

```
http://127.0.0.1:5000
```

## ⚙️ How It Works

1. Enter a city name in the search bar.
2. Flask sends a request to the Open-Meteo Geocoding API.
3. The city is converted into latitude and longitude coordinates.
4. Flask requests weather data from the Open-Meteo Forecast API.
5. The dashboard displays current weather and a 5-day forecast.

## 🔮 Future Enhancements

| Feature | Description |
|----------|-------------|
| 🌍 Geolocation | Detect user's location automatically |
| 🌡️ Unit Toggle | Switch between Celsius and Fahrenheit |
| ⏰ Hourly Forecast | Display detailed hourly weather data |
| ⭐ Favorites | Save frequently searched cities |
| 🎨 Dynamic Themes | Change background based on weather conditions |
| 🐳 Docker Support | Containerize the application for easy deployment |

## 📸 Preview

Add screenshots here after deploying the project.

## 📜 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Developed by Abhijeet
