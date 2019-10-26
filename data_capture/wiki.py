from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

resp=urlopen('https://en.wikipedia.org/wiki/Main_Page').read().decode('utf-8')
soup=BeautifulSoup(resp,'html.parser')
listUrls=soup.find_all('a',href=re.compile(r'^/wiki/'))

for url in listUrls:
    if not re.search('\.(jpg|JPG)$',url['href']):
        print(url.get_text(),'<----->','https://en.wikipedia.org'+url['href'])
