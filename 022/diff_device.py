# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'wzhuo'
__mtime__ = '2016/4/9'
"""
from PIL import Image


def chage_resolution(path, devW, devH):
	im = Image.open(path)
	w, h = im.size
	wtimes = float(w) / devW
	htimes = float(h) / devH
	if wtimes > 1 or htimes > 1:
		times = wtimes if wtimes > htimes else htimes
	else:
		times = 1
	im.resize((int(w / times), int(h / times)))
	name = 'resolution' + str(devH) + '-' + str(devW) + '.jpg'
	im.save(name, 'jpeg')


if __name__ == '__main__':
	devs = {}
	path = r'..\005\resolution.jpg'
	devs['ip6'] = (1334, 750)
	devs['ip6p'] = (1920, 1080)
	for k, v in devs.items():
		chage_resolution(path, v[0], v[1])
