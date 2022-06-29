Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> imman=[1,2,3,4,5]
>>> imman.append (32)
>>> imman
[1, 2, 3, 4, 5, 32]
>>> imman.insert (1,99)
>>> imman
[1, 99, 2, 3, 4, 5, 32]
>>> imman.clear(imman)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    imman.clear(imman)
TypeError: clear() takes no arguments (1 given)
>>> imman.remove(99)
>>> imman
[1, 2, 3, 4, 5, 32]
>>> imman.pop(0)
1
>>> imman
[2, 3, 4, 5, 32]
>>>   imman.pop()
SyntaxError: unexpected indent
>>> imman.pop()
32
>>> imman
[2, 3, 4, 5]
>>> del imman(2:)
SyntaxError: invalid syntax
>>> del imman(2:)
SyntaxError: invalid syntax
>>> ggg=[12,13,14,15,16,17,18]
>>> ggg
[12, 13, 14, 15, 16, 17, 18]
>>> del ggg[3:]
>>> ggg
[12, 13, 14]
>>> del imman[2:]
>>> imman
[2, 3]
>>> imman.append (23,24,25)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    imman.append (23,24,25)
TypeError: append() takes exactly one argument (3 given)
>>> imman.append(32)
>>> imman
[2, 3, 32]
>>> imman.insert(0,1)
>>> imman
[1, 2, 3, 32]
>>> imman.pop(0)
1
>>> imman
[2, 3, 32]
>>> imman.remove(0)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    imman.remove(0)
ValueError: list.remove(x): x not in list
>>> imman.remove(2)
>>> imman
[3, 32]
>>> del.ggg[1:]
SyntaxError: invalid syntax
>>> del ggg[1:]
>>> ggg
[12]
>>> ggg extend([13,14,15,16,17]
	       
SyntaxError: invalid syntax
>>> ggg.extend ([13,14,15,16,17])
	       
>>> ggg
	       
[12, 13, 14, 15, 16, 17]
>>> jjjj=print("imman \nmakes")
	       
imman 
makes
>>> jj=print(r"imman \number")
	       
imman \number
>>> min(ggg)
	       
12
>>> min(oo)
	       
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    min(oo)
NameError: name 'oo' is not defined
>>> max(ggg)
	       
17
>>> sum(ggg)
	       
87
>>> gog=[4,3,2,1]
	       
>>> gog.sort()
	       
>>> gog
	       
[1, 2, 3, 4]
>>> gog.clear()
	       
>>> gog
	       
[]
>>> gog.append
