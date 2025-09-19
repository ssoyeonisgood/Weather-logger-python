import requests
from datetime import datetime

API_KEY = "6f4598ea4307e2eec73f487375dc7e6d"  
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


