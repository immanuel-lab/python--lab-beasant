
# a,c='18'
# b,a='34'
# print(a+b+c)

#1.REVERSE A STRING

# str='imman'
# str1=str[::-1]
# print(str1)

# str='imman'
# str1=list(reversed(str))
# str1=''.join(str1)
# print(str1)

# str='imman'
# str1=''
# for i in range(len(str)-1,-1,-1):
# 	str1=str1+str[i]
# print(str1)

# str='imman'
# str1=''
# i=len(str)-1
# while i>=0:
# 	str1=str1+str[i]
# 	i=i-1
# print(str1)

#2.REVERSE ORDER OF WORDS
#INPUT=learning python is very easy
#output=easy very is python learning
 
# input='learning python is very easy'
# output=''
# str1=input.split()
# str1=list(reversed(str1))
# output=' '.join(str1)
# print(output)

# input='learning python is very easy'
# output=''
# str1=input.split()
# str1=str1[::-1]
# output=' '.join(str1)
# print(output)

#3.input='durga software solutions'
#output='agrud erawtfos snoitulos'

# input='durga software solutions'
# output=''
# str1=input.split()
# i=0
# while i<len(str1):
# 	output=output+str1[i][::-1]+' '
# 	i+=1
# print(output)

#input='durga software solutions'

# l=input.split()
# l1=[]
# for words in l:
# 	l1.append(words[::-1])
# str1=' '.join(l1)
# print(str1)

#4.input='one two three four five six'
#output='one owt three ruof five xis'
# input='one two three four five six'
# l=input.split()
# l1=[]
# i=0
# while(i<len(l)):
# 	if i%2!=0:
# 		l1.append(l[i][::-1])
# 	else:
# 		l1.append(l[i])
# 	i+=1
# output=' '.join(l1)
# print(output)

#5.print charecters at even and odd index seperately

# input="durgasoft"
# l1=[]
# l2=[]
# for i in range(len(input)):
# 	if i%2==0:
# 		l2.append(input[i])
# 	else:
# 		l1.append(input[i])

# print('words at odd index:',l1)

# print('words at even index:',l2)

# print('words at odd index:')
# for i in range(len(l1)):
# 	print(l1[i],end=' ')
# 	print()
# print('words at even index:')
# for i in range(len(l2)):
# 	print(l2[i],end=' ')


# input="durgasoft"
# str2=input[::2]
# str1=input[1::2]
# print('charecters at odd index',str1)
# print('charecters at even index',str2)



#6 sort alphabets followed by digits
# input=b4a1d3
# output=abd134

# input='b4a1d3'
# l1,l2=[],[]
# for i in input:
# 	if i.isalpha():
# 		l1.append(i)
# 	else:
# 		l2.append(i)
# output=''.join(sorted(l1))+''.join(sorted(l2))
# print(output)

#7.input=a4b3c2
#output=aaaabbbcc
# input='a4b3c2'
# output=''
# for i in input:
# 	if i.isalpha():
# 		x=i
# 	else:
# 		d=int(i)
# 		output=output+x*d
# print(output)

# input='a3z2b4'
# output='aaazzbbbb'
# input='a3z2b4'
# output=''
# for i in input:
# 	if i.isalpha():
# 		x=i
# 	else:
# 		output=output+x*int(i)
# output=sorted(output)
# output=''.join(output)
# print(output)

# input='aaaabbbccz'
# output='4a3b2c1z'

# input='aaaabbbccz'
# output=''
# prev=input[0]
# count=1
# i=1

# while i<len(input):
# 	if input[i]==prev:
# 		count+=1
# 	else:
# 		output=output+str(count)+prev
# 		prev=input[i]
# 		count=1
# 	if i==len(input)-1:
# 		output=output+str(count)+prev

	
# 	i+=1
# print(output)


#input='a4k3b2'
#output='aeknbd'

# input='a4k3b2'
# output=''
# for i in input:
# 	if i.isalpha():
# 		output=output+i
# 		prev=i
# 	else:
# 		output=output+chr(ord(prev)+int(i))
# print(output)


#count the number of elements with duplicates

# str='aaazzbbbb'
# d={}
# for i in str:
# 	d[i]=d.get(i,0)+1
# for k,v in d.items():
# 	print(f'{k} occurs {v} times')


# str='aaazzbbbb'
# l=[]
# for i in str:
# 	if i not in l:
# 		l.append(i)
# for item in l:
# 	print(f'{item} occurs {str.count(item)} times')

#number of occurences of each vowel in string

# input="durgasoftsolutions"
# l=[]
# l1=[]
# vowels=['a','e','i','o','u']
# for i in input:
# 	if i not in l:
# 		l.append(i)
# for i in l:
# 	if i in vowels:
# 		l1.append(i)
# for i in sorted(l1):
# 	print(f'{i} occurs {input.count(i)} times')

# input="durgasoftsolutions"
# d={}
# vowels=['a','e','i','o','u']
# for i in  input:
# 	if i in vowels:
# 		d[i]=d.get(i,0)+1
# print(d)


#program to check whether two strings are anagrams

# def isanagram(str1,str2):
# 	str1=sorted(str1)
# 	str2=sorted(str2)
# 	if str1==str2:
# 		return 'string are anagrams'
# 	else:
# 		return 'strings are not anagrams'
	

# s1,s2='fried','fired'
# print(isanagram(s1,s2))


# s1='abcde'
# s2='12345'
# i=j=0
# while i<len(s1) or j<len(s2):
# 	output=s1[i]+s2[j]
# 	print(output+",",end='')
# 	i+=1
# 	j+=1

# s1='abcdefg'
# s2='xyz'
# s3='12345'
# i=j=k=0
# while i<len(s1) or j<len(s2) or k<len(s3):
# 	output=''
# 	if i<len(s1):
# 		output=output+s1[i]
# 		i+=1
# 	if j<len(s2):
# 		output=output+s2[j]
# 		j+=1
# 	if k<len(s3):
# 		output=output+s3[k]
# 		k+=1
# 	print(output)



	
