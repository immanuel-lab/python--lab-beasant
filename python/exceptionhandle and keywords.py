##The try block lets you test a block of code for errors.
##
##The except block lets you handle the error.
##
##The finally block lets you execute code, regardless of the result of the
##
##You can use the else keyword to define a block of code to be executed
##if no errors were raised:
##
##
##try:
##    x=1
##    y=0
##    z=x/y
##    print(z)
##except:
##    print("cannot divide by zero")
##else:
##    print("successfully divided")
##finally:
##    print("completed")
##    
##try:
##  print(x)
##except NameError:
##  print("Variable x is not defined")
##except:
##  print("Something else went wrong")

##
##x = "hello"
##
##if not type(x) is int:
##  raise TypeError("Only integers are allowed")
##

##x = 10
## 
##if not x > 10:
## 
##    print("not retured True")
## 
##else:
## 
##    print("not retured False")

##x = ["apple", "banana", "cherry"]
##
##y = ["apple", "banana", "cherry"]
##
##print(x is y) #false since it is different object

##x=5
##y=x
##print(x is y)  #trus since x and y have same object

##
##
##x=5
##x=float(x)
##print(x)


##x=5
##y=complex(x)
##print(y)

##txt = "     banana     "
##
##x = txt.strip()
##
##print("of all fruits", x, "is my favorite")
##

x="      i love orange"
x=x.strip()
print(x)





















    








