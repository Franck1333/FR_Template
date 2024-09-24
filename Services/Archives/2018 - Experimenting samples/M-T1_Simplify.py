# -*- coding: utf-8 -*-
#https://dzone.com/articles/python-thread-part-1
#https://www.shanelynn.ie/asynchronous-updates-to-a-webpage-with-flask-and-socket-io/

import time
import threading #import Thread

def func1():
    print (' first func running')
    time.sleep(1)
    print (' first func done')

def func2():
    print (' second func running')
    time.sleep(1)
    print (' second func done')

threadFunc1 = threading.Thread(target=func1)
threadFunc1.start()

threadFunc2 = threading.Thread(target=func2)
threadFunc2.start()


threadFunc1.join()
threadFunc2.join()

if not threadFunc1.is_alive():
    print("threadFunc1 not Alive (working)")
    #why not re-start the thread so ?
