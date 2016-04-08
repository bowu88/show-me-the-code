# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'wzhuo'
__mtime__ = '2016/4/8'
"""

import xlrd
import re


def read_xls(path):
	xls = xlrd.open_workbook(path)
	call_sheet = xls.sheet_by_name('call')
	call = []
	becalled = []
	for i in range(1, call_sheet.nrows):
		if call_sheet.row_values(i)[3] == '主叫':
			call.append(call_sheet.row_values(i)[2])
		else:
			becalled.append(call_sheet.row_values(i)[2])
	return call, becalled


def cal_sec(info):
	time_info = re.compile(r'(\d+)*分*(\d+)*秒')
	res = re.match(time_info, info).groups()
	if res[-1] == None:
		return int(res[0])
	else:
		return int(res[0]) * 60 + int(res[1])


def get_msg(phone):
	length = len(phone)
	phone = list(map(cal_sec, phone))
	# reduce报错，不知道为什么
	# t = reduce(lambda x, y: x + y, phone)
	t = 0
	for i in phone:
		t = t + i
	return length, t


if __name__ == '__main__':
	call, becalled = read_xls('call_record.xls')
	print('一共拨打%s个电话，总时长%s' % get_msg(call))
	print('一共接听%s个电话，总时长%s' % get_msg(becalled))
