# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:38:04 2022

@author: AllenKll

--- Part Two ---
It seems like there is still quite a bit of duplicate work planned. Instead, 
the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, 
while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do 
overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?

Your puzzle answer was 833.
"""

total = 0

file = open("input.txt", "r")  # , newline='\r\n')
# file = open("debug.txt", "r" ) #, newline='\r\n')
line = file.readline()

while line:
    line  = line.strip()
    
    splt = line.split(',')
    se1 = splt[0].split('-')
    se2 = splt[1].split('-')
    
    #convert all to integers
    se1 = [eval(i) for i in se1]
    se2 = [eval(i) for i in se2]
    
    sections1 = list(range(se1[0], se1[1]+1))
    sections2 = list(range(se2[0], se2[1]+1))

    for section in sections1:
        if section in sections2:
            total = total + 1
            break
    
    line = file.readline()

print(total)





























