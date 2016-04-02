# coding:utf-8
import re
from bs4 import BeautifulSoup
from urllib import request


def get_html(url):
    with request.urlopen(url) as resp:
        if resp.status != 200:
            return ''
        return resp.read().decode('utf-8')


def parse_html(html):
    bs = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    imgs = bs.find_all('img')
    urls = set()
    for link in imgs:
        url = link['src']
        urls.add(url)
    return urls


def download_img(urls):
    for url in urls:
        img = request.urlopen(url).read()
        filename = re.findall(r'\/([0-9a-zA-Z]+\.jpg)', url)
        if filename == '' or len(filename) == 0:
            continue
        filename = filename[0]
        f = open(filename, 'wb')
        f.write(img)
        f.close()


if __name__ == '__main__':
    url = r'http://tieba.baidu.com/p/3756942593'
    html = get_html(url)
    urls = parse_html(html)
    download_img(urls)
