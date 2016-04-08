# coding:utf-8
import xlrd
import json
import codecs


def read_xls(path):
    xls = xlrd.open_workbook(path)
    city_sheet = xls.sheet_by_name('city')
    data = {}
    for i in range(city_sheet.nrows):
        data[city_sheet.row_values(i)[0]] = city_sheet.row_values(i)[1:]
    return json.dumps(data, ensure_ascii=False)


def save_to_xml(data):
    with codecs.open('city.xml', 'w', 'utf-8') as f:
        head = r'''
            <?xmlversion="1.0" encoding="UTF-8"?>
<root>
<citys>
<!--
    城市信息
-->
        '''
        tail = r'''
            </citys>
</root>
        '''
        f.write(head)
        f.write(data)
        f.write(tail)


if __name__=='__main__':
    xls = read_xls(r'..\015\city.xls')
    save_to_xml(xls)