#!/usr/bin/python

try:
    print('try..')
    r=10/int('3')
    print('result:success',r)
except ZeroDivisionError as e:
    print('except:',e)
except ValueError as e:
    print('except:',e)
else:
    print('have not error')
finally:
    print('finally..')
print('END')
