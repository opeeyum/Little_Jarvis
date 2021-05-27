import pyttsx3
import datetime
import speech_recognition as sr
import pyautogui as pg
import time
import webbrowser
import pyjokes
import TYPE_MODE
import COMMANDS

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()

def OPEN(text):
    if text.strip():
        pg.hotkey('win', 's')
        pg.write(text, interval=0.01)
        pg.press("enter")

def wishMe():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello Sir,Good Morning")
        print("Hello Sir,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello Sir,Good Afternoon")
        print("Hello Sir,Good Afternoon")
    else:
        speak("Hello Sir,Good Evening")
        print("Hello Sir,Good Evening")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Sorry, can you please say that again")
            return "None"
        return statement

def standby():
    speak("Starting Standby mode Sir.")     
    while True:            
        statement = takeCommand().lower()
        if statement==0:
            continue

        elif 'wake up' in statement or 'back to work' in statement:
            return

if __name__=='__main__':
    speak("Little Jarvis at your service sir. ")
    wishMe()
    val = 1
    while val:  
        speak("Tell me how can I help you now?   ")      
        statement = takeCommand().lower()
        if statement==0:
            continue
        else: 
            val = COMMANDS.commands(statement)