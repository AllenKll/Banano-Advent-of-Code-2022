"""
Created on Thu Dec  8 16:46:04 2022

@author: AllenKll

--- Day 7: No Space Left On Device ---
--- Part Two ---
Now, you're ready to choose a directory to delete.

The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000. You need to find a directory you can delete that will free up enough space to run the update.

In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165; this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required by the update. Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run.

To achieve this, you have the following options:

Delete directory e, which would increase unused space by 584.
Delete directory a, which would increase unused space by 94853.
Delete directory d, which would increase unused space by 24933642.
Delete directory /, which would increase unused space by 48381165.
Directories e and a are both too small; deleting them would not free up enough space. However, directories d and / are both big enough! Between these, choose the smallest: d, increasing unused space by 24933642.

Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?

Your puzzle answer was 3696336.
"""
from collections import deque

file = open("input.txt", "r", encoding="ascii")  # , newline='\r\n')
#file = open("test.txt", "r", encoding="ascii")  # , newline='\r\n')
line = "1"

path = []
sizes = {}
size = 0

while line:
    line = file.readline()
    line  = line.strip()
    if "$ cd " in line:
        sizeEntry = "/".join(path)
        if sizeEntry in sizes:
            sizes[sizeEntry] = sizes[sizeEntry] + size
        else:
            sizes[sizeEntry] = size
        dirName = line[4:].strip()
        if dirName == "..":
            #store the size
            path.pop()
            # add subdirectory to the parent
            parentEntry = "/".join(path)
            sizes[parentEntry] = sizes[parentEntry] + sizes[sizeEntry]
        else:
            path.append(dirName)
        size = 0
        continue
    elif "$ ls" == line:
        continue

    split = line.split(" ") 
    if split[0].isnumeric():
        size += eval(split[0])

### clean up the path and do final add ups
sizeEntry = "/".join(path)
#store the size
if sizeEntry in sizes:
    sizes[sizeEntry] = sizes[sizeEntry] + size
else:
    sizes[sizeEntry] = size

# climb up the tree
while len(path) > 1:
    path.pop()
    # add subdirectory to the parent
    parentEntry = "/".join(path)
    sizes[parentEntry] = sizes[parentEntry] + sizes[sizeEntry]

maxSize = 43598597999
for dir, sz in sizes.items():
    if sz > 3598595 and sz < maxSize:
        maxSize = sz

print(maxSize)
