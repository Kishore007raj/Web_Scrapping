
---

# Demo Projects Documentation

### 1. **Requests - Checking Website Status Code and HTML Content**

This code uses the `requests` library to fetch and display the HTTP status code and HTML content of the Netflix India homepage.

```python
import requests as rq

demo = rq.get("https://www.netflix.com/in/")
print(demo.status_code)
print(demo.text)
```

- **Imports**: `requests` (as `rq` for simplicity).
- **Key Functions**:
  - `rq.get(url)`: Sends an HTTP GET request to the specified URL.
  - `demo.status_code`: Returns the status code of the response (e.g., `200` for a successful request).
  - `demo.text`: Returns the HTML content of the page as a string.
- **Output**:
  - `demo.status_code`: Printed to show if the request was successful.
  - `demo.text`: Printed to display the raw HTML content of the webpage.

---

### 2. **BeautifulSoup - Parsing Webpage Content and Extracting Links**

This code uses the `requests` and `BeautifulSoup` libraries to fetch and parse the LinkedIn homepage, extract the title, and gather all hyperlinks (`<a>` tags with `href` attributes).

```python
from bs4 import BeautifulSoup
import requests

r = requests.get("https://linkedin.com") # Fetch HTML Page
soup = BeautifulSoup(r.text, "html.parser") # Parse HTML Page

if soup.title is not None:
    print("Webpage Title:", soup.title.string)
else:
    print("No title found")

print("Fetch All Links:", [a['href'] for a in soup.find_all('a', href=True)])
```

- **Imports**:
  - `requests`: Used to make an HTTP request.
  - `BeautifulSoup` from `bs4`: Parses HTML content.
- **Key Functions**:
  - `requests.get(url)`: Retrieves HTML content from the specified URL.
  - `BeautifulSoup(html, "html.parser")`: Parses HTML content using the HTML parser.
  - `soup.title.string`: Extracts and prints the title of the webpage.
  - `[a['href'] for a in soup.find_all('a', href=True)]`: Finds and prints all `href` links in `<a>` tags.
- **Output**:
  - `Webpage Title`: Displays the page title if available.
  - `Fetch All Links`: Displays all URLs within `<a>` tags.

---

### 3. **Selenium - Automating Web Browser Actions**

This code uses the `selenium` library to open the Chrome browser, navigate to the Google homepage, wait for 10 seconds, and then close the browser.

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Correct import
import time # for some long time process

# Provide the path to the chromedriver executable
service = Service(executable_path="chromedriver.exe")

# Initialize the webdriver with the service
driver = webdriver.Chrome(service=service)

# Open the Google homepage in the browser
driver.get("https://www.google.com/")

time.sleep(10)

driver.quit()
```

- **Imports**:
  - `webdriver` from `selenium`: Controls the web browser.
  - `Service` from `selenium.webdriver.chrome.service`: Manages the Chrome WebDriver service.
  - `time`: Used for pausing execution.
- **Key Functions**:
  - `Service(executable_path="chromedriver.exe")`: Sets up the path to the ChromeDriver executable.
  - `webdriver.Chrome(service=service)`: Initializes Chrome WebDriver with the specified service.
  - `driver.get(url)`: Opens the given URL in Chrome.
  - `time.sleep(seconds)`: Pauses the program for the specified number of seconds.
  - `driver.quit()`: Closes the browser session.
- **Output**:
  - This code doesn’t produce any console output but opens and closes the Google homepage in a browser window.

---