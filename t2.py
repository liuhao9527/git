#!/usr/bin/python3
import os
from multiprocessing import Process

def run_proc(name):
    print('Run child process %s (%s)...' %(name,os.getpid()))

if __name__=='__main__':
    print('Parent process %s.'% os.getpid())
    p=Process(target=run_proc,args=('test',))
    print('Child Process will start.')
    p.start()
    p.join()
    print('Child process end.')
