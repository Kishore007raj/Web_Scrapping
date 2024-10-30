from bs4 import BeautifulSoup
import requests
r = requests.get("https://linkedin.com") #Fetch HTML Page
soup = BeautifulSoup(r.text, "html.parser") #Parse HTML Page
if soup.title is not None:
    print("Webpage Title:", soup.title.string)
else:
    print("No title found")
print("Fetch All Links:", [a['href'] for a in soup.find_all('a', href=True)])

