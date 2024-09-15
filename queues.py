import pyttsx3    #importing module
#defining a function to speak and print same things almost simutaneously
def speak_text(*args):
    engine=pyttsx3.init()
    engine.setProperty("rate",180)
    engine.say(args)
    print(args)
    engine.runAndWait()    
#defining a function to just speak multiple and single argument
def speak(*args):
    engine=pyttsx3.init()
    engine.setProperty("rate",180)
    engine.say(args)
    engine.runAndWait()
stk=[]#intializing an empty list to perform opperations of queue
front=-1#intializing front element as -1 which shows empty queue which can be changed further while execution
rear=-1#intializing rear element as -1 which shows empty queue which can be changed further while execution
def empty():
   #defing a function theck whether queue is empty or not
    if stk==[]:
        return True
    else:
        return False
def enqueue(a):
    #defining a function to push(enqueue) element in queue
    global front,rear
    stk.append(a)
    if (front==-1 and rear==-1):
        rear+=1
        front+=1
    else:
        rear+=1
def dequeue():
    #defining a function to pop(dequeue) element from the queue
    global front,rear
    if empty():
        speak_text("no elements its underflow")
    a=stk.pop(0)
    if rear==0:
        front-=1
        rear-=1
    else:
        rear-=1
    speak(f"you want to delete an element so i am popping front element {a} in queue")
    return a
def peek():
    #defiining a function to check rear and frotement of queue 
    global front,rear
    if empty():
        speak_text("no elements its underflow")
    speak_text("front=",stk[front])
    speak_text("rear=",stk[rear])
    
def printstk():
    #defining a funtion to print whole queue
    global front,rear
    if empty():
        speak_text("no elements its underflow")
    speak("printing queue")
    for i in stk:
        speak(i)
        print(i,end="  ")
#__main__         
speak("choose 1 for push  2 for pop  3 for peek  4 for print  5 for exit")
while True:
    print("\n 1:enqueue \n 2:dequeue \n 3:peek \n 4: print \n 5 :exit")
    speak("please enter choice")
    choice=int(input("enter choice:"))
    speak("you have chosen",choice)
    if choice==1:
        speak("please enter your desired element")
        a=int(input("enter element"))
        speak(f"pushing {a} in queue")
        enqueue(a)
    elif choice==2:
        print(dequeue())
    elif(choice == 3):
        speak("you want me to show you front and rear elements let me tell you")
        peek()
    elif choice==4:
        printstk()
    elif choice ==5:
        speak("you want to terminate queue so i am terminating queue")
        break
    else:
        speak_text("invalid input")
        