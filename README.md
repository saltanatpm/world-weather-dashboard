World Weather Dashboard

📌 Project Overview

The World Weather Dashboard is a data engineering capstone project that collects global weather data using Selenium web scraping, processes and cleans the dataset using Pandas, stores structured data in SQLite, and provides interactive data visualization through a Streamlit dashboard.

This project demonstrates end-to-end data pipeline skills:

- Data collection (web scraping)
- Data cleaning and transformation
- Data storage (SQLite)
- Data visualization (Streamlit + Plotly)
          ⚙️ Tech Stack
          🧠 Python
          🌐 Selenium (Web Scraping)
          🐼 Pandas (Data Processing)
          🗄️ SQLite (Database Storage)
          📊 Plotly (Visualizations)
          📦 Streamlit (Interactive Dashboard)
          🚀 Features
        
🔎 Web Scraping
    Scrapes global weather data from a dynamic website using Selenium
    Handles pagination across multiple pages
    Manages missing or inconsistent HTML elements safely
    Stores raw scraped data into CSV format (raw_weather.csv)
    Prevents duplicate scraping requests
🧹 Data Cleaning & Transformation
    Loads raw dataset into Pandas DataFrame
    Removes duplicates and missing values
    Converts data types (e.g., temperature strings → numeric values)
    Standardizes column formats
    Produces cleaned dataset (cleaned_weather.csv)
    Includes before vs after comparison of dataset size
📊 Data Visualization
    Interactive charts built with Plotly
    Includes:
        🌡️ Temperature comparison across cities
        🌍 Weather condition distribution
        🔥 Top hottest / coldest cities ranking
    Fully interactive filters:
        City dropdown
        Temperature range slider
        Dynamic chart updates based on user input
📈 Dashboard (Streamlit App)
    Built using Streamlit for interactive exploration
    Clean UI with sidebar filters
    Displays processed data and visual insights
    Responsive layout for easy navigation
    Includes clear titles, descriptions, and user guidance
🧑‍💻 Code Quality & Structure
    Modular code structure:
        scraper.py
        clean_data.py
        database.py
        streamlit_app.py
    Functions used for reusability and readability
    Inline comments explaining logic and transformations
    Requirements file included for reproducibility
