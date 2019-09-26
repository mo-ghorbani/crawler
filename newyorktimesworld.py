import requests
from bs4 import BeautifulSoup

categories = ['world', 'us', 'politics', 'opinion', 'nyregion','business', 'technology', 'science']

for category in categories:
    url = "https://www.nytimes.com/section/" + category
    s = requests.session()
    r = s.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')
    streamSection = soup.find("section", {"id":"stream-panel"})
    links = streamSection.findAll("a")

    for link in links:
        if link['href'][0] == '/':
            if link['href'][-5:] == '.html':
                print(link['href'])