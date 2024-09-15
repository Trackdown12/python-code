stk=[]
def empty():
    if stk==[]:
        return True
    else:
        return False
def push(a):
    stk.append(a)
    
def pop():
    if empty():
        print("underflow")
        exit()
    else:
        print(f" popped item is {stk.pop()}")
      
def peek():
    if empty():
        print("underflow")
        exit()
    else:
        a=len(stk)
        print(stk[a-1])
def prstk():
    if empty():
        print("underflow")
        exit()
    else:
        for i in range(len(stk)-1,-1,-1):
            print(stk[i])
while True:
    print("1:push \n  2:pop \n 3:peek \n 4: print \n 5 :exit")
    choice=int(input("enter choice:"))
    if choice==1:
        a=int(input("enter element"))
        push(a)
    elif choice==2:
        pop()
    elif(choice == 3):
        peek()
    elif choice==4:
        prstk()
    elif choice ==5:
        break
    else:
        print("invalid input")