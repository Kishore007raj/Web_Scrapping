from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Correct import
import time #for some long time process

# Provide the path to the chromedriver executable
service = Service(executable_path="chromedriver.exe")

# Initialize the webdriver with the service
driver = webdriver.Chrome(service=service)

# Open the Google homepage in the browser
driver.get("https://www.google.com/")

time.sleep(10)

driver.quit()