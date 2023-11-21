from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json
import re
# fridg_models = ['RSSE445M25WN', 'RF23R62E3B1']
fridg_models_input = input('input samsung regrigerator model code here: ')
parameres= f'samsung+refrigerator+model+{fridg_models_input}+kwh'
url = 'https://www.google.com/search?q=' + parameres
headers = {
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15"
}

req = Request(url, headers=headers)

# Open the URL and read its content
response = urlopen(req)

# Check the content type
content_type = response.getheader('Content-Type')

if 'text/html' in content_type:
    # If it's HTML, use BeautifulSoup
    soup = BeautifulSoup(response.read(), 'html.parser')
    soup.prettify()
    results=soup.find_all( 'div', class_='tF2Cxc' ) 
    # description_results=soup.find_all( 'div', class_='VwiC3b' ) 
    
    for i in results:
        title = i.find('h3').text
        link = i.find('a')['href']
        description = i.find(class_='VwiC3b')
        # bold_words=  i.find('em')         
        
        text = description.text.strip()
        power_rate_match = re.search(r'(\d+\s*kwh)', text, re.IGNORECASE)
        power_rate = power_rate_match.group(1) if power_rate_match else None

        if power_rate:
            print(f"Title: {title}")
            print(f"Power Rate: {power_rate}")
            print()
            break  # Stop processing other snippet elements if power rate is found

    if not power_rate:
        print(f"Title: {title}")
        print("Power Rate not found")
        print()
       
elif 'application/json' in content_type:
    # If it's JSON, you can load it as a JSON object
    json_data = json.loads(response.read().decode('utf-8'))
    print(json_data)
else:
    # Handle other content types accordingly
    print(f"Unsupported content type: {content_type}")

# Close the response
response.close()

