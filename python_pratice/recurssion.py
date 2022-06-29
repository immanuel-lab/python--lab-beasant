
#recussion

# def f(n):
# 	if n==0:
# 		return 0
# 	else:
# 		return f(n-1)+20
# print(f(5))


#using recurssion
# def fact1(num):
# 	if num==0:
# 		return 1
# 	else:
# 		return num*fact1(num-1)
# print(fact1(5))

# find sum from n to n-1
# def sum(num):
# 	if num==1:
# 		return 1
# 	else:
# 		return num+sum(num-1)
# print(sum(5))

#fibannocci series

# 0 1 1 2 3 5 8 13

# 0 1 2 3 4 5 6 7 8

# def fib(n):
# 	if n==0 or n==1:
# 		return n
# 	else:
# 	  return fib(n-1)+fib(n-2)
# print(fib(6))



# 0 1 1 2 3 5 8 13

# 0 1 2 3 4 5 6 7 8

def fib(n):
	if n<=1:
      return n
	else:
	  return fib(n-1)+fib(n-2)
for x in range(10):
	print(fib(x))

