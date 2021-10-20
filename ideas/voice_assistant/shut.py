import pyttsx3
import speech_recognition as sr
import os


def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio)
            print("the query is printed='", query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
    import time
    time.sleep(2)
    return query


def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


speak("Do you want to shutdown your computer sir?")
while True:
    command = take_commands()
    if "no" in command:
        speak("Thank u sir I will not shut down the computer")
        break
    if "yes" in command:
        # Shutting down
        speak("Shutting the computer")
        os.system("shutdown /s /t 30")
        break
    speak("Say that again sir")
