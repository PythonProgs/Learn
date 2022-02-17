import requests
from bs4 import BeautifulSoup

content=requests.get('https://bmkg.go.id')
print(content.status_code)