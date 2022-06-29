##
##import threading
##import time
##def fun():
##    for x in range(0,5):
##         print("immanuel")
##         time.sleep(2)
##   
##def gun():
##    for x in range(0,5):
##        print("joshua")
##t1=threading.Thread(target=fun)
##t2=threading.Thread(target=gun)
##   
##t1.start()
##t2.start()

##import time as t
##
##for x in range(6):
##    print("immanuel")
##    t.sleep(2)



from threading import*
print("hello world",current_thread().getName())















