#!/usr/bin/python

l=[]
def a():
    for s in range(6):
        l.append(s)
        yield()
    return
print(a())

