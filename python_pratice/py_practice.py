# swap two variables without using third variable
# x,y=20,30

# x=x+y
# y=x-y
# x=x-y
# print('the value of x and y is:',x ,'and',y )

#FACTORIAL WITH 3 TYPES
# import math
# print(math.factorial(5))

#using recurssion
# def fact1(num):
# 	if num==0:
# 		return 1
# 	else:
# 		return num*fact1(num-1)
# print(fact1(5))

#using loop

# def fact2(num):
# 	fact=1
# 	for x in range(1,num+1):
# 		fact=fact*x
# 	return fact
# print(fact2(5))


# fact=1
# n=5
# for i in range(1,n+1):
# 	fact=fact*i
# print(fact)


#palindrome

# def ispdrome(var):
# 	str=var[::-1]
# 	if str==var:
# 		print('is palindrome')
# 	else:
# 		print('not palindrome')
# ispdrome('stsr')

#Reverse a number

# def rev_num(num):
# 	sum=0
	

# 	while(0<num):
# 		rem=num%10
# 		sum=(sum*10)+rem
# 		num=num//10
# 	return sum	
# print(rev_num(12345))

		

# print(rev_num(123))

# num=12345
# rev_num=str(num)
# num1=rev_num[::-1]

# num2=int(num1)
# print(num2)

# walrus operator 
#new to python 3.8
#assigns values to variables as a part of larger expression


# print(happy:='imman')
# print('walrus operator',happy)

# using while loop

# foods=list()
# i=0
# while :
# 	food=input("what food you like:")

# 	foods.append(food)
# 	i+=1

# happy = True
# print(happy)

# print(happy := True)

# foods = list()
# while True:
#   food = input("What food do you like?: ")
#       if food == "quit":
#           break
#   foods.append(food)
 
 # using walrus operator
# foods = list()
# while food := input("What food do you like?: ") != "quit":
#     foods.append(food)

# nums=[]
# num=input("type a number:")
# while num.isdigit():
# 	nums.append(int(num))
# 	num=input("type a number:")


#Leap year

# year=int(input("enter the year:"))
# if(year%4==0 and year%100!=0)or year%400==0:
# 	print("is leap year")
# else:
# 	print("not leap year")

# year=int(input("enter the year:"))
# if(year%4==0):
	
# 	if(year%100==0):
		
# 		if(year%400==0):
# 			print("leap year")
# 		else:
# 			print("not leapyear")
# 	else:
# 		print("leapyear")
# else:
# 	print("not leapyear")

# year=1700
# import calender as cal
# print(cal.isleap(year))

#FIBANOCCI SERIES

# 0 1 1 2 3 5 8 13

# 0 1 2 3 4 5 6 7 

# n=2
# if(n==1):
#     print(0)
# else:
#     a=0
#     b=1
#     print(0)
#     print(1)
#     for x in range(2,n):
#         c=a+b
#         print(c)
#         a=b
#         b=c

#ARMSTRONG NUMBER

# def isarms(n):
# 	sum=0
# 	arms=n
# 	while(0<n):
# 		r=n%10
# 		sum=sum+(r*r*r)
# 		n=n//10
# 	if sum==arms:
# 		return'ARMSTRONG num'
# 	else:
# 		return 'not armstrong num'
# print(isarms(153))

# ARMSTRONG NUMBER
#153=1*1*1+5*5*5+3*3*3
# num=153
# sum=0
# temp=num
# while(temp>0):
#     r=temp%10
#     sum+=r**3
#     temp=temp//10
# if(num==sum):
#     print("armstrong number")
# else:
#     print("not armstrong number")