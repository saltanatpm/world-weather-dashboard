import pandas as pd
import sqlite3

# Load cleaned data
df = pd.read_csv("cleaned_weather.csv")

print("Data loaded:", df.shape)

# Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect("weather.db")

# Save to SQL table
df.to_sql("weather_data", conn, if_exists="replace", index=False)

print("Data saved to SQLite database successfully!")

# Close connection
conn.close()