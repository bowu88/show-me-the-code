#coding:utf-8
import re


def read_file(path):
    with open(path, 'rb') as f:
        return f.read().decode('utf-8')


if __name__ == '__main__':
    content = read_file(r'..\004\article.txt')
    words = {}
    s = set()
    L = re.findall(r'[0-9a-zA-Z]+', content)
    # collect word in content
    for word in L:
        if word not in s:
            words[word] = 1
            s.add(word)
        else:
            words[word] += 1
    #use sort
    a=sorted(words.items(),key=lambda x:x[1],reverse=True)
    print('most important word:',a[0])