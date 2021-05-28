import pyttsx3
import datetime
import speech_recognition as sr
import pyautogui as pg
import time
import webbrowser
import pyjokes
import TYPE_MODE
import COMMANDS

engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):    
    engine.say(text)
    engine.runAndWait()

def OPEN(text):
    if text.strip():
        pg.hotkey('win', 's')
        time.sleep(1)
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

def takeCommand(st:int=1):
    r = sr.Recognizer()
    with sr.Microphone() as source:        
        r.adjust_for_ambient_noise(source, duration=2)
        if st:speak("Listening...")
        else:print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            if st: speak("Sorry, can you please say that again")
            return ""
        return statement

def standby():
    speak("Starting Standby mode Sir.")     
    while True:            
        statement = takeCommand(0).lower()
        if statement==0:
            continue
        elif 'wake up' in statement or 'back to work' in statement:
            wishMe()
            return

if __name__=='__main__':
    speak("Little Jarvis at your service sir. ")
    wishMe()
    speak("How can I help you now.")
    val = 1; flag = 0
    while val:    
        statement = takeCommand().lower()
        if statement==0:
            continue            
        elif "go to typing mode" in statement or "start typing" in statement:
            flag = 1
            speak("Ready to type sir, make sure cursor is in place.")
            COMMANDS.commands("delay")
            continue 
        elif not flag: 
            val = COMMANDS.commands(statement)            
        elif flag:
            flag = TYPE_MODE.type_commands(statement)