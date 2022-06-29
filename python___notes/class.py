# =oops
# it is a blue print for creating objects

# class New:
#     var=10
# print(New.var)

# class New:
#     def fun(a,b):
#         print(a+b)
# New.fun(10,30)

# class New:
#     def fun(a):
#         print(a)
# New.fun("dhoni")
# count=10
# class New:
#     count=20
#     def fun(a,b):
#         print(a+b)
# New.fun(100,200)
# print(count)
# print(New.count)

# count=10
# class New:
#     global count
#     count=20
#     def fun(a,b):
#         print(a+b)
# New.fun(100,200)
# print(count)
# print(New.count)

# class New:
#     def fun():
#         print("success")
#     def fun():
#         print("good")
# New.fun()

# class New:
#     def fun(a,b):
#         print(a+b)
#     def fun():
#         print("good")
# New.fun(10,20)
# class New:
#     def fun(a,b):
#         print(a+b)
#     def __fun():
#         print("good")
# New.fun(10,20)


# class New:
#     def fun(a,b):
#         print(a+b)
#     def fun1():
#         print("success")
# New.fun(100,200)
# New.fun1()

# class New:
#     "my function"
#     def fun(a,b):
#         print(a+b)
#     def fun1():
#         print("success")
# New.fun(100,200)
# print(New.__doc__)

# class New:
#     def mul(a,b):
#         "multiplication"
#
#         print(a*b)
#     def sub(a,b):
#
#         print(a-b)
# New.mul(10,20)
# New.sub(10,20)


#INHERITANCE

# class ms:
#     def fun(a,b):
#         print(a+b)
# class dhoni(ms):
#     def fun1():
#         print("success")
# dhoni.fun1()
# dhoni.fun(10,20)

# class A:
#     def fun():
#         print("a")
# class B(A):
#     def fun():
#         print("b")
# class C(B,A):
#     def fun():
#         print("c")
# class D(C,B):
#     def fun():
#         print("d")
# D.fun()



#
# class A:
#     def fun():
#         print("a")
# class B(A):
#     def fun():
#         print("b")
# class C(B,A):
#     def fun():
#         print("c")
# class D(C,B):
#     pass
# D.fun()

# class New:
#     def fun(ip,pwd):
#         print(ip,pwd)
#     def fun1(ip,pwd,code):
#         print(ip,pwd,code)
# New.fun("127.0.0.1","@123")
# New.fun1("127.0.0.1","@123","ipconfig")
#
# class New:
#     def __init__(self,ip,pwd):
#         self.a=ip
#         self.b=pwd
#     def fun(self):
#         print(self.a,self.b)
#     def fun1(self):
#         print(self.a,self.b)
# a=New("127.0.0.1","@123")
# a.fun()
# a.fun1()

# class New:
#     def __init__(self,ip,pwd,code):
#         self.a=ip
#         self.b=pwd
#         self.c=code
#     def fun(self):
#         print(self.a,self.b)
#     def fun1(self):
#         print(self.a,self.b,self.c)
# a=New("127.0.0.1","@123","ipconfid")
# a.fun()
# a.fun1()
#
# class New:
#     def __init__(self,ip,pwd,code):
#         self.a=ip
#         self.b=pwd
#         self.c=code
#     def fun(self):
#         print(self.a,self.b)
#     def fun1(self):
#         print(self.a,self.b,self.c)
# a=New("127.0.0.1","@123","ipconfid")
# a.fun()
# a.fun1()
#
# class New:
#     def __init__(self,ip,pwd):
#         self.a=ip
#         self.b=pwd
# 
#     def fun(self):
#         print(self.a,self.b)
#     def fun1(self,code):
#         print(self.a,self.b,code)
# a=New("127.0.0.1","@123")
# a.fun()
# a.fun1("ipconfig")
