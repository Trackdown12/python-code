s={}#empty dict
print(type(s))
a=set()#empty set
print(s,type(s),"\n",a,type(a))
a={1,2,3,48,45,451,"hello_imposter ",14}#gives output in unorderd manner
print(a)
c={12,1,4,151,54114,851}
print(c)
b=sorted(c)#this method can be used to sort a set returns set in a list
print(b)
c.add(144)
print(c)
print(len(c))
c.remove(12)#removes 12 from set
print("removing 12",c)
c.pop()#removes random element from set 
print("removing random element",c)