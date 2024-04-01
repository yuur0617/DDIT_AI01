from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("http://localhost:8888/MVVM_EMP/emp.html")

# print(driver.page_source)

time.sleep(2)

tables = driver.find_elements(By.CSS_SELECTOR, 'table')
trs = tables[0].find_elements(By.CSS_SELECTOR, 'tr')

for idx, tr in enumerate(trs):
    if idx == 0:
        continue
    tds = tr.find_elements(By.CSS_SELECTOR, 'td')
    print(tds[1].text, tds[3].text)
