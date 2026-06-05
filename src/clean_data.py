import pandas as pd

df = pd.read_csv("data/raw_weather.csv")

print("BEFORE CLEANING")
print(df.head())
print(f"Rows before cleaning: {len(df)}")

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

# Clean temperature column
df["Temperature"] = df["Temperature"].str.replace("°C", "", regex=False)
df["Temperature"] = pd.to_numeric(df["Temperature"], errors="coerce")

# Remove rows where temperature could not be converted
df = df.dropna(subset=["Temperature"])

print("\nAFTER CLEANING")
print(df.head())
print(f"Rows after cleaning: {len(df)}")
df.to_csv("data/cleaned_weather.csv", index=False)

print("Cleaned data saved.")
