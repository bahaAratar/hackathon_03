import requests
from bs4 import BeautifulSoup as BS
from decouple import config

URL = config('SITE_URL')
r = requests.get(URL)
print(r.json())

