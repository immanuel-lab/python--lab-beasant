##from collections import namedtuple
##a=namedtuple('students',['name','age','No'])
##b=a('dhoni',42,7)
##print(b)
##print(b[1])
##print(b.No)
##print(getattr(b,'name'))
##li=["yuvi",45,14]
##print(a._make(li))
##di={"name":"kohli","age":33,"No":3}
##print(a(**di))
##print(b._asdict())
##print(b._fields)
##print(b._replace(name="beasent"))
##
##print(list(b))
##
##from collections import deque
##a=deque([10,11,12,13,14])
##print(a)
##a=deque((10,11,12,13,14))
##print(a)
##a.append(15)
##a.appendleft(9)
##print(a)
##a.extend([16,17])
##print(a)
##a.extendleft([7,8])
##print(a)
##a.pop()
##print(a)
##a.popleft()
##print(a)
##print(a[1])
##
##from collections import ChainMap
##a ={1:"a",5:'e',b:'f'}
##b={4:'d',5:'e',b:'f'}
##c=ChainMap(a,b)
##print(c)
##print(list(c.keys()))
##print(list(c.values()))
##
##from collections import Counter
##a=[1,2,3,4,1,2,3]
##b=Counter(a)
##print(b)
##var="india is my country"
##c=Counter(var)
##print(c)
      
##from collections import OrderedDict
##a={}
##a[0]="a"
##a[1]="b"
##a[2]="c"
##for key,values in a.items():
##    print(key,values)
##a[1]='z'
##for key,values in a.items():
##    print(key,values)
##a.pop(1)
##for key,values in a.items():
##    print(key,values)
##a[1]="k"
##for key,values in a.items():
##    print(key,values)

##from collections import OrderedDict
##a={}
##a[0]="a"
##a[1]="b"
##a[2]="c"
##for key,values in a.items():
##    print(key,values)
##a[1]='z'
##for key,values in a.items():
##    print(key,values)
##a.pop(1)
##for key,values in a.items():
##    print(key,values)
##a[1]="k"
##for key,values in a.items():
##    print(key,values)

##
##from collections import OrderedDict
##a=OrderedDict()
##a[0]="a"
##a[1]="b"
##a[2]="c"
##for key,values in a.items():
##    print(key,values)
##a[1]='z'
##for key,values in a.items():
##    print(key,values)
##a.pop(1)
##for key,values in a.items():
##    print(key,values)
##a[1]="k"
##for key,values in a.items():
##    print(key,values)
##print(a[3])   #no error

##
##from collections import defaultdict
##def fun():
##    return "no key"
##a=defaultdict(fun)
##a[0]='a'
##a[1]='b'
##a[2]='c'
##
##for key,values in a.items():
##    print(key,values)
##print(a[3])



























































    

    



































