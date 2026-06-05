import pandas as pd
import sqlite3

# LOAD DATA
raw_df = pd.read_csv("data/raw_weather.csv")
clean_df = pd.read_csv("data/cleaned_weather.csv")

# CLEANING (if needed check)
clean_df = clean_df.drop_duplicates()
clean_df = clean_df.dropna()

# Example transformation
if "Temperature" in clean_df.columns:
    clean_df["Temperature"] = clean_df["Temperature"].str.replace("°C", "", regex=False)
    clean_df["Temperature"] = pd.to_numeric(clean_df["Temperature"], errors="coerce")

# SQLITE CONNECTION
conn = sqlite3.connect("weather.db")

raw_df.to_sql("raw_weather", conn, if_exists="replace", index=False)
clean_df.to_sql("cleaned_weather", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("SQLite database successfully created with raw + cleaned tables.")