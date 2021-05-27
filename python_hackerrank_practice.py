import pyttsx3
import speech_recognition as sr
import pyautogui as pg
import time
import TYPE_MODE

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def open(text):
    pg.hotkey('win', 's')
    pg.write(text, interval=0.01)
    pg.press("enter")

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

while True:  
        speak("Tell me how can I help you now?")      
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "goodbye" in statement or "ok bye" in statement or "stop" in statement or "bye" in statement:
            speak('Good bye SIR')
            break
        
        elif 'open' in statement:
            statement =statement.replace("open", "")
            open(statement)
            time.sleep(6)
        
        elif 'go to type mode' in statement or "start typing" in statement:
            TYPE_MODE.type()

        elif 'move to home' in statement:
            pg.hotkey('win', 'd')
        
        elif statement != None :
            speak("You said {}".format(statement))