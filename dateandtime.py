 # import datetime

# d=datetime.date(2024,7,14)
# d=datetime.date.today()
# d=datetime.date.today().weekday()
# d=datetime.date.today().isoweekday()

# TIMEDELTA

# d=datetime.date.today()
# td=datetime.timedelta(days=7)

# print(d+td)


# calculation of current birthday

# today=datetime.date.today()
# bday=datetime.date(2024,8,6)
# time_delta=bday-today
# # print(time_delta)
# # print(time_delta.days)
# print(time_delta.total_seconds())

# time=datetime.time(11,12,12)
# print(time.hour)
# print(time.minute)

# from datetime import datetime

# current_time = datetime.now()
# print(current_time.time())


# import time

# start = time.perf_counter()
# time.sleep(5)
# end = time.perf_counter()
# print(f"Duration: {end - start} seconds")


import time

start_time = time.time()
time.sleep(2)
for x in range(5):
    print("hello")
end_time = time.time()
print(f"time taken is {end_time-start_time}")











