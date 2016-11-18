#!/usr/bin/python

class FooError(ValueError):
    pass

def foo(s):
    n =int(s);
    if n==0:
        raise FooError('Error Value:%s'% s)
    
    print(10/n)
n=raw_input('Please your input  a number(not 0):')
foo(n)
