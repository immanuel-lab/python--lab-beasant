# var=[10,7,9,12,13]
# a=[]
# # for x in var:
# #     b=x**2
# #     a.append(b)
# #
# # print(a)
#
# var=[10,7,9,12,13]
# a=[]
# b=[x**2 for x in var]
# print(b)


# var=[10,7,9,12,13]
# a=[]
# for x in var:
#     if(x%2==0):
#      a.append(x)
#
# print(a)

# var=[10,7,9,12,13]
# a=[]
# b=[x for x in var if(x%2==0)]
# print(b)
#
# n=5
# a=[]
# count=1
# for x in range(10):
#     b=n*count
#     a.append(b)
#     count+=1
# print(a)


# li=[]
# for x in range(5,6):
#     for y in range(1,11):
#         a=x*y
#         li.append(a)
# print(li)

# b=[x*y for x in range(5,6) for y in range(1,11)]
# print(b)
#
# a=[10,7,9,12,13,15]
# odd=[]
# even=[]
# for x in a:
#     if(x%2==0):
#         even.append(x)
#     else:
#         odd.append(x)
# print("odd is:",odd)
# print("even is:",even)


# a=[10,7,9,12,13,15]
# b=["even" if(x%2==0) else"odd" for x in a]
# print(b)

# a=[10,7,9,12,13,15]
# b={}
# for x in a:
#     b[x]=x
# print(b)


# a=[10,7,9,12,13,15]
# c={x:x for x in a}
# print(c)

# a=[10,7,9,12,13,15]
# b={}
# for x in a:
#     if(x%2==0):
#         b[x]=x
# print(b)

# a=[10,7,9,12,13,15]
# c={x:x for x in a if(x%2==0)}
# print(c)

# a=["csk","rcb","kkr"]
# b=["dhoni","kholi","dk"]
#
# for x in a:
#     for y in b:
#
#         a[x]=b[y]
# print(a)


# a=["csk","rcb","kkr"]
# b=["dhoni","kholi","dk"]
# c=list(zip(a,b))
# print(c)
# di={}
# for x,y in c:
#     di[x]=y
# print(di)

# a=["csk","rcb","kkr"]
# b=["dhoni","kholi","dk"]
# d={x:y for x,y in zip(a,b)}
# print(d)


# a=[7,8,9,10,11]
# b=set(a)
# print(b)

# a=[7,8,9,10,11]
# c={x for x in a}
# print(c)


# a=[7,8,9,10,11]
# b=set()
# for x in a:
#     if(x%2==0):
#         b.add(x)
# print(b)

# a=[7,8,9,10,11]
# c={x for x in a if(x%2==0)}
# print(c)


#generator comprehension
# a=[7,8,9,10,11,12,14,16]
# b=(x for x in a if(x%2==0))
# for x in b:
#     print(x,end=" ")
