#!/usr/bin/python
#-*-coding:utf-8-*-
import hashlib

md5=hashlib.md5()
md5.update('how to use md5'.encode('utf-8'))
md5.update(' in pythow hashlib?'.encode('utf-8'))
print(md5.hexdigest())
