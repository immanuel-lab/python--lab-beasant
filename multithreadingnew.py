import threading as t
import time


start_time=time.perf_counter()
def hello_loop():
    for _ in range(10):
        print("hello")


def bye_loop():
    for _ in range(10):
        print("bye")


print(f'number of threads {t.active_count()}')


t1=t.Thread(target=hello_loop,name='hellothread')
t2=t.Thread(target=bye_loop,name='byethread')
t1.start()

l=t.enumerate()

t2.start()


t1.join()



t2.join()
print(f'number of threads {t.active_count()}')


end_time=time.perf_counter()

print(f'number of threads {t.active_count()}')


print(f'time taken is {(end_time-start_time)*100000}')

for t in l:
    print(f'thread {t} with identification number {t.ident} is active')



