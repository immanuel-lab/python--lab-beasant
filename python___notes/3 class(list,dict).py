
#STRING IS IMMUTABLE

##var="india"
####
######var[1]="m"
######print(var)
##print(var.replace("n","m"))
#####print(var)
########
####var="india"
####var.replace("n","m")
####print(var)

#LIST
##var=["dhoni","kohli",7,32]
##print(var)
#print(var[0])
#print(var[1:3])
#print(var[1][1])  # o
##var[1]="yuvi"
##print(var)

##
##var=["dhoni","kohli",7,32]
##var[1][1]="m"
##print(var) #error bcoz string is immutable


##LIST MANIPULATE
##var=["dhoni","kohli",7,32]
##var.append("yuvi")
###print(var)
####var.append("yuvi","jadega")
####print(var)

##var=["dhoni","kohli",7,32]
####var.append(["yuvi","jadega"])
####print(var)
####
##var.extend(["yuvi","jadega"])
##print(var)

##sports=["dhoni","kohli","yuvi"]
##football=["messi","owen","james"]
##sports.extend(football)
##print(sports)


##var=["dhoni","kohli"]
####var.pop()
####print(var)
######
####var.pop(0)
####print(var)
##
##var.remove("kohli")
##print(var)

##var=["dhoni","kohli"]
###var.insert("yuvi")
##var.insert(1,"yuvi")
##print(var)
##
##
##var=["dhoni","kohli","agar"]
##var.sort()
##print(var)

##var=["dhoni","kohli","agar"]
##var.sort(reverse=False)
##print(var)


##var=["dhoni","kohli","agar"]
####print(sorted(var))
##print(sorted(var,reverse=True))

##
##var=["dhoni","kohli","agar"]
##var.clear()
##print(var)
##
##
##var=["dhoni","kohli","agar"]
##del(var)
##print(var)    #var is deleted from memory

##var=[10,7,9]
##var1=[15,17,18]
####var.extend(var1)
####print(var)
##var2=var1+var
##print(var2)


#DICTIONARY
##var={"name":"dhoni","age":40}
##print(type(var))
##print(var)

##var={"name":"dhoni","age":40}
##print(var["name"])
##print(var["name"][1])

##var={"name":"dhoni","age":40}
##var["name"]="kholi"
##print(var)
##
##var={"name":"dhoni","age":40}
##print(var.get("age","no key")) #gives the key age,or else key is not there gives no key


##
##var={"name":"dhoni","age":40}
##var1={"name":"yuvi","age":42}
##var.update(var1)
##print(var)               #update with same key name replaces existing key and value
##
##var={"name":"dhoni","age":40}
##var1={"name 1":"yuvi","age 2":42}
##var.update(var1)       #here update adds to dict
##print(var)
##
##var={"name":"dhoni","age":40}
##
##print(var["name"].count("d"))



####
##var={"name":["dhoni","kohli","yuvi"],"age":[40,32,42]}
##print(var["name"])
####
####var={"name":["dhoni","kohli","yuvi"],"age":[40,32,42]}
####
####var={"name":["dhoni","kohli","yuvi"],"age":[40,32,42]}
####
##
var={"name":["dhoni","kohli","yuvi"],"age":[40,32,42]}
var["name"].append("jadega")
print(var)










































