import COMMANDS

def demonstration():
    with open('all_commands.txt') as file:
        for line in file:
            val = COMMANDS.commands(line)