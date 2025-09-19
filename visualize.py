import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_NAME = "weather_data.csv"
PLOT_FILE = "weather_plot.png"

def visualize_weather():
    if not os.path.exists(FILE_NAME):
        print("❌ The file doesn't exist")
        return
    
    df = pd.read_csv(FILE_NAME)
    if "temperature" not in df.columns:
        print("❌ No 'temperature' column.")
        return

    plt.figure(figsize=(8, 5))
    plt.plot(df.index, df["temperature"], marker="o", label="Temperature (°C)")
    plt.title("Weather Temperature Trend")
    plt.xlabel("Record Index")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True)
    
    plt.savefig(PLOT_FILE)
    plt.close()
    print(f"✅ Complete storing data (overwriting): {PLOT_FILE}")
