import pandas as pd
import sqlite3

conn = sqlite3.connect("weather.db")

df = pd.read_csv("data/cleaned_weather.csv")

df.to_sql(
    "weather_data",
    conn,
    if_exists="replace",
    index=False
)

conn.commit()
conn.close()

print("Database created successfully.")