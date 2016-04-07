import json
import xlwt


def get_data(path):
    with open(path, 'rb') as f:
        content = f.read().decode('utf-8')
    return json.loads(content)


def save_file(content):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('num')
    row = 0
    for ll in content:
        col = 0
        for value in ll:
            ws.write(row, col, value)
            col += 1
        row += 1
    wb.save('num.xls')


if __name__ == '__main__':
    content = get_data('num.txt')
    save_file(content)
