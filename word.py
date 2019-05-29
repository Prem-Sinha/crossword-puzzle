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

# put a word into the field, this function checks nothing at all!
def putWord(w, direction, line, char):
    if direction == 1:
        # flowing word up, line changes, character does not
        c = 0
        for ch in w: 
            puzzle[line][char] = w[c]
            line -= 1
            c += 1
    elif direction == 2:
        # flowing up-right, gets tricky
        # char increases, line decreases
        c = 0
        for ch in w:
            puzzle[line][char] = w[c]
            char += 1
            line -= 1
            c += 1

    elif direction == 3:
        # flowing word to the right, line will not change
        c = 0
        while char <= len(w) + 1:
            puzzle[line][char] = w[c]
            char += 1
            c += 1
    elif direction == 4:
        # flowing down-right
        # char increases, line increases
        c = 0
        for ch in w:
            puzzle[line][char] = w[c]
            char += 1
            line += 1
            c += 1
    elif direction == 5:
        # flowing down
        # char doesnt change, line increases
        c = 0
        for ch in w:
            puzzle[line][char] = w[c]
            line += 1
            c += 1
    elif direction == 6:
        # flowing down-left
        # char decreases, line increases
        c = 0
        for ch in w:
            puzzle[line][char] = w[c]
            char -= 1
            line += 1
            c += 1
    elif direction == 7:
        # flowing left
        # char decreases, line does not change
        c = 0
        for ch in w:
            puzzle[line][char] = w[c]
            char -= 1
            c += 1
    elif direction == 8:
        # flowing up-left
        # char decreases, line decreases
        c = 0
        for ch in w:
            puzzle[line][char] = w[c]
            char -= 1
            line -= 1
            c += 1
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

# check a single line/char location for presence of existing characters or empty marker
def checkLocation(w, line, char):
    if puzzle[line][char] == "+":
        # valid place to put a character, nothing there yet
        return True
    elif puzzle[line][char] != "+":
        # not valid, there is already a character there
        return False
    else:
        # this should probably never happen
        pass

# check if word will spill out of the bounds of the puzzle
# returns True if word fits, False if it does not
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
    

# find specific character(s) of intersection
def checkWordOverlap(w, direction, line, char):
    # we will only work with a left search for now
    if direction == 3:
        condition = False
        # lets look right for intersects
        endChar = char + len(w) + 1
        inc = char
        i = 0
        while inc <= endChar:
            if puzzle[line][inc] != '+':
                # somethign here, cant place character
                #condition = False
                # we need to first determine the overlaps
                #print(line, inc)
                #print(puzzle[line][inc])
                #print(w[i])
                condition = True
                """
                if puzzle[line][inc] == w[inc - char + 1]:
                    print("line: %s char :%s"% (line, inc)) 
                    print(puzzle[line][inc],w[i])
                else:
                    # no match found
                    print("no match found on overlap")
                    print("line: %s char :%s"% (line, inc)) 
                    print(puzzle[line][inc],w[inc - char + 1])
                """  
            else:
                # nothing here, leave condition alone for now
                pass
            inc += 1
            i += 1
        if condition == True:
            return True
        else:
            return False

# check if word will spill out of the bounds of the puzzle
# returns False if there is a word intersection, True if there is NOT

def checkWordIntersect(w, direction, line, char):
    # returns False if something is blocking/intersecting
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
    elif direction == 2:
        condition = True
        # lets insert a up-right aligned word
        endLine = line - len(w) + 1
        # need to increment the char value since this is diagnoal
        inc = line
        while inc >= endLine:
            if puzzle[inc][char] != '+':
                # something here, cant place a character
                condition = False
            else:
                # nothing here, leave condition set to True
                pass
            # now lets increment char
            inc -= 1
            char += 1
        if condition == True:
            return True
        else:
            return False
    elif direction == 3:
        condition = True
        # lets look right for intersects
        endChar = char + len(w) + 1
        inc = char
        while inc <= endChar:
            if puzzle[line][inc] != '+':
                # somethign here, cant place character
                condition = False
            else:
                # nothing here, leave condition alone for now
                pass
            inc += 1
        if condition == True:
            return True
        else:
            return False
    elif direction == 4:
        condition = True
        # checking down-right
        endChar = char + len(w) + 1
        inc = char
        while inc <= endChar:
            if puzzle[line][inc] != '+':
                condition = False
            else:
                pass
            inc += 1
            line += 1
        if condition == True:
            return True
        else:
            return False
    elif direction == 5:
        condition = True
        # checking down
        endLine = line + len(w) + 1
        inc = line
        while inc <= endLine:
            if puzzle[inc][char] != '+':
                condition = False
            else:
                pass
            inc += 1
        if condition == True:
            return True
        else:
            return False
    elif direction == 6:
        condition = True
        # checking down-left
        endLine = line + len(w) + 1
        inc = line
        while inc <= endLine:
            if puzzle[inc][char] != '+':
                condition = False
            else:
                pass
            inc += 1
            char -= 1
        if condition == True:
            return True
        else:
            return False
    elif direction == 7:
        condition = True
        # checking left
        endChar = char - len(w) + 1
        inc = char
        while inc >= endChar:
            if puzzle[line][inc] != '+':
                condition = False
            else:
                pass
            inc -= 1
        if condition == True:
            return True
        else:
            return False
    elif direction == 8:
        condition = True
        # checking up-left
        endChar = char - len(w) + 1
        inc = char
        while inc >= endChar:
            if puzzle[line][inc] != '+':
                condition = False
            else:
                pass
            inc -= 1
            line -= 1
        if condition == True:
            return True
        else:
            return False
        
print("\n\n\n")
puzzle = buildGrid(15,15)

words = ['ALPHA','BRAVO','CHARLIE','DELTA']

puzzle[5][5] = 'B'
puzzle[4][5] = 'R'
puzzle[3][5] = 'A'
puzzle[2][5] = 'V'
puzzle[1][5] = 'O'

"""
puzzle[3][3] = 'B'
puzzle[4][3] = 'A'
puzzle[5][3] = 'R'
puzzle[6][3] = 'G'
"""

"""
puzzle[2][8] = 'D'
puzzle[3][8] = 'U'
puzzle[4][8] = 'D'
puzzle[2][8] = 'E'
"""
printCleanGrid(puzzle)


word = 'GOATS'
"""
# checking the correct movements for putWord()
putWord('TOSS',1,14,14)
putWord('ROTE',2,14,0)
putWord('MITE',4,0,0)
putWord('TACO',5,0,14)
putWord('BOAT',6,0,12)
putWord('BOTTOM',7,14,12)
putWord('ROOK',8,9,3)
printCleanGrid(puzzle)
"""

"""
if checkWordIntersect(word,3,4,3) == False:
    print("there is an intersection, we need to check some other things first before excluding this location")
    if checkWordOverlap(word,3,4,3) == True:
        # good to go, lets put a word into play!
        putWord(word,3,4,3)
        printCleanGrid(puzzle)
else:
    print("no intersection found at all")
"""
