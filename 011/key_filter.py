# coding:utf-8
import re


def get_key(path):
    with open(path, 'rb') as f:
        content = f.read().decode('utf-8')
        key = re.split(r'\r\n', content)
        words = set(key)
        return words


if __name__ == '__main__':
    words = get_key('filtered_words.txt')
    while True:
        word=input('输入内容:\n')
        if word in words:
            print('Freedom')
        else:
            print('Human Rights')
