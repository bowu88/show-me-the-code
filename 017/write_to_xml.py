# coding:utf-8
import xlrd
import json
import codecs


def read_xls(path):
	exl = xlrd.open_workbook(path)
	exl_sheet = exl.sheet_by_name('stu')
	data = {}
	for i in range(exl_sheet.nrows):
		data[exl_sheet.row_values(i)[0]] = exl_sheet.row_values(i)[1:]
	return json.dumps(data, ensure_ascii=False)


def write_to_xml(data):
	L = []
	head = r'''
    <?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!--
    学生信息表
    "id" : [名字, 数学, 语文, 英文]
-->
    '''
	L.append(head)
	L.append(data)
	tail = r'''
        </students>
</root>
    '''
	L.append(tail)

	fcontent = ''.join(L)
	with codecs.open('stu.xml', 'w', 'utf-8') as f:
		f.write(fcontent)


if __name__ == '__main__':
	xls = read_xls(r'..\014\stu.xls')
	write_to_xml(xls)
