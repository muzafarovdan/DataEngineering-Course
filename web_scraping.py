import requests
from bs4 import BeautifulSoup

url = 'https://www.drom.ru/pdd/themes/traffic_signs/'

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.2319 YaBrowser/23.9.0.2319 Yowser/2.5 Safari/537.36'
}

response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
tags = soup.find_all('img', class_='b-image b-image__image')

for i in range(len(tags)):
    link = tags[i].attrs['src']
    request = requests.get(url=link, headers=headers)

    with open(f'/Users/muzafarov/Desktop/MyEducation/DataEngineering-Course/Web_Scraping_img/{i+1}.jpg', 'wb') as file:
        file.write(request.content)
        print(f'Dowloaded {i+1} of {len(tags)}')

