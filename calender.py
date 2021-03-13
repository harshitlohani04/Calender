import datetime
import speech_recognition as sr

x = datetime.datetime.now()

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak: ")
    audio = r.listen(source)


my_audio = r.recognize_google(audio)
try:
    if "day" in my_audio:
        print("Today is",x.strftime("%A"))
        
    elif "time" in my_audio:
        print("The time is :",x.strftime("%X"),x.strftime("%p"))
    elif "month" in my_audio:
        print("The ongoing month is:", x.strftime("%B"))
    elif "year" in my_audio:
        print("The current year is:",x.strftime("%Y"))
 
except sr.UnknownValueError:
    print("sorry")