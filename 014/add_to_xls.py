# coding:utf-8
import json
import codecs
import xlwt


def read_file(path):
    with codecs.open(path, 'r', 'utf-8') as f:
        return f.read()


def write_to_xls(con):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('stu')
    row = 0
    for k, v in con.items():
        col = 0
        ws.write(row, col, k)
        for value in v:
            col += 1
            ws.write(row, col, value)
        row += 1
    wb.save('stu.xls')


if __name__ == '__main__':
    content = read_file('stu.txt')
    content=json.loads(content)
    write_to_xls(content)
