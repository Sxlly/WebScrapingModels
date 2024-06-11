from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


options = Options()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://logs.tf")





