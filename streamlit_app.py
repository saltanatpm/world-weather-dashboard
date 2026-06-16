import streamlit as st
import pandas as pd
import sqlite3
from pathlib import Path
import plotly.express as px

# CONFIG
st.set_page_config("Weather Dashboard 🌤️", layout="wide")

st.markdown("""
            <style>
            .main { background:#0d1b2a; }
            section[data-testid="stSidebar"] { background:#0a1520; }
            </style>
            """, unsafe_allow_html=True)

# DATA LOADER
@st.cache_data
def load_data():
    for db in ["weather.db", "data/weather.db"]:
        if Path(db).exists():
            conn = sqlite3.connect(db)
            for t in ["cleaned_weather", "weather_data"]:
                try:
                    return pd.read_sql(f"SELECT * FROM {t}", conn), f"DB:{t}"
                except:
                    pass

    for f in ["data/cleaned_weather.csv", "cleaned_weather.csv"]:
        if Path(f).exists():
            return pd.read_csv(f), f"CSV:{f}"

    return pd.DataFrame({
        "City": ["NY","London","Tokyo","Paris","Dubai"],
        "Condition": ["Cloudy","Rain","Clear","Cloudy","Sunny"],
        "Temperature": [72,58,68,60,104]
    }), "Sample"

df, source = load_data()

df.columns = [c.strip() for c in df.columns]

# SIDEBAR FILTERS
with st.sidebar:
    st.title("🌤️ Weather Explorer")
    st.caption(source)

    conditions = st.multiselect(
        "Condition",
        df["Condition"].unique(),
        default=df["Condition"].unique()
    )

    tmin, tmax = float(df.Temperature.min()), float(df.Temperature.max())
    temp_range = st.slider("Temperature", tmin, tmax, (tmin, tmax))

    city = st.text_input("City search")

mask = (
    df["Condition"].isin(conditions)
    & df["Temperature"].between(*temp_range)
    & df["City"].str.contains(city, case=False, na=False)
)

df = df[mask]

if df.empty:
    st.warning("No data found")
    st.stop()

# METRICS
c1, c2, c3 = st.columns(3)
c1.metric("Cities", len(df))
c2.metric("Avg Temp", f"{df.Temperature.mean():.1f}°F")
c3.metric("Max Temp", f"{df.Temperature.max():.0f}°F")

st.divider()

# BAR CHART
st.subheader("🌡️ Temperature by City")

top_n = st.slider("Top cities", 5, min(30, len(df)), min(10, len(df)))

plot_df = df.nlargest(top_n, "Temperature")

fig_bar = px.bar(
    plot_df.sort_values("Temperature"),
    x="Temperature",
    y="City",
    orientation="h",
    color="Temperature",
    color_continuous_scale="Turbo",
    title="City Temperature Ranking",
    hover_data=["Condition"]
)

st.plotly_chart(fig_bar, use_container_width=True)

# PIE CHART 
col1, col2 = st.columns(2)
with col1:
    st.subheader("🌦️ Conditions Breakdown")
    cond = df["Condition"].value_counts().reset_index()
    cond.columns = ["Condition", "Count"]

    fig_pie = px.pie(
        cond,
        names="Condition",
        values="Count",
        hole=0.4
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# BOX PLOT
with col2:
    st.subheader("📦 Temperature Spread")

    fig_box = px.box(
        df,
        x="Condition",
        y="Temperature",
        color="Condition",
        points="all"
    )
    st.plotly_chart(fig_box, use_container_width=True)

# SCATTER PLOT
st.subheader("📍 City Temperature Scatter")

df_sorted = df.sort_values("Temperature").reset_index(drop=True)
df_sorted["rank"] = df_sorted.index + 1

fig_scatter = px.scatter(
    df_sorted,
    x="rank",
    y="Temperature",
    color="Condition",
    hover_data=["City"],
    size=[10] * len(df_sorted),
    title="Temperature vs City Rank"
)

st.plotly_chart(fig_scatter, use_container_width=True)

# RAW DATA
if st.checkbox("Show data"):
    st.dataframe(df, use_container_width=True)