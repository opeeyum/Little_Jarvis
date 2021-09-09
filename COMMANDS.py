import voice_assistant as va
import Demon

def commands(statement)->int:
    try:
        if "goodbye" in statement or "ok bye" in statement or "stop" in statement or "bye" in statement:
            va.speak('Good bye SIR')
            return 0

        elif "speak" in statement:
            statement = statement.replace("speak", "")
            va.speak(statement)

        elif 'time' in statement:
            strTime = va.datetime.datetime.now().strftime("%H:%M:%S")
            va.speak(f"current time is {strTime}")
        
        elif 'date' in statement:
            strTime = va.datetime.date.today()
            #print(strTime)
            va.speak(f"Todays date is {strTime}")
        
        elif 'open' in statement:
            if 'jarvis' in statement:
                statement = statement.replace("jarvis", "")
            statement =statement.replace("open", "")
            va.OPEN(statement)
            va.time.sleep(5)

        elif 'search for' in statement or 'search' in statement:
            statement = statement.replace("search for", "")
            if 'jarvis' in statement:
                statement = statement.replace("jarvis", "")
            va.webbrowser.get('windows-default')
            va.webbrowser.open_new(statement)
        
        elif 'joke' in statement:
            va.speak(va.pyjokes.get_joke())

        elif 'move to home' in statement:
            va.pg.hotkey('win', 'd')

        elif 'switch tab' in statement or 'switch' in statement or 'next' in statement:
            va.pg.keyDown('alt')
            va.pg.press('tab', presses=2)
            va.pg.keyUp('alt')

        elif 'close' in statement:
            va.pg.hotkey('alt', 'f4')

        elif 'stand by' in statement or "wait" in statement:
            va.standby()
        
        elif 'demonstration mode' in statement or 'tell me about yourself' in statement:
            va.speak("Switching to Demonstration mode.")
            Demon.demonstration()
            va.speak("Demonstration Completed.")       
        
        elif 'press enter' in statement or 'enter' in statement:
            va.pg.press('enter')

        elif 'press tab' in statement or 'tab' in statement:
            va.pg.press('tab')
        
        elif 'delay' in statement:
            va.time.sleep(2) 
        
        elif statement.strip():
            va.speak("You said {}".format(statement))

    except:
        pass
    
    return 1
