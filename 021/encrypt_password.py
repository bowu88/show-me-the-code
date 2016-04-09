# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'wzhuo'
__mtime__ = '2016/4/9'
"""
import os
from hashlib import sha256
from hmac import HMAC


def encrypt_pwd(pwd, salt=None):
	if salt is None:
		salt = os.urandom(8)  # 64 bits.
	pwd = pwd.encode('utf-8')
	result = pwd
	for i in range(10):
		result = HMAC(result, salt, sha256).digest()
	return salt + result


def validate_pwd(hashed, pwd):
	return hashed == encrypt_pwd(pwd, salt=hashed[:8])


if __name__ == '__main__':
	hashed = encrypt_pwd('secret')
	print(validate_pwd(hashed, 'secret'))
