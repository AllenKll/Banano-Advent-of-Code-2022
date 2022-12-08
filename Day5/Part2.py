"""
Created on Mon Dec  7 20:13:04 2022

@author: AllenKll
--- Day 5: Supply Stacks ---
--- Part Two ---
As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?

Your puzzle answer was TZLTLWRNF.



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
stacks.append( list('MFCWTDLB'))
stacks.append( list('LBN'))
stacks.append( list('VLTHCJ'))
stacks.append( list('WJPS'))
stacks.append( list('RLTFCSZ'))
stacks.append( list('ZNHBGDW'))
stacks.append( list('NCGVPSMF'))
stacks.append( list('ZCVFJRQW'))
stacks.append( list('HLMPR'))

def doMove(fromStack, toStack, numItems):
    moving = stacks[fromStack-1][:numItems]
    del(stacks[fromStack-1][:numItems])
    stacks[toStack-1] = moving + stacks[toStack-1]

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