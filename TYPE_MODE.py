import voice_assitant as va

def insert(sym):
    symbols = {
        'comma' : ',',
        'full stop': '.',
        'single quotation': "'",
        'double quotation': '"',
        'semicolon': ';',
        'colon': ':',
        'left curly bracket': '{',
        'right curly bracket': '}',
        'left bracket': '(',
        'right bracket': ')',
        'left square bracket': '[',
        'right square bracket': ']',
        'question mark': '?',
        "plus": "+",
        "minus": '-',
    }
    try:
        va.pg.write(symbols.get(sym))
    except:
        pass

def type():
    va.speak("Ready to type sir.")     
    while True:            
        statement = va.takeCommand().lower()

        if statement==0:
            continue

        elif 'type' in statement:
            statement = statement.replace("type", "")
            va.pg.write(statement)

        elif 'delete that' in statement or 'delete' in statement:
                va.pg.press('backspace')            
            
        elif 'close' in statement:           
            va.pg.hotkey('alt', 'f4')

        elif 'stop typing' in statement:
            va.speak('Leaving typing mode')          
            return
        
        elif 'press enter' in statement or 'enter' in statement:
            va.pg.press('enter')

        elif 'press tab' in statement or 'tab' in statement:
            va.pg.press('tab')
        
        elif 'insert' in statement:
            statement = statement.replace('insert', "")
            insert(statement.strip())

        elif 'move left' in statement:
            va.pg.press('left')
        
        elif 'move right' in statement:
           va.pg.press('right')


            