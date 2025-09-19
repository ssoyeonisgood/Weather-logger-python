from weather_api import get_weather
from data_handler import save_to_csv
from visualize import visualize_weather
import schedule
import time

def main():
    while True:
        weather = get_weather()
        print("Weather Date:", weather)
        save_to_csv(weather)
        visualize_weather()
        print("🕥 Checking again in 10 seconds...\n")
        time.sleep(10) 

if __name__ == "__main__":
    main()

