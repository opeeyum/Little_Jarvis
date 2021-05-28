import COMMANDS
import TYPE_MODE

def demonstration():
    with open('all_commands.txt') as file:
        val = 0
        for line in file:
            if "go to typing mode" in line or "start typing" in line:
                val = 1
                continue
            elif not val:
                COMMANDS.commands(line)
            elif val:
                val = TYPE_MODE.type_commands(line)
            
            
    return