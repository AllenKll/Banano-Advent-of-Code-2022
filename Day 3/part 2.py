# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 09:38:04 2022

@author: AllenKll

--- Part Two ---
As you finish identifying the misplaced items, the Elves come to you with 
another issue.

For safety, the Elves are divided into groups of three. Every Elf carries a 
badge that identifies their group. For efficiency, within each group of three
Elves, the badge is the only item type carried by all three Elves. That is, if 
a group's badge is item type B, then all three Elves will have item type B 
somewhere in their rucksack, and at most two of the Elves will be carrying any 
other item type.

The problem is that someone forgot to put this year's updated authenticity 
sticker on the badges. All of the badges need to be pulled out of the rucksacks
so the new authenticity stickers can be attached.

Additionally, nobody wrote down which item type corresponds to each group's 
badges. The only way to tell which item type is the right one is by finding the
one item type that is common between all three Elves in each group.

Every set of three lines in your list corresponds to a single group, but each 
group can have a different badge item type. So, in the above example, the first
group's rucksacks are the first three lines:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
And the second group's rucksacks are the next three lines:

wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
In the first group, the only item type that appears in all three rucksacks is 
lowercase r; this must be their badges. In the second group, their badge item 
type must be Z.

Priorities for these items must still be found to organize the sticker 
attachment efforts: here, they are 18 (r) for the first group and 52 (Z) for 
the second group. The sum of these is 70.

Find the item type that corresponds to the badges of each three-Elf group. What
is the sum of the priorities of those item types?

Your puzzle answer was 2602.

"""

import re

total = 0

file = open("input1.txt", "r" ) #, newline='\r\n')
#file = open("debug.txt", "r" ) #, newline='\r\n')
line = file.readline()

while line:
    # get and trim three lines
    line2 = file.readline()
    line3 = file.readline()


    line = line.strip()
    line2 = line2.strip()
    line3 = line3.strip()
        
    #find all matches in line2 that appear in line 1
    matches = re.findall("["+line+"]", line2)
    
    # make unique (with set) and turn into a string for checking line 3
    matches = "".join(set(matches))
    
    # check line 3 for matches from 1 + 2
    matches = re.findall("["+matches+"]", line3)
    
    #no error checking is done as input is assumed correct.
    
    # turn the final match into a string for calulating value.
    matches = "".join(set(matches))
    
    val = ord(matches)
    if val >= ord('a') and val <= ord('z'):
        val = val - ord('a') + 1
    else:
        val = val - ord('A') + 27
        
    total = total + val
    
    line = file.readline()

print(total)


























