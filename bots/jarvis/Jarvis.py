import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import socket
import sys
from secrets import email, passcode

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# for voice in voices:
    # print(voice.id)
engine.setProperty('voice', voices[1].id)
# sys.exit()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am JARVIS, What can I do for you?")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print("Recognizing...")   
        socket.getaddrinfo('localhost', 8080) 
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email, passcode)
    server.sendmail(email, to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        print(query)

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            if(query):
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open my songs' in query:
            webbrowser.open("https://www.youtube.com/watch?v=Pkh8UtuejGw&list=PLfcEmnRuxxwCwvsBZotVrLVPR9ogFRLqT&index=1")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif ('play music' in query or 'open music' in query):
            music_dir = 'C:\\songs'
            songs = os.listdir(music_dir)
            # print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif ('stop music' in query or 'pause music' in query):
            # stop the running music
            os.system("TASKKILL /F /IM Video.UI.exe")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = email   
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email") 