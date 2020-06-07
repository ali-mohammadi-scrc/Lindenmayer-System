import os

def get_console_size():
    try:
        return tuple(os.get_terminal_size())
    except:
        return (80, 25)

clear_console = lambda: os.system('cls' if os.name=='nt' else 'clear')

def empty_screen():
    console_size = get_console_size()
    return [[0 for c in range(console_size[0] - 2)] for l in range(console_size[1] - 2)]

def draw_line(start, angle, length):
    import math
    angle = math.radians(angle)
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    X = 1
    N = round(2 * cos_a * length)
    if round(sin_a * length) > N:
        X = 0
        N = round(sin_a * length)
    for i in range(N):
        x = start[0]
        y = start[1]
        if X:
            x += i
            y += round(i/2 * sin_a / cos_a)
        else:
            y += i
            x += round(2 * i * cos_a / sin_a)
        screen[y][x] = 1

def print_screen():
    screen.reverse()
    nice_screen = '\n'.join([''.join([chr(9617 + 2 * c) for c in line]) for line in screen])
    screen.reverse()
    print(nice_screen)

def L_System_update(current_pattern):
    if current_pattern == '':
        return axiom
    new_pattern = [a if a in constants else '' for a in current_pattern]
    old_state = rules.keys()
    for state in old_state:
        new_state = rules[state]
        C = 1
        if state[0] == '*' and state[2] == '*':
            state = state[1]
            C = 0
        elif state[0] == '*':
            state = state[1:2]
            C = 0
        elif state[2] == '*':
            state = state[0:1]
        ind = 0
        while ind < len(current_pattern):
            ind = pattern.find(state, ind)
            if ind < 0:
                break
            new_pattern[ind+C] = new_state
            ind += 1
    return ''.join(new_pattern)

screen = empty_screen()
