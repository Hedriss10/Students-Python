import requests
from bs4 import BeautifulSoup


url = 'https://casino.bet365.com/Play/LiveRoulette'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for pergunta in html.select('html'):
    print(pergunta)
