# Import required libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

# Initialize WebDriver using webdriver_manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service) 

# Lists to store data
products = []
prices = []

# Fetch the page
url = "https://www.flipkart.com/search?q=Laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&as-pos=1&as-type=HISTORY&as-backfill=on"
driver.get(url)

# Parse HTML content using BeautifulSoup
description = driver.page_source
soup = BeautifulSoup(description, 'html.parser')

# Loop through items and collect data
for item in soup.find_all(attrs={'class': 'CGtC98'}):  
    name = item.find('div', attrs={'class': 'KzDlHZ'})  
    price = item.find('div', attrs={'class': 'Nx9bqj _4b5DiR'})  # Updated class name
    if name and price:  
        products.append(name.text)
        prices.append(price.text)

# Create DataFrame and save to CSV
df = pd.DataFrame({'Name': products, 'Price': prices})
df.to_csv('laptop.csv', index=False, encoding='utf-8')

# Close the WebDriver
driver.quit()