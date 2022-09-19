import requests 
from lxml import html

try:
    print("Url : ")
    url = input()
    navigator = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    requestOne = requests.get('https://www.fundamentus.com.br/', headers=navigator)
   
    if(requestOne.status_code == 200):
        page =  html.fromstring(requestOne.text)
        page.cssselect('a.home')
except:
    print("Response failed, você copiou certo a url?")
    
# finally:
#     print("Ocorreu tudo ok!")


# home 
# consciente 
# mais-opcoes 
# contato