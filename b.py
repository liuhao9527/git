#!/usr/bin/python
import logging
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)**2
def main():
    try:
        b=bar('r')
        print(b)
        print('success')
    except Exception as e:
        logging.exception(e)
main()
print('End..')
