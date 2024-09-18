a=5
for i in range(0,a):
    print(" "*(a-i-1),end="")
    for j in range(0,i+1):
        print(i-j+1,end="")
    print()
    a=5