from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = Options()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://logs.tf")
driver.maximize_window()

allLogsTable = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/table/tbody')

allLogsNames = []

for log in allLogsTable.find_elements(By.XPATH, '//tr'):

    row = [item.text for item in log.find_elements(By.XPATH, './/td')]
    allLogsNames.append(row)

for log in allLogsNames:
    print("\n")
    print(log)





