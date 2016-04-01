# coding:utf-8
import mysql.connector
import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def create_code(num, length):
    codes = set()
    i = 0
    while i < num:
        answer = ''
        for j in range(length):
            answer += random.choice(chars)
        if answer not in codes:
            codes.add(answer)
            i += 1
        else:
            continue
    return codes


if __name__ == '__main__':
    conn = mysql.connector.connect(user='root', password='', database='test')
    cursor = conn.cursor()
    cursor.execute(
        'create table if not exists activatecode(id int auto_increment primary key,code varchar(30))')
    codes = create_code(50, 10)
    for code in codes:
        cursor.execute('insert into activatecode(code) VALUES (%s)', [code])
        conn.commit()
    cursor.close()
    conn.close()
