# coding:utf-8
import random


# 从ascii表获取随机数据
def create_code(num, length):
    codes = set()
    i = 0
    while i < num:
        answer = ''
        for j in range(length):
            answer += chr(random.randint(48, 123))
        if answer not in codes:
            codes.add(answer)
            i += 1
        else:
            continue
    return codes


if __name__ == '__main__':
    chars = 'abcdefghijklmnopqrstuvwxyz'
    res = create_code(100, 20)
    for code in res:
        print('%s'%code)
        # print(code)
    # print(res)
    print(chars.upper())
