#comprehensions
#syntax-[expressions for item in iterable]
#syntax-[expressions for item in iterable if condition]
#syntax-[expressions if else for item in iterable]

# list1=[x for x in range(1,11)]
# print(list1)

# list2=[x for x in range(1,11) if x%2==0]
# print(list2)

# list2=[]
# for x in range(1,11):
# 	if x%2==0:
# 		list2.append(x)
# print(list2)

# list3=[x if x>2 else x+2 for x in range(1,11)]
# print(list3)

# list3=[x+3 if x>2 else x+2 for x in range(1,11)]
# print(list3)

# var=[10,7,9,12,13]
# b=[x**2 for x in var]
# print(b)

# num=[10,20,30,40]
# num=[x*2 for x in num]
# print(num)

# str='iman1993'
# list=[x.isdigit() for x in str]
# print(list)

# str='iman1993'
# list=[x for x in str if x.isdigit()]
# print(list)

# str='iman1993'
# list=[x for x in str if x.isalpha()]
# print(list)

# list_1=[[1,2,3],['a','g','h'],['a','v','h']]
# print([x[0] for x in list_1])


# list comprehension with function

# def sqr(x):
# 	return x**2
# lst=[sqr(x) for x in range(1,11)]
# print(lst)

# a=[1,2,3]
# b=[1,2,3]
# print([x+y for x in a for y in b])


# a=[1,2,3]
# b=[1,2,3]
# c=[a[x]+b[x] for x in range(0,len(a))]
# print(c)

# a=[1,2,3]
# b=[1,2,3]
# ass=[]
# for x in range(0,len(a)):
# 	ass.append(a[x]+b[x])
# print(ass)



