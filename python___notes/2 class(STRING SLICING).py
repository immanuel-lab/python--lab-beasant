##var="india"
##print(var[1])
##print(var[4])

##var="India"
##print(var[1:4])#starting -index =0,#ending value=4(index starts from 0 value from 1)


##var="SamSung"
##print(var[3:6])
##print(var[1:4])

###values has negative values from back
##var="SamSung"
##print(var[-5])

##var="SamSung"
##print(var[-6:-4])
##print(var[-6:-3])
##print(var[-3:])
##print(var[-7:])

##
####var="Ganguly"
##print(var[1:4])
##print(var[1:-3])
##print(var[-6:4])
##print(var[-6:-3])
      
##print(var[3:5])
##print(var[3:-1])
##print(var[-4:-1])
##print(var[-4:-1])
##
####
##var="ganguly"
##print(var[::-1])
##print(var[::-3])
##print(var[:-1])

#CANNOT SLICE BACKWARDS
####
##var="india intention india"
##print(var.count("in"))
##print(var.count("in",2))
##print(var.count("in",2,10))
##print(var.find("in"))
##print(var.find("in",2))
##print(var.find("in",8,19))


var="india intention india"
print(var.find("in"))
print(var.find("in",2))
print(var.find("in",8,19))
##print(var.find("irr",2))   -1 since irr is not there


var="india intention india"
print(var.index("in"))
print(var.index("in",2))
print(var.index("in",8,19))


##var="westindies"
##print(var.find("z")) -1
##print(var.index("z")) error


##var="india is my country"
##print(var.split("is"))
##print(var.partition("is"))
##
##print(len(var))

##var="!india is my country!"
##print(var.strip("!"))
##
##print(var.lstrip("!"))
##print(var.rstrip("!"))
##
##print(var.strip("is"))
##print(var.strip("india"))

##
##var="india is my country"
##print(var.upper())
##print(var.lower())
##print(var.capitalize())
##print(var.title())


##var="india is my country"
##print(var.isupper())
##print(var.islower())
##print(var.istitle())


##
##var="India is my country"
##print(var.startswith("India"))
##print(var.endswith("country"))
##print("is" in var)
##                     
##

##RAW STRING
##var="hello \nworld"
####print(var)
##var=R"hello \nworld"
##print(var)




## s = 'Hi\xHello'  UNEXPECTED INDENT
## print(s)
 
##s = r'Hi\xHello'
##print(s)

##
##
##Replace the character H with a J.
##
##
##txt = "Hello World"
##txt = txt.replace("H", "J")
































