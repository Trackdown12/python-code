n=int(input("enter number"))
pro=1
for i in range(1,n+1):
    pro*=i
print("factorial using for loop",pro)
a=1
b=1
print(a)
while(a<n+1):
    print(a)
    b*=a
    a+=1
print("factorial using while loop",b)   
for i in range(10,0,-1):
    print(n*i)