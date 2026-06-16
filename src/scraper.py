from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from pathlib import Path

# PATH SETUP
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

driver = webdriver.Chrome()
driver.get("https://www.timeanddate.com/weather/")

wait = WebDriverWait(driver, 10)
wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "table tbody tr")
    )
)

data = []
rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) >= 4:
        city = cols[0].text.strip()
        local_time = cols[1].text.strip()

        condition = ""

        try:
            img = cols[2].find_element(By.TAG_NAME, "img")

            condition = (
                img.get_attribute("alt")
                or img.get_attribute("title")
                or ""
            ).strip()

        except:
            condition = cols[2].text.strip()
        temperature = cols[3].text.strip()

        data.append([
            city,
            local_time,
            condition,
            temperature
        ])

driver.quit()

df = pd.DataFrame(
    data,
    columns=[
        "City",
        "Local_Time",
        "Condition",
        "Temperature"
    ]
)

output_file = DATA_DIR / "raw_weather.csv"
df.to_csv(output_file, index=False)

print("✅ Scraping completed successfully")
print("📊 Total rows collected:", len(df))
print("📁 Saved to:", output_file)
print(df.head())