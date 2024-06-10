import requests
from bs4 import BeautifulSoup

url = "https://garage-r.co.jp/cars/184153"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
title = soup.find("h3")
print(title)