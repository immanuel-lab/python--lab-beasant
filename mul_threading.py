import  threading as t
import time

def f1():
	for i in range(5):
		time.sleep(1)
		print('hello world')
	

def f2():
	for j in range(5):
		time.sleep(1)
		print('immanuel')
	
start_time=time.time()
t1=t.Thread(target=f1)
t2=t.Thread(target=f2)	



t1.start()
t1.join()
t2.start()

t2.join()
end_time=time.time()
print('time for execution',end_time-start_time)