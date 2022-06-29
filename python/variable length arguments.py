## two types of arguments are formal arguments and actual arguments
## actual arguments
## 1.position
## 2.keyword
## 3.default
## 4.variable length arguments(arguments not fixed)


#POSITION ARGUMENTS
##def value("immanuel",25)  
##      print(name)
##      print(age)
##      
##value("immanuel",25)

#KEYWORD ARGUMENTS
##def value(name,age):
##      print(name)
##      print(age)
##  
###value(age=25,name="immanuel")  
##


##DEFAULT ARGU
def value(name,age=18):
      print(name)
      print(age)
  
value(age=25,name="immanuel")  




  #VARIABLE LENGTH ARGUMENTS
##def sum(a,*b):
##    c=a
##    for i in b:
##         c  =c+i
##    print(c)        
##sum(5,6,34,78)

        
    
##def sum(*b):
##    c=0
##    for i in b:
##        c=c+i
##    print(c)
##sum(10,10,10,10,10)     
##



#KEYWORDED VARIABLE LENGTH ARGUMENTS
##def profile(name,**data):
##      print(name)
##      print(data)
##profile("immanuel",age=25,country="india",phno=90034)      


## ALSO THIS WAY
def profile(name,**data):
      print(name)
      for i,j in data.items():
           print(i,j)
profile("immanuel",age=25,country="india",phno=90034)      












        
