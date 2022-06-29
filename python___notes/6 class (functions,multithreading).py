#FUNCTIONS
##group of related statments that perform specific task
##it can be exprecuted only if called
##code reusability ,modular,better understanding
##
##
##def new():
##    print("success")
##new()
          
##def new(a):
##    print(a)
##new("dhoni")

##def new(a,b):
##    print(a+b)
##
##new(10,20)
##new(30,40)
##new(50,60)
##
##def nxt(name,avg):
##    print(name,"has average" ,avg)
##nxt("dhoni",59)
##
##def nxt(name,avg="NA"):
##    print(name,"has average" ,avg)
##nxt("dhoni")

##def nxt(name="dhoni",avg):
##    print(name,"has an average" ,avg)
##nxt(59)

##def nxt(avg,name="dhoni"):
##    print(name,"has an average" ,avg)
##nxt(59)

##
##def nxt(name,avg):
##    print(name,"has an average" ,avg)
##nxt(avg=59,name="dhoni")

##
##def new(a,b):
##    print("success")
##    print(a+b)
##    return "good"
##new(10,20)

##def new(a,b):
##    print("success")
##    print(a+b)
##    return "good"
##print(new(10,20))

##def new(a,b):
##    print("success")
##    return "good"
##    print(a+b)
##    
##print(new(10,20))

##def new(a,b):
##    return "good"
##    print("success")
##   
##    print(a+b)
##    
##print(new(10,20))

def new(*a):
    print(a)
new(10)
new(20,30)
new(40,50,60)
##
##def new(**a):
##    print(a)
##new(a=10)
##new(b=20,c=30)

#MULTITHREADING
##import time
##def fun():
##    print("one")
##    print(time.ctime())
##    time.sleep(2)
##def fun1():
##    print("two")
##    print(time.ctime())
##fun()
##fun1()
##               
##import threading      
##import time
##def fun():
##    print("one")
##    print(time.ctime())
##    time.sleep(2)
##def fun1():
##    print("two")
##    print(time.ctime())
##t1=threading.Thread(target=fun)
##t2=threading.Thread(target=fun1)
##t1.start()
##t2.start()
##print("good")
##
##import time
##import threading
##def fun(a):
##    print("success",a)
##    print(time.ctime())
##def fun1(a):
##    print("good",a)
##    print(time.ctime())
##t1=threading.Thread(target=fun,args="dhoni")
##t2=threading.Thread(target=fun1,args="kohli")
##t1.start()
##t2.start()
##
##import time
##import threading
##def fun(a):
##    print("success",a)
##    print(time.ctime())
##def fun1(a):
##    print("good",a)
##    print(time.ctime())
##t1=threading.Thread(target=fun,args=("dhoni",))
##t2=threading.Thread(target=fun1,args=("kohli",))
##t1.start()
##t2.start()


##import time
##import threading
##def fun(name):
##    new()
##    print(name,x)
##x=0
##def new():
##    global x
##    x+=1
##t1=threading.Thread(target=fun,args=("dhoni",))
##t2=threading.Thread(target=fun,args=("kohli",))
##t1.start()
##t2.start()

##import time
##import threading
##def fun(name,L):
##    L.acquire()
##    new()
##    print(name,x)
##    L.release()
##x=0
##def new():
##    global x
##    x+=1
##L=threading.Lock()
##t1=threading.Thread(target=fun,args=("dhoni",L))
##t2=threading.Thread(target=fun,args=("kohli",L))
##t1.start()
##t2.start()          #gil global interpreter lock












































































