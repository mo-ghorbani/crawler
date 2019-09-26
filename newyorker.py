import requests
from bs4 import BeautifulSoup

url = "https://www.newyorker.com/latest"
s = requests.session()

# headers = {'Host': 'www.newyorker.com',
#            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
#            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#            'Accept-Language': 'en-US,en;q=0.5',
#            'Accept-Encoding': 'gzip, deflate, br',
#            'Connection': 'keep-alive',
#            'Pragma': 'no-cache',
#            'Cache-Control': 'no-cache'
# }
# r = s.get(url,headers=headers)
r = s.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
links = soup.findAll("div",{"class": "River__riverItemContent___2hXMG"})

for link in links:
    link=link.findAll('a')
    print(link[1]['href'])