#!/usr/bim/python
#def normalize(name):
#    return name.capitalize()
#L1=['wert','qwctT']
#l2=list(map(normalize,L1))
#print(l2)

from functools import reduce
#li=[1,3,4,5]
#def cj(x,y):
 #   return x*y
#def prod():
 #   va=reduce(cj,li)
  #  print(va)
#prod()

def f(x,y):
    return x*10+y
def shif(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
nu=reduce(f,map(shif,'123123'))
nu=nu/1000
print(nu)

