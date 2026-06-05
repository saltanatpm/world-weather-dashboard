from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get("https://www.timeanddate.com/weather/")

time.sleep(5)
data = []

#real table rows
rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
for row in rows:
    try:
        cols = row.find_elements(By.TAG_NAME, "td")
        city = cols[0].text
        temp = cols[1].text
        condition = cols[2].text
        data.append([city, temp, condition])
    except:
        continue
driver.quit()

df = pd.DataFrame(data, columns=["City", "Temperature", "Condition"])
df.to_csv("data/raw_weather.csv", index=False)

print("Scraping complete:", df.shape)
