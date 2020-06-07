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

def print_screen():
    screen.reverse()
    nice_screen = '\n'.join([''.join([chr(9617 + 2 * c) for c in line]) for line in screen])
    screen.reverse()
    print(nice_screen)

def draw_line(start, ang, length):
    import math
    ang = math.radians(ang)
    cos_a = math.cos(ang)
    sin_a = math.sin(ang)
    L_X = round(2 * cos_a * length)
    L_Y = round(sin_a * length)
    if abs(L_X) >= abs(L_Y):
        X = 1
        N = L_X
    else:
        X = 0
        N = L_Y
    Sign = 1
    if N < 0:
        Sign = -1
        N *= -1
    x = start[0]
    y = start[1]
    for i in range(N):
        x = start[0]
        y = start[1]
        if X:
            x += i * Sign
            y += round(i/2 * sin_a / cos_a) * Sign
        else:
            y += i * Sign
            x += round(2 * i * cos_a / sin_a) * Sign
        y %= len(screen)
        x %= len(screen[y])
        screen[y][x] = 1
    return (x, y)

def L_System_update(current_pattern):
    if current_pattern == '':
        return axiom
    new_pattern = []
    for a in current_pattern:
        new_pattern += [rules.get(a, a)]
    return ''.join(new_pattern)

def depict(point, alpha):
    import time
    stack = []
    for a in pattern:
        if a == '-':
            alpha -= angle
        elif a == '+':
            alpha += angle
        elif a == '[':
            stack = stack + [(point, alpha)]
        elif a == ']':
            point = stack[-1][0]
            alpha = stack[-1][1]
            stack = stack[:-1]
        else:
            point = draw_line(point, alpha, 3)
    clear_console()
    print_screen()
    time.sleep(0.7)

console_size = get_console_size()
screen = empty_screen()

variable = []
constants = []
rules = {}
axiom = ''
angle = 0
N_Step = 0

N_Pattern = int(input('Enter pattern#: (0-3) '))

if N_Pattern == 0:
    variables = ['F', 'X']
    constants = ['-', '+', '[', ']']
    rules = {
        'F': 'FF',
        'X': 'F-[[X]+X]+F[+FX]-X'
    }
    axiom = 'X'
    angle = 25
    N_Step = 5
    point_0 = (0, 0)
    alpha_0 = 160
elif N_Pattern == 1:
    variables = ['F', 'B']
    constants = ['-', '+', '[', ']']
    rules = {
        'F': 'FF',
        'B': 'F[-B]+B'
    }
    axiom = 'B'
    angle = 30
    N_Step = 5
    point_0 = (int(console_size[0] / 2), 0)
    alpha_0 = 90
elif N_Pattern == 2:
    variables = ['A', 'B']
    constants = ['-', '+']
    rules = {
        'A': 'B-A-B',
        'B': 'A+B+A'
    }
    axiom = 'A'
    angle = 60
    N_Step = 5
    point_0 = (0, 0)
    alpha_0 = 0
elif N_Pattern == 3:
    variables = ['T', 'R', 'L', 'F']
    constants = ['-', '+', '[', ']']
    rules = {
        'T': 'R+[T]--[--L]R[++L]-[T]++T',
        'R': 'F[--L][++L]F',
        'L': '[-F+L+F-]',
        'F': 'FF'
    }
    axiom = 'T'
    angle = 30
    N_Step = 5
    point_0 = (int(console_size[1] / 2), 0)
    alpha_0 = 50

pattern = ''
for t in range(N_Step):
    pattern = L_System_update(pattern)
    screen = empty_screen()
    depict(point_0, alpha_0)