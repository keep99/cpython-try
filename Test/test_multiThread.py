# -*- coding: utf-8 -*-
import threading
import time

def deadLoop1():
    while(1):
        a = 111
        print a
    # print "exit 11"
    
def deadLoop2():
    while(1):
        a = 222222
        print a
    # print "exit 22"

f1 = threading.Thread(target=deadLoop1)
f2 = threading.Thread(target=deadLoop2)

f1.start()
f2.start()

# time.sleep(10)

while(1):
    a = 333333333
    print a
   

while(1):
    a = "xxxxxxxxxxxxxx"
    print a

while(1):
    a = "pppppppppppppppppppppp"
    print a

f1.join()
f2.join()