from urllib import request
from bs4 import BeautifulSoup
import re


def get_html(url):
    with request.urlopen(url) as f:
        data = f.read().decode('utf-8')
        return data


if __name__ == '__main__':
    html = get_html('http://txiner.top')
    print(html)
    bs=BeautifulSoup(html)
    links=set()
    for link in bs.find_all('a'):
        links.add(link['href'])
    print(links)
