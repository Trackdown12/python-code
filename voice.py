import speech_recognition as speech
import pyttsx3
#print(dir(pyaudio))
#print(dir(speech))
def speak(*args):
    engine=pyttsx3.init()
    engine.setProperty("rate",190)
    engine.say(args)
    print(args)
    engine.runAndWait()
def voice_input():
    voice_data=speech.Recognizer()
    try:
        
        with speech.Microphone() as mic:
            print("listening")
            voice_data.adjust_for_ambient_noise(mic,duration=0.2)
            audio=voice_data.listen(mic)
            text = voice_data.recognize_google(audio)
            print("You said:", text)
            return text
    except speech.UnknownValueError:
        print("could not listen")
        return None
    except speech.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

if __name__ == "__main__":
    recognized_text = voice_input()
    if recognized_text:
        speak(recognized_text)
    else:
        speak("Please try again.")
    while True:
        user_input = voice_input()
    
        if user_input == "exit":
            print("Exiting...")
            break
