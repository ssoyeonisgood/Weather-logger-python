# Weather Logger

A Python project that collects Perth weather data every 10 seconds, stores it in CSV, and automatically updates a temperature graph.


## Features

- Fetches real-time weather data from an API
- Stores historical data in `weather_data.csv`
- Generates a temperature trend graph (`weather_plot.png`) automatically
- Modular code structure for easy maintenance
- Demonstrates Python scripting, data handling, and visualization skills


## Project Structure


- main.py                     # Main script to run the project
- weather_api.py              # Fetch weather data from API
- data_handler.py             # Save data to CSV
- visualize.py                # Generate and overwrite temperature graph
- weather_data.csv            # Accumulated weather data
- weather_plot.png            # Latest temperature graph

---

## Requirements

- Python 3.x
- pandas
- matplotlib
- requests

## How to Run

python main.py


The script will fetch weather data, append it to weather_data.csv, and update weather_plot.png.
By default, it checks the weather every 10 seconds (can be adjusted in main.py).


