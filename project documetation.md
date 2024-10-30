
---

# Laptop Data Scraping from Flipkart

This project demonstrates web scraping using **Selenium**, **BeautifulSoup**, and **Pandas** to collect and organize data on laptops from the Flipkart website. As my first web scraping project, it provided valuable experience in data extraction and data management.

---

### Project Purpose

The primary goal of this project is to collect data on laptop names and prices from Flipkart, a popular e-commerce website. I chose to use **Selenium** for browser automation, **BeautifulSoup** for HTML parsing, and **Pandas** for data manipulation and storage.

---

### Code Walkthrough

Below is the code with explanations of each part:

```python
# Import required libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
```

1. **Libraries Used**:
   - `selenium`: For automating browser interactions.
   - `webdriver_manager`: Manages ChromeDriver installation.
   - `bs4` (`BeautifulSoup`): Parses HTML content.
   - `pandas`: Manages and saves data in CSV format.

```python
# Initialize WebDriver using webdriver_manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service) 
```

2. **Initialize WebDriver**:
   - Sets up the Chrome WebDriver to automate a Chrome browser instance using `webdriver_manager` to install ChromeDriver automatically.

```python
# Lists to store data
products = []
prices = []
```

3. **Data Storage**:
   - Creates empty lists (`products` and `prices`) to store the scraped laptop names and prices.

```python
# Fetch the page
url = "https://www.flipkart.com/search?q=Laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&as-pos=1&as-type=HISTORY&as-backfill=on"
driver.get(url)
```

4. **Fetch the URL**:
   - Opens the Flipkart laptops search page for data extraction.

```python
# Parse HTML content using BeautifulSoup
description = driver.page_source
soup = BeautifulSoup(description, 'html.parser')
```

5. **Parse HTML Content**:
   - Retrieves the HTML content of the page using Selenium’s `page_source`.
   - Parses it with BeautifulSoup to make HTML elements accessible for scraping.

```python
# Loop through items and collect data
for item in soup.find_all(attrs={'class': 'CGtC98'}):  
    name = item.find('div', attrs={'class': 'KzDlHZ'})  
    price = item.find('div', attrs={'class': 'Nx9bqj _4b5DiR'})  # Updated class name
    if name and price:  
        products.append(name.text)
        prices.append(price.text)
```

6. **Extract and Store Data**:
   - Loops through each product item by targeting the relevant CSS classes for name and price.
   - Extracts the text content of each element and appends it to the `products` and `prices` lists.

```python
# Create DataFrame and save to CSV
df = pd.DataFrame({'Name': products, 'Price': prices})
df.to_csv('laptop.csv', index=False, encoding='utf-8')
```

7. **Store Data in CSV**:
   - Converts the collected data into a `pandas` DataFrame.
   - Exports the DataFrame to a CSV file (`laptop.csv`) for future reference and analysis.

```python
# Close the WebDriver
driver.quit()
```

8. **Close WebDriver**:
   - Terminates the WebDriver session, closing the Chrome browser.

---

### Project Insights

This project offered me hands-on experience in web scraping, browser automation, and data handling with CSV files. By working with three essential tools—Selenium, BeautifulSoup, and Pandas—I gained a better understanding of:

- **Dynamic content extraction** using Selenium.
- **HTML parsing** with BeautifulSoup.
- **Data structuring** and saving using Pandas.

This project has sparked my interest in further developing web scraping skills and exploring more complex data extraction tasks.

---