import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
CITY = "Perth,AU"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

FILE_NAME = "weather_data.csv"

def get_weather():
    response = requests.get(URL)
    data = response.json()
    weather = {
        "city": CITY,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"]
    }
    return weather


