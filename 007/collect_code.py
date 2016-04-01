# coding:utf-8
import re


def read_file(path):
    with open(path, 'rb') as f:
        return f.read().decode('utf-8')


if __name__ == "__main__":
    content = read_file(r'..\006\collect_important_word.py')
    all_line = re.findall(r'.*\n', content)
    print('all lines are %s' % len(all_line))
    anno_line = re.findall(r'.*#.*\n', content)
    print('annotation lines are %s' % len(anno_line))
    # 不知道怎么匹配了
    code_line = re.findall(r'[0-9a-zA-Z]{1}.*\r\n', content)
    print('code lines are %s' % len(code_line))
