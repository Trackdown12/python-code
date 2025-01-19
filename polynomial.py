import platform
x=int(input("enter value of x"))
dict1={1:2,6:1,2:6}
sum1=0
for i in dict1:
    sum1=sum1+(i*x**dict1[i])
print(sum1)