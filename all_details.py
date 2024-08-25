import requests
from bs4 import BeautifulSoup

url=requests.get("http://127.0.0.1:8000/")
print(url.content)
soup = BeautifulSoup(url.text, 'html.parser')
print(soup.find(id="loginEmail"))
print(soup.find(id="loginPassword"))