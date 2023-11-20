from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json

url = 'https://studies.cs.helsinki.fi/stats-mock/api/courses'
headers = {'User-Agent': 'Mozilla/5.0'}

req = Request(url, headers=headers)

# Open the URL and read its content
response = urlopen(req)

# Check the content type
content_type = response.getheader('Content-Type')

if 'text/html' in content_type:
    # If it's HTML, use BeautifulSoup
    soup = BeautifulSoup(response.read(), 'html.parser')
    print(soup)
elif 'application/json' in content_type:
    # If it's JSON, you can load it as a JSON object
    json_data = json.loads(response.read().decode('utf-8'))
    print(json_data)
else:
    # Handle other content types accordingly
    print(f"Unsupported content type: {content_type}")

# Close the response
response.close()

