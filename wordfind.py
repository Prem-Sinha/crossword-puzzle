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
        for line in range(h):
            # we need to build a line, ya?
            l = []
            for char in range(w):
                l.append('+')
            lines.append(l)
        self.puzzle = lines
        #buildGrid affect self.puzzle; it doesn't need to return anything

    # this prints out the puzzle
    def printCleanGrid(self, p):
        for line in p:
            print(line)
            
    # pretty alternative print functions
    def printCleanGrid_alt1(self, p):
        for line in p:
            for l in line:
                print(l, end=' ')
            print()
    # pretty alternative print functions
    def printCleanGrid_alt2(self, p):
        for line in p:
            for l in line:
                print(l, end=' | ')
            print()
            for l in line:
                print("--", end='--')
            print()

    # pick random direction
    def pickDirection(self):
        d = random.randint(1,8)
        return d
    
    # pick random line/char combo
    # this function will keep searching until it finds a clear space, use wisely
    def pickLocation(self):
        r_line = random.randint(0,14)
        r_char = random.randint(0,14)
        if self.puzzle[r_line][r_char] == '+':
            # found a good spot
            return r_line, r_char
        else:
            while self.puzzle[r_line][r_char] != '+':
                r_line = random.randint(0,14)
                r_char = random.randint(0,14)

            # now lets return
            return r_line, r_char

    # A Much smaller function to put a word into the field
    # this one checks nothing, too!
    def putWordPlus(self, w, direction, line, char):
        dirchange = [[],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1]]
        charchange = dirchange[direction][0]
        linechange = dirchange[direction][1]
        for ch in w:
            self.puzzle[line][char] = ch
            char += charchange
            line += linechange
    #The list contains lists explaining how much to change
    #char and list by for each direction.
    #The first element is a blank list beacuse
    #there is no direction 0.
    
    # original putWord
    # UNUSED FUNCTION
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
    
    #UNUSED FUNCTION
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

    #UNUSED FUNCTION
    # check a single line/char location for presence of existing characters or empty marker
    def checkLocation(self, line, char):
        return (self.puzzle[line][char] == "+")

    # check if word will spill out of the bounds of the puzzle
    # returns True if word fits, False if it does not
    def checkWord(self, w, direction, line, char):
        # 
        # first a simple bounds check
        #
        if direction == 1:
            # up
            return not(line <= len(w))
                #returned False:
                #print("will go out of bounds")
                #print("word: %s, direction: up, line: %s, char: %s" % (w, line, char))
                #returned True:
                #print("shouldn't go out of bounds")
                #print("word: %s, direction: up, line: %s, char: %s" % (w, line, char))
        elif direction == 2:
            # up-right
            return not(line - len(w) <= 0 or char + len(w) > 14)
        elif direction == 3:
            # right
            return not(char + len(w) > 14)
        elif direction == 4:
            # down-right
            return not(line + len(w) > 14 or char + len(w) > 14)
        elif direction == 5:
            # down
            return not(line + len(w) > 14)
        elif direction == 6:
            # down-left
            return not(line + len(w) > 14 or char - len(w) < 0)
        elif direction == 7:
            # left
            return not(char - len(w) < 0)
        elif direction == 8:
            # up-left
            return not(line - len(w) < 0 or char - len(w) < 0)
        else:
            pass
            # this should never happen
            #return False
    

    # find specific character(s) of intersection
    def checkWordOverlap(self, w, direction, line, char):
        pass # nothing to do right now, this needs to be fleshed out
    
    # returns False if there is a word intersection, True if there is NOT

    def checkWordIntersect(self, w, direction, line, char):
        # returns False if something is blocking/intersecting

        # this function will not check if something would flow out of bounds
        # that needs to be done BEFORE using this function

        if direction == 1:
            # up
            endLine = line - len(w) + 1 # needs to be +1 instead of -1 for some reason?
            inc = line
            while inc >= endLine:
                if self.puzzle[inc][char] != '+':
                    return False
                #False returned immediately on encountering intersect
                else:
                    pass
                inc -= 1
        elif direction == 2:
            # up-right
            endLine = line - len(w) - 1
            inc = line
            while inc >= endLine:
                if self.puzzle[inc][char] != '+':
                    return False
                else:
                    pass
                inc -= 1
                char += 1
        elif direction == 3:
            # right
            endChar = char + len(w) - 1
            inc = char
            while inc <= endChar:
                if self.puzzle[line][inc] != '+':
                    # something here, cant place a character
                    return False
                else:
                    # nothing here, we are good
                    pass
                inc += 1
        elif direction == 4:
            # down-right
            endChar = char + len(w) - 1
            inc = char
            while inc <= endChar:
                if self.puzzle[line][inc] != '+':
                    return False
                else:
                    pass
                inc += 1
                line += 1
        elif direction == 5:
            # down
            endLine = line + len(w) - 1
            inc = line
            while inc <= endLine:
                if self.puzzle[inc][char] != '+':
                    return False
                else:
                    pass
                inc += 1
        elif direction == 6:
            # down-left
            endLine = line + len(w) - 1
            while line <= endLine:
                if self.puzzle[line][char] != '+':
                    return False
                else:
                    pass
                line += 1
                char -= 1
        elif direction == 7:
            # left
            endChar = char - len(w) + 1
            while char >= endChar:
                if self.puzzle[line][char] != '+':
                    return False
                else:
                    pass
                char -= 1
        elif direction == 8:
            # up-left
            endChar = char - len(w) + 1
            while char >= endChar:
                #print("LINE: %s CHAR: %s = %s" % (line, char, self.puzzle[line][char]))
                if self.puzzle[line][char] != '+':
                    return False
                else:
                    pass
                char -= 1
                line -= 1
        else:
            pass
        return True
        #True returned if no intersect found
