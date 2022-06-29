# class old:
#     def __init__(self,name,age):
#         self.a=name
#         self.b=age
#     def fun1(self):
#         print(self.a,self.b)
# class new(old):
#     def __init__(self,name,age):
#         self.a1=name
#         self.b1=age
#
#     def fun2(self):
#         print(self.a1,self.b1)
#
# b=new("dhoni",42)
# # b.fun1()
# b.fun2()

#
# class old:
#     def __init__(self,name,age):
#         self.a=name
#         self.b=age
#     def fun1(self):
#         print(self.a,self.b)
# class new(old):
#     def __init__(self,name,age,num):
#         old.__init__(self,name,age)
#         self.a1=name
#         self.b1=age
#
#
#
#     def fun2(self):
#         print(self.a1,self.b1)
#
# b=new("dhoni",42)
# b.fun1()
# b.fun2()

#polmorphismPOLYMORPHISM

# class Tomato:
#     def colour(self):
#         print("red")
#     def type(self):
#         print("vegetable")
# class Apple:
#     def colour(self):
#         print("red")
#     def type(self):
#         print("fruits")
#
# def fun(obj):
#     obj.colour()
#     obj.type()
# fun(Tomato())
# fun(Apple())

# class New:
#     def __init__(self,salary,year):
#         self.a=salary
#         self.b=year
#     @classmethod
#     def fun(cls,salary,instalment,year):
#         return cls(salary-instalment,year)
#     @staticmethod
#     def fun1(salary):
#         if(salary>500):
#             print("valid")
#     def fun2(self):
#         print(self.a,self.b)
# c=New(15000,192)
# c.fun2()
# c.fun1(7000)
# d=New.fun(25000,5000,1992)
# d.fun2()
