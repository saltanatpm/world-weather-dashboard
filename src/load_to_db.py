import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
RAW_PATH = DATA_DIR / "raw_weather.csv"
CLEAN_PATH = DATA_DIR / "cleaned_weather.csv"

DB_PATH = BASE_DIR / "weather.db"

# LOAD DATA
raw_df = pd.read_csv(RAW_PATH)
clean_df = pd.read_csv(CLEAN_PATH)

conn = sqlite3.connect(DB_PATH)

# Store raw data
raw_df.to_sql(
    "raw_weather",
    conn,
    if_exists="replace",
    index=False
)

# Store cleaned data
clean_df.to_sql(
    "cleaned_weather",
    conn,
    if_exists="replace",
    index=False
)

conn.commit()
conn.close()

print("✅ SQLite database created successfully")
print("Tables created: raw_weather, cleaned_weather")