import pandas as pd
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "cleaned_weather.csv"
DB_FILE = BASE_DIR / "data/weather.db"

# LOAD DATA
df = pd.read_csv(DATA_FILE)

print("Data loaded:", df.shape)
conn = sqlite3.connect(DB_FILE)

df.to_sql(
    "weather_data",
    conn,
    if_exists="replace",
    index=False
)
conn.commit()
conn.close()

print("✅ Data saved to SQLite database successfully!")
print(f"Database location: {DB_FILE}")