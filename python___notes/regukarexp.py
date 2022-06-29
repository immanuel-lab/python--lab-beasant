# import re
# var="india is my country"
# var1=re.match("india",var)
# print(var1.group())

#
# import re
# var="india is my country"
# var1=re.match("INDIA",var)
# print(var1.group())

#
# import re
# var="india is my country"
# var1=re.match("INDIA",var,re.I)
# print(var1.group())

# import re
# var="<html><hand><hand><hand><html>"
# var1=re.match("<.*>",var)
# print(var1.group())


# import re
# var="<html><hand><hand><hand><html>"
# var1=re.match("<.*?>",var)
# print(var1.group())

# import re
# var="india is smarter than china"
# var1=re.match(".* is .*",var)
# print(var1.group())

#
# import re
# var="india is smarter than china"
# var1=re.match("(.*) is (.*)",var)
# print(var1.group(1))
# print(var1.group(2))

# import re
# var="india is smarter than china"
# var1=re.match("(.*) is (.*) (.*)",var)
# print(var1.group(1))
# print(var1.group(2))
# print(var1.group(3))


# import re
# var="india is smarter than china"
# var1=re.match("(.*) is (.*?) (.*)",var)
# print(var1.group(1))
# print(var1.group(2))
# print(var1.group(3))

# import re
# var="&3345@567"
# var1=re.sub("&"," ",var)
# var2=re.sub("@"," ",var1)
# print(var2)

# import re
# var=re.compile("[a-z]")
# var1=var.findall("india")
# print(var1)

# import re
# var=re.compile("[a-z]")
# var1=var.findall("INDIA")
# print(var1)

# import re
# var=re.compile("[a-z]")
# var1=var.findall("INDIA",re.I)
# print(var1)
#
# import re
# var=re.compile("[A-Z]")
# var1=var.findall("INDIA")
# print(var1)

# import re
# var=re.compile("[a-z]+"])
# var1=var.findall("INDIA")
# print(var1)

# import re
# var=re.compile("[a-z]*")
# var1=var.findall("INDIA")
# print(var1)

# import re
# var="india scored 183 runs against srilanka in 39 with 9 extras"
# var1=re.findall("\d{3}",var)
# print(var1)

# import re
# var="india scored 183 runs against srilanka in 39 with 9 extras"
# var1=re.findall("\d{1}",var)
# print(var1)

# import re
# var="india scored 183 runs against srilanka in 39 with 9 extras"
# var1=re.findall("\d{2,3}",var)
# print(var1)

# import re
# var="india scored 183 runs against srilanka in 93 with 9 extras"
# var1=re.findall("\d[]",var)
# print(var1)
#
# import re
# var="india scored 183 runs against srilanka in 93 with 9 extras"
# var1=re.findall("\D{2}",var)
# print(var1)
#
# import re
# var="india scored 183 runs against srilanka in 93 with 9 extras"
# var1=re.findall("\s{2}",var)
# print(var1)

# import re
# var="india scored 183 runs against srilanka in 93 with 9 extras"
# var1=re.findall("\S{2}",var)
# print(var1)

# import re
# var="india scored 183 runs against srilanka in 93 with 9 extras"
# var1=re.findall("\w{2}",var)
# print(var1)



# import re
# var="india scored 183 runs against srilanka in 93 with 9 extras"
# var1=re.findall("\W{2}",var)
# print(var1)


# import re
# var="india scored 183 runs against srilanka in 93 with 9 extras"
# var1=re.findall("\d[0-9]",var)
# print(var1)

# import re
# var="india scored 183 runs against srilanka in 93 with 9 extras"
# var1=re.findall("\d[0-9]+",var)
# print(var1)

# import re
# var="india scored 183 runs against srilanka in 39 with 9 extras"
# var1=re.findall("\d[0-9]*",var)
# print(var1)

# import re
# var="india scored 183 runs against srilanka in 39 with 9 extras"
# var1=re.findall("\D[0-9]",var)
# print(var1)
#
# import re
# var="india scored 183 runs against srilanka in 39 with 9 extras"
# var1=re.findall("\D[0-9]+",var)
# print(var1)

# import re
# var="india scored 183 runs against srilanka in 39 with 9 extras"
# var1=re.findall("\D[0-9]*",var)
# # print(var1)
#
# import re
# var="india scored 183 runs against srilanka in 39 with 9 extras"
# var1=re.findall("\s[a-z]",var)
# print(var1)

# import re
# var="india scored 183 runs against srilanka in 39 with 9 extras"
# var1=re.findall("\s",var)
# print(var1)


# import re
# var="india scored 183 runs against srilanka in 39 with 9 extras"
# var1=re.findall("\W",var)
# print(var1)


# import re
# var="india scored 183 runs against srilanka in 39 with 9 extras"
# var1=re.findall("\d",var)
# print(var1)


# import re
# var="india scored 183 runs against srilanka in 39 with 9 extras"
# var1=re.findall("\D",var)
# print(var1)


# import re
# var="india scored 183 runs against srilanka in 39 with 9 extras"
# var1=re.findall("\s",var)
# # print(var1)
#
#
# import re
# var="india scored 183 runs against srilanka in 39 with 9 extras"
# var1=re.findall("\S",var)
# print(var1)

# import re
# var="india scored 183 runs against srilanka in 39 with 9 extras"
# var1=re.findall("\D",var)
# print(var1)

# import re
# var="india scored 183 runs against srilanka in 39 with 9 extras"
# var1=re.findall("\W",var)
# print(var1)

# \d =number
# \D=alphabet
# \s=empty space
# \S=alphabet+numbers
# \w=alpha+numbers
# \W=empty space

# import re
# var=input("enter your email id:")
# condition="[a-z]+[0-9]+[@]\D{5}[.]\D{2,3}"
# if(re.search(condition ,var)):
#     print("valid")
# else:
#     print("invalid")


# import re
# var=input("enter your email id:")
# condition="[a-z]+[0-9]*[@]\D{5}[.]\D{2,3}"
# #condition='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# if(re.search(condition ,var)):
#     print("valid")
# else:
#     print("invalid")
