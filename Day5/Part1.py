"""
Created on Mon Dec  7 20:13:04 2022

@author: AllenKll
--- Day 5: Supply Stacks ---
The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?

Your puzzle answer was TGWSMRBPN.

"""
from collections import deque

file = open("input.txt", "r")  # , newline='\r\n')
# file = open("debug.txt", "r" ) #, newline='\r\n')
line = file.readline()

#reading in the starting positions would be a pain in the ass due to the format, so we will hard code them.
"""
[M]                     [N] [Z]    
[F]             [R] [Z] [C] [C]    
[C]     [V]     [L] [N] [G] [V]    
[W]     [L]     [T] [H] [V] [F] [H]
[T]     [T] [W] [F] [B] [P] [J] [L]
[D] [L] [H] [J] [C] [G] [S] [R] [M]
[L] [B] [C] [P] [S] [D] [M] [Q] [P]
[B] [N] [J] [S] [Z] [W] [F] [W] [R]
 1   2   3   4   5   6   7   8   9 
"""

stacks = []
stacks.append( deque('MFCWTDLB'))
stacks.append( deque('LBN'))
stacks.append( deque('VLTHCJ'))
stacks.append( deque('WJPS'))
stacks.append( deque('RLTFCSZ'))
stacks.append( deque('ZNHBGDW'))
stacks.append( deque('NCGVPSMF'))
stacks.append( deque('ZCVFJRQW'))
stacks.append( deque('HLMPR'))

def doMove(fromStack, toStack, numItems):
    for i in range(numItems):
        stacks[toStack-1].appendleft(stacks[fromStack-1].popleft())

lineNumber = 11

while line:
    line  = line.strip()
    
    if not "move" in line:
        line = file.readline()
        continue
    
    splt = line.split(' ')
    numItems  = eval(splt[1])
    fromStack = eval(splt[3])
    toStack   = eval(splt[5])

    doMove(fromStack, toStack, numItems)

    line = file.readline()
    lineNumber = lineNumber + 1

output = []
for stack in stacks:
    output.append(stack[0])

print("".join(output))