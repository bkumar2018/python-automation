import requests
from bs4 import BeautifulSoup

url = "https://www.google.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract data from the webpage
data = soup.find("input", {"aria-label": "Google Search"}).text
print(data)
                           