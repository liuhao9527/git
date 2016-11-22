#!/usr/bin/python3

import re,io

test=input('Please input a number:')
if re.match(r'\d{3}\-\d{5,9}',test):
    print('The number is a telphone number!')
else:
    print('The number is not a tel')
