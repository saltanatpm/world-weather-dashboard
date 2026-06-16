import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
RAW_PATH = DATA_DIR / "raw_weather.csv"
CLEAN_PATH = DATA_DIR / "cleaned_weather.csv"

df = pd.read_csv(RAW_PATH)

print("BEFORE CLEANING")
print(df.head())
print(f"Rows before cleaning: {len(df)}")

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

# Clean temperature column (°F instead of °C)
df["Temperature"] = (
    df["Temperature"]
    .str.replace("°F", "", regex=False)
    .str.strip()
)

# Convert to numeric
df["Temperature"] = pd.to_numeric(df["Temperature"], errors="coerce")

df = df.dropna(subset=["Temperature"])

# Clean condition text (remove extra spaces)
df["Condition"] = df["Condition"].str.strip()

print("\nAFTER CLEANING")
print(df.head())
print(f"Rows after cleaning: {len(df)}")

df.to_csv(CLEAN_PATH, index=False)
print(f"\n✅ Cleaned data saved to: {CLEAN_PATH}")