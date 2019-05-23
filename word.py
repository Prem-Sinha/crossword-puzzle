#!/usr/bin/python3

import random

"""
this is the direction mapping

8    1    2

7    -    3

6    5    4
"""

# initial grid builder, just fills with + 
def buildGrid(h, w):
    lines = []
    for line in range(0,h):
        # we need to build a line, ya?
        l = []
        for char in range(0,w):
            l.append('+')
        lines.append(l)
    return lines

# this prints out the puzzle
def printGrid(p):
    i = 0;
    for line in puzzle:
        print("%s: %s"%(i, line))
        i += 1

# this prints out the puzzle
def printCleanGrid(p):
    for line in puzzle:
        print(line)

# this function picks a location for a word, hopefully smartly
def placeWord(w, puzzle):
    # now we pick a direction for this word
    #direction = random.randint(1,8)

    # for now we work with a static direction, uncomment the previous line later
    direction = 1 # we are testing up to start with

    # first we must pick the location of the first letter
    rLine = random.randint(0,14)
    rChar = random.randint(0,14)
    if puzzle[rLine][rChar] == "+":
        # free space, lets do it
        print("good to go, no character placed here yet")
        if checkWord(w, direction, rLine, rChar) == True and checkWordIntersect(w, direction, rLine, rChar) ==  True:
            if direction == 1:
                # lets insert a word upwards
                endLine = rLine - len(w) + 1 # this math checks out!
                #print("rLine: %s , endLine: %s" % (rLine,endLine))
                inc = rLine
                ch = 0
                while inc >= endLine:
                    puzzle[inc][rChar] = w[ch] 
                    inc -=  1
                    ch += 1
            return puzzle
    elif puzzle[rLine][rChar] != "+":
        # something is here, cant do it man
        print("error: space is used already")
    else:
        print("definitely cant do anything here")

#
# All check() functions need to only return True/False
#

# check if word will spill out of the bounds of the puzzle
def checkWord(w, direction, line, char):
    # 
    # first a simple bounds check
    #
    if direction == 1:
        # up
        if line <= len(w):
            return False
            #print("will go out of bounds")
            #print("word: %s, direction: up, line: %s, char: %s" % (w, line, char))
        else:
            return True
            #print("shouldn't go out of bounds")
            #print("word: %s, direction: up, line: %s, char: %s" % (w, line, char))
    elif direction == 2:
        # up-right
        if line - len(w) <= 0 or char + len(w) > 14:
            return False
        else:
            return True
    elif direction == 3:
        # right
        if char + len(w) > 14:
            return False
        else:
            return True
    elif direction == 4:
        # down-right
        if line + len(w) > 14 or char + len(w) > 14:
            return False
        else:
            return True
    elif direction == 5:
        # down
        if line + len(w) > 14:
            return False
        else:
            return True
    elif direction == 6:
        # down-left
        if line + len(w) > 14 or char - len(w) < 0:
            return False
        else:
            return True
    elif direction == 7:
        # left
        if char - len(w) < 0:
            return False
        else:
            return True
    elif direction == 8:
        # up-left
        if line - len(w) < 0 or char - len(w) < 0:
            return False
        else:
            return True
    else:
        # this should never happen
        return False
    

# check if word will spill out of the bounds of the puzzle
def checkWordIntersect(w, direction, line, char):
    if direction == 1:
        condition = True
        # lets insert a word upwards
        endLine = line - len(w) + 1 # this math checks out!
        #print("rLine: %s , endLine: %s" % (rLine,endLine))
        inc = line
        ch = 0
        while inc >= endLine:
            if puzzle[inc][char] != '+':
                # this incidates there is something in space we would occupy
                condition = False
            else:
                # this should only happen if space has a +
                pass
            inc -=  1
            ch += 1
        if condition == True:
            # we are good to insert, no failures picked up
            return True
        else:
            return False
    
print("\n\n\n")
puzzle = buildGrid(15,15)
#printGrid(puzzle)
#print(puzzle[1][2])
# excellent, we can access thins just a i thought line,character

words = ['ALPHA','BRAVO','CHARLIE','DELTA']


#p = placeWord(words[1], puzzle)
#printCleanGrid(p)
"""
for word in words:
    puzzle = placeWord(word, puzzle)
    printCleanGrid(puzzle)
"""
print(checkWord('SAVAGE', 8, 12, 3))
