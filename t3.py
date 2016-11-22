#!/usr/bin/python3


import subprocess

print('$ nslookup')
p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err=p.communicate(b'set q=mx\npython.org\n exit \n')
print(output.decode('uft-8'))
print('Exit code:',r)
