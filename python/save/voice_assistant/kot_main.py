import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', voices[1].id)  # 0 - male, 1 - female


def send_email(to, content):
    """
    Send emails to one or more than one recipient.
    An instance method called sendmail is present in the SMTP module.
    This instance method allows us to send an email.
    It takes 3 parameters:
    The sender: Email address of the sender.
    The receiver: Email of the receiver.
    The message: A string message which needs to be sent to one or more than one recipient.
    :param to:
    :param content:
    :return:
    """
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('justbitwallet@gmail.com', '**********')
    server.sendmail('justbitwallet@gmail.com', to, content)
    server.close()


def take_command():
    """
    It takes microphone input from the user and returns string output
    :return:
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition
        print(f'User said: {query}\n')
    except Exception as err:
        print(err)
        print('Say that again please...')
        return "None"
    return query


def wish_me():
    """
    Variable "hour" means current time in your area.
    If the time is between 00:00 and 12:00, Kot says "Good Morning!".
    If the time is between 12:00 and 18:00, it's "Good Afternoon!".
    Else, it means between 18:00 and 00:00, it is "Good Evening!"
    """
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak('Good Morning!')
    elif 12 <= hour <= 18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')


def speak(audio):
    """
    This function will take audio as an argument, and then it will pronounce it.
    :param audio: text to be spoken
    """
    engine.say(audio)
    engine.runAndWait()  # Without this command speech will not be audible to us


if __name__ == "__main__":
    # speak("Hello I am Kot")
    # wish_me()
    listening = True
    while listening:
        # if 1:
        query = take_command().lower()  # Converting user query into lower

        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'D:\my_playlist'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {str_time}")

        elif 'open code' in query:
            # code_path = "C:\Users\chenuli\AppData\Local\Programs\Microsoft VS Code\levelmenu.exe"
            # os.startfile(code_path)
            pass

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = take_command()
                to = "liorschirov@gmail.com"
                send_email(to, content)
                speak("Email has been sent!")
            except Exception as err:
                print(err)
                speak("Sorry my friend. I am not able to send this email")  # If @ and password is incorrect

        elif 'thank you' in query:
            speak('You are welcome')

        elif 'bye' in query:
            speak('Bye Bye')
            listening = False
