import json
import codecs
import xlwt


def read_file(path):
    with codecs.open(path, 'r', 'utf-8') as f:
        return f.read()


def write_to_xls(content):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('city')
    row = 0
    for k, v in content.items():
        ws.write(row, 0, k)
        ws.write(row, 1, v)
        row += 1

    wb.save('city.xls')


if __name__ == '__main__':
    content = read_file('city.txt')
    content = json.loads(content)
    write_to_xls(content)
