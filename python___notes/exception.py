##
##try:
## var=india
## print(var)
##except(NameError):
####      print("good")
###
##try:
## var=10+'a'
## print(var)
##except(NameError):
##      print("good")
##except(TypeError):
##      print("success")


##
##try:
##     var=10/0
##     print(var)
##except(NameError):
##     print("good")
##except(TypeError):
##     print("good")
##except:
##     print("hello")
#
#
# try:
#     var=10/0
#     print(var)
# except(TypeError,NameError):
#     print("success")
# except:
#     print("good")


##
##try:
##     var=10+'a'
##     print(var)
##except(TypeError,NameError):
##     print("success")
##except(ZeroDivisionError):
##     print("good")
##else:
##  print("hello")

#
# try:
#     var=10 +10
#     print(var)
# except(TypeError,NameError):
#     print("success")
# except(ZeroDivisionError):
#     print("good")
# else:
#     print("hello")
# finally:
#     print("done")

##try:
## var=india
## print(var)
##except NameError as a:
##     print(a)

# try:
#     var=india
#     print(var)
# except TypeError as a:
#     print(a)

# handles every error
# try:
#     var=10+'a'
#     print(var)
# except Exception as a:
#     print (a)

#
# try:
#     name=dhoni
#     print(var)
# except Exception as a:
#     print (a)

# try:
#     var=10/0
#     print(var)
# except Exception as a:
#     print (a)

# USER DEFINED EXCEPTION
#
# try:
#     var=10
#     if(var>5):
#         raise TypeError
# except:
#     print("good")
#
# try:
#   var=10
#   if(var>5):
#   raise TypeError
# except TypeError as a:
#     print(a)

# try:
#   var=10
#   if(var>5):
#    raise Exception ("good")
# except Exception as a:
#   print(a)
##
##class Error(Exception):
##    var="ownError"
##try:
##  var=10
##  if(var>5):
##   raise Error
##except Error as a:
##  print(a.var)





























































