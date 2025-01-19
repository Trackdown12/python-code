import pyttsx3
def speak(*args):
    engine=pyttsx3.init()
    engine.setProperty("rate",175)
    engine.say(args)
    print(args)
    engine.runAndWait()



