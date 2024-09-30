import requests
from bs4 import BeautifulSoup

url = "https://www.google.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract data from the webpage
# data = soup.find("input", {"aria-label": "Google Search"}).text
# print(data)


# Extract all the titles (example: h2 tags)
titles = soup.find_all('<a')
for title in titles:
    print(title.text)






# import requests
# from bs4 import BeautifulSoup

# # URL of the webpage to scrape
# url = "https://example.com"

# # Send a GET request to the webpage
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# # Extract all the titles (example: h2 tags)
# titles = soup.find_all('h2')
# for title in titles:
#     print(title.text)

                           