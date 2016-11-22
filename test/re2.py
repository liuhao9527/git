#!/usr/bin/python3

import re
ma=input('Email:')
mail=re.compile(r'^\w+|\W+)@(\w+|\W+\).(\w{3-5}|\W{3-5})$')
if mail.match(ma):
    print('Right mail')
else:
    print('Error mail')
