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
        for l in range(h):
            # we need to build a line, ya?
            line = []
            for char in range(w):
                line.append('+')
            lines.append(line)
        self.puzzle = lines
        # buildGrid affect self.puzzle; it doesn't need to return anything

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
        d = random.randint(1, 8)
        return d

    # pick random line/char combo
    # this function will keep searching until it finds a clear space, use wisely
    def pickLocation(self):
        r_line = random.randint(0, 14)
        r_char = random.randint(0, 14)
        if self.puzzle[r_line][r_char] == '+':
            pass
            # found a good spot
        else:
            while self.puzzle[r_line][r_char] != '+':
                r_line = random.randint(0, 14)
                r_char = random.randint(0, 14)
    # now lets return
        return r_line, r_char

    # alternate putWord 
    # A Much smaller function to put a word into the field
    # this one checks nothing, too!
    def putWordPlus(self, w, direction, line, char):
        dirchange = [[], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
        charchange = dirchange[direction][0]
        linechange = dirchange[direction][1]
        for ch in w:
            self.puzzle[line][char] = ch.upper()
            char += charchange
            line += linechange
    # The list contains lists explaining how much to change
    # char and list by for each direction.
    # The first element is a blank list beacuse
    # there is no direction 0.

    # UNUSED FUNCTION
    # check a single line/char location for presence of existing characters or empty marker
    def checkLocation(self, line, char):
        return self.puzzle[line][char] == "+"

    # check if word will spill out of the bounds of the puzzle
    # returns True if word fits, False if it does not
    def checkWord(self, w, direction, line, char):
        # 
        # first a simple bounds check
        #
        if direction == 1:
            # up
            return not(line <= len(w))
            # returned False:
            # print("will go out of bounds")
            # print("word: %s, direction: up, line: %s, char: %s" % (w, line, char))
            # returned True:
            # print("shouldn't go out of bounds")
            # print("word: %s, direction: up, line: %s, char: %s" % (w, line, char))
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
            # return False

    # find specific character(s) of intersection
    def checkWordOverlap(self, w, direction, line, char):
        pass  # nothing to do right now, this needs to be fleshed out

    # New function with shorter code. Returns intersecting characters
    # Also allows overlap if the same letter is repeated
    def checkWordIntersectPlus(self, w, direction, line, char):
        # Returns dictionary of characters that are blocking/intersecting.
        # If dictionary is empty, it means there are no intersections

        # this function will not check if something would flow out of bounds
        # that needs to be done BEFORE using this function
        intersect = {}
        dirchange = [[], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
        charchange = dirchange[direction][0]
        linechange = dirchange[direction][1]
        for ch in w:
            prev = self.puzzle[line][char]
            if prev != '+' and prev != ch:
                intersect[(line, char)] = prev
            char += charchange
            line += linechange
        return intersect
        # False (empty dictionary) returned if no intersect found

    # UNUSED FUNCTION
    # bulk place takes a list of words and inserts them
    def bulkPlace(self, wordlist):
        for word in wordlist:
            r_line, r_char = self.pickLocation()
            r_direction = self.pickDirection()
            # bounds check time
            #print("PROCESSING: %s" % wordlist[r_word])
            #print("r_direction: %s r_line: %s r_char %s" % (r_direction, r_line, r_char))
            if self.checkWord(word, r_direction, r_line, r_char):
                # true incidates the word fits
                WordIntersect = self.checkWordIntersectPlus(word, r_direction, r_line, r_char)
                if not WordIntersect:
                    # true here (false WordIntersect) indicates no intersections detected!
                    self.putWord(word, r_direction, r_line, r_char)
                    #print("successfully placed %s" % wordlist[r_word])
                else:
                    print("Could not place %s (Intersect)" % word)
                    print("Blocking characters:", WordIntersect)
            else:
                print("Could not place %s (Bounds)" % word)
                # false here indicates out of bounds word 

    # fill in the empty stuff
    # This function does not check for the unintentional
    # addition of other, valid words.
    def fillPuzzle(self):
        size = len(self.puzzle)
        for line in range(size):
            for char in range(size):
                if self.puzzle[line][char] == '+':
                    # we need to replace
                    self.puzzle[line][char] = chr(random.randint(65, 90))
