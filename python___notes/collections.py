#COLLECTIONS
#named tuple
from collections import namedtuple
a=namedtuple('students',['name','age','No'])
b=a('dhoni',42,7)
print(b)
