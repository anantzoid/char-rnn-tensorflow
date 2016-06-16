import requests
from bs4 import BeautifulSoup as bs
import re
import unicodedata

def get_essay_links():
    url = 'http://www.aaronsw.com/2002/feeds/pgessays.rss'
    resp  = requests.get(url)
    f = open('pg_links.txt', 'w')
    for line in resp.text.split('\n'):
        if '<link>' in line:
            link = re.sub('<link>|<\/link>', '', line)  
            print link
            print >>f, link

f = open('pg_links.txt', 'r')
g = open('pg_essays.txt', 'a+')
for link in f.readlines():
    print link
    resp = requests.get(link.replace('\n',''))
    soup = bs(resp.text, "html.parser")
    print >>g, soup.find('title').text
    third_td = soup.findAll('td')[2]
    print >>g, unicodedata.normalize("NFKD", third_td.text).encode('utf-8')
    print >>g, '\n\n\n'
    
