import re
import codecs

f = codecs.open('article.txt', 'r', 'utf-8')
content = f.read()
f.close()
print(len(re.findall(r'[0-9a-zA-Z]+',content)))