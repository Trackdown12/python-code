a=(1)#gives you the integer values
print(type(a))
a=(1,)#creates tuple
print(type(a))
b=(1,6,5,4,8,2,4,6,6,6,47)
print(b.index(6))#prints the first index existence of given argument
print(b.count(6))#prints the occurence of given argument
c=("apple",12)
d=("orange",13)
e=c+d#like strings tuples can be concatenated too
print(e)
print(c*3)#replicate the tuple
print(6 in b)#print true as 6 exist in b (membership operator 'in')
print(len(b))