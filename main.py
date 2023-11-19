from bs4 import BeautifulSoup
import requests

req = Request(
        url='https://code.visualstudio.com/docs/python/tutorial-django', 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
response = requests.get(req)
print(response)
