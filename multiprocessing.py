import multiprocessing as mp
import time



start_time = time.perf_counter()

c_list=[]
b_list=[]
a_list=[]


def a():
    for i in range(90000000000):
        a_list.append(i)

def b():
    for i in range(100000000):
        b_list.append(i)

def c():
    for i in range(100000000):
        c_list.append(i)





p1 = mp.Process(target=a)
p2 = mp.Process(target=b)
p3 = mp.Process(target=c)

p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()





end_time = time.perf_counter()

print(f'the time taken is {end_time-start_time}')