"""
AllenKll
12/10/2002 01:30

--- Day 10: Cathode-Ray Tube ---

This is an easier to read output for the part 2 problem.
"""

file = open("input.txt", "r", encoding="ascii")  # , newline='\r\n')
line = "null"

register = 1
cycle = 1

wait = 0  
screenClock = 0
screen = [  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ']

def printScreen(scrn):
    print("".join(scrn))

while line:
    if screenClock == 40:
        screenClock = 0
        printScreen(screen)
        screen = [  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ',  '  ' ]

    if register - 1 <= screenClock and register + 1 >= screenClock:
        screen[screenClock] = "##"
    
    if wait == 0:
        line = file.readline()
        if not line:
            break
        line  = line.strip()

        splt = line.split(" ")
        instruction = splt[0]

        if instruction == "noop":
            pass
        elif instruction == "addx":
            wait = 1
    else:
        wait -=1
        if wait == 0:
            register += eval(splt[1])
    

    cycle += 1
    screenClock += 1


