from urllib import request
import re

def get_html(url):
    with request.urlopen(url) as f:
        data=f.read().decode('utf-8')
        return data

if __name__=='__main__':
    html=get_html('http://www.baidu.com')
    print(html)
    body=re.findall(r'<body>(.*)</body>',html)
    print(body)
