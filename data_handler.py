import os
import pandas as pd

FILE_NAME = "weather_data.csv"

def save_to_csv(record):
    df = pd.DataFrame([record])
    if os.path.exists(FILE_NAME):
        df.to_csv(FILE_NAME, mode="a", header=False, index=False)
    else:
        df.to_csv(FILE_NAME, index=False)

