# coding:utf-8
import re


def get_key(path):
    with open(path, 'rb') as f:
        content = f.read().decode('utf-8')
        words = re.split(r'\r\n', content)
        return words


if __name__ == '__main__':
    words = get_key(r'..\011\filtered_words.txt')
    while True:
        word = input('输入内容:\n')
        for key in words:
            if key in word:
                print(word.replace(key,'**'))
