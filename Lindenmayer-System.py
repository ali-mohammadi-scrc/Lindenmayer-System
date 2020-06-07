import os

def get_console_size():
    try:
        return tuple(os.get_terminal_size())
    except:
        return (80, 25)

clear_console = lambda: os.system('cls' if os.name=='nt' else 'clear')

