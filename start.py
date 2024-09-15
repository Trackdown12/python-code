import pyttsx3
from datetime import *
#print(dir(datetime))
engine = pyttsx3.init()
def speak(*args):
    for arg in args:
        if isinstance(arg, str):
            engine.say(arg)
        elif isinstance(arg, (int, float)):
            engine.say(str(arg))
        else:
            raise TypeError(f"Unsupported type: {type(arg)}")
    
    engine.runAndWait()

a=datetime.now().strftime("%I:%M %p") 
speak("program begins")
speak("its",a,"sir")

print(a)
x=1
for i in range(1,6):
    for j in range(1,i):
        speak(x)
        print(x,end=" ")
        x=x+1
    print()    
speak("program ends sir ")