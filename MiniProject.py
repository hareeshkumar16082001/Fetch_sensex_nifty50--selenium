import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Sensex")
search_box.submit()
try:
    market_value_sensex = driver.find_element(By.XPATH, "//span[@class='IsqQVc NprOob wT3VGc']").text
    market_change_sensex = driver.find_element(By.XPATH, "//span[@class='IsqQVc NprOob wT3VGc']").text
    print(f"At {datetime.datetime.now()} - Sensex: {market_value_sensex}, Change: {market_change_sensex}")
except Exception as e:
    print("Failed to retrieve Sensex data:", e)
search_box = driver.find_element(By.NAME, "q")
search_box.clear()
search_box.send_keys("Nifty 50")
search_box.submit()
try:
    market_value_nifty = driver.find_element(By.XPATH, "//span[@class='IsqQVc NprOob wT3VGc']").text
    market_change_nifty = driver.find_element(By.XPATH, "//span[@class='IsqQVc NprOob wT3VGc']").text
    print(f"At {datetime.datetime.now()} - Nifty 50: {market_value_nifty}, Change: {market_change_nifty}")
except Exception as e:
    print("Failed to retrieve Nifty 50 data:", e)
time.sleep(5)
driver.quit()
