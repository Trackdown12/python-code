'''a=[1,2,3,6,4,5,8.02,79,]
print(a)
a.append(56)
print("append  list",a)
a.sort()
print("sorted list",a)
a.reverse()
print("reversed list",a)
a.insert(5,55)#insert 55 at index 5
print("inserted list",a) 
a.pop()
print(a)
print("value of pop",a.pop(4))
print("poped list",a)'''
#print data of list
l=[10,12,2,102,33]
print(l[0:3])
print("sum:",sum(l))
i=0
while(i<len(l)):
    print(f"the list using while {l[i]}")
    i+=1
for i in l:
    print(f"the list using for {i}")