# coding:utf-8
import xlrd
import json
import codecs


def read_xls(path):
    xls = xlrd.open_workbook(path)
    num_sheet = xls.sheet_by_name('num')
    L = []
    for i in range(num_sheet.nrows):
        L.append(num_sheet.row_values(i))
    return json.dumps(L)


def save_to_xml(data):
    with codecs.open('num.xml', 'w', 'utf-8') as f:
        head = r'''
        <?xml version="1.0" encoding="UTF-8"?>
<root>
<numbers>
<!--
    数字信息
-->
        '''
        tail = r'''
        </numbers>
</root>
        '''
        f.write(head)
        f.write(data)
        f.write(tail)


if __name__ == '__main__':
    xls = read_xls(r'..\016\num.xls')
    save_to_xml(xls)
