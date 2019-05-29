#!/usr/bin/env python3

""" wordfind.py: class for building wordfind puzzles """

__author__ = "Drew Hynes"
__copyright__ = "Copyright 2019"
__credits__ = ["Drew Hynes"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Drew Hynes"
__email__ = "drew.hynes@gmail.com"
__status__ = "In Development"


import random

"""
this is the direction mapping

8    1    2

7    -    3

6    5    4
"""

class Wordfind(object):
    
    puzzle = ''
    # this builds an empty grid
    def buildGrid(self, h, w):
        lines = []
        for line in range(0,h):
            # we need to build a line, ya?
            l = []
            for char in range(0,w):
                l.append('+')
            lines.append(l)
        self.puzzle = lines
        return lines # perhaps a better return?

    # this prints out the puzzle
    def printGrid(self, p):
        i = 0;
        for line in puzzle:
            print("%s: %s"%(i, line))
            i += 1

    # this prints out the puzzle
    def printCleanGrid(self, p):
        for line in p:
            print(line)

    # put a word into the field, this function checks nothing at all!
    def putWord(self, w, direction, line, char):
        if direction == 1:
            # flowing word up, line changes, character does not
            c = 0
            for ch in w: 
                self.puzzle[line][char] = w[c]
                line -= 1
                c += 1
        elif direction == 2:
            # flowing up-right, gets tricky
            # char increases, line decreases
            c = 0
            for ch in w:
                self.puzzle[line][char] = w[c]
                char += 1
                line -= 1
                c += 1
        elif direction == 3:
            # flowing word to the right, line will not change
            c = 0
            while char <= len(w) + 1:
                self.puzzle[line][char] = w[c]
                char += 1
                c += 1
        elif direction == 4:
            # flowing down-right
            # char increases, line increases
            c = 0
            for ch in w:
                self.puzzle[line][char] = w[c]
                char += 1
                line += 1
                c += 1
        elif direction == 5:
            # flowing down
            # char doesnt change, line increases
            c = 0
            for ch in w:
                self.puzzle[line][char] = w[c]
                line += 1
                c += 1
        elif direction == 6:
            # flowing down-left
            # char decreases, line increases
            c = 0
            for ch in w:
                self.puzzle[line][char] = w[c]
                char -= 1
                line += 1
                c += 1
        elif direction == 7:
            # flowing left
            # char decreases, line does not change
            c = 0
            for ch in w:
                self.puzzle[line][char] = w[c]
                char -= 1
                c += 1
        elif direction == 8:
            # flowing up-left
            # char decreases, line decreases
            c = 0
            for ch in w:
                self.puzzle[line][char] = w[c]
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
