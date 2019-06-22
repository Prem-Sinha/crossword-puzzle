#!/usr/bin/env python3

""" wordfind.py: class for building wordfind puzzles """

__author__ = "Drew Hynes"
__copyright__ = "Copyright 2019"
__credits__ = ["Prem Sinha, Drew Hynes"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Prem Sinha"
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
    size = ()
    words = set()

    # this builds an empty grid
    def buildGrid(self, h, w):
        self.size = (h, w)
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
    def printCleanGrid(self):
        for line in self.puzzle:
            print(line)

    # pretty alternative print functions
    def printCleanGrid_alt1(self):
        for line in self.puzzle:
            for l in line:
                print(l, end=' ')
            print()

    # pretty alternative print functions
    def printCleanGrid_alt2(self):
        for line in self.puzzle:
            for l in line:
                print(l, end=' | ')
            print()
            for _ in line:
                print("--", end='--')
            print()

    # pick random direction
    def pickDirection(self):
        return random.randint(1, 8)

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
        if w not in self.words:
            self.words.add(w.upper())
            dirchange = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
            char_change = dirchange[direction-1][0]
            line_change = dirchange[direction-1][1]
            for ch in w:
                self.puzzle[line][char] = ch.upper()
                char += char_change
                line += line_change
    # The list contains lists explaining how much to change
    # char and list by for each direction.
    # The first element is a blank list because
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

    # New function with shorter code. Returns intersecting characters
    # Also allows overlap if the same letter is repeated
    def checkWordIntersectPlus(self, w, direction, line, char):
        # Returns dictionary of characters that are blocking/intersecting.
        # If dictionary is empty, it means there are no intersections

        # this function will not check if something would flow out of bounds
        # that needs to be done BEFORE using this function
        intersect = {}
        dirchange = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
        char_change = dirchange[direction-1][0]
        line_change = dirchange[direction-1][1]
        for ch in w:
            prev = self.puzzle[line][char]
            if prev != '+' and prev != ch:
                intersect[(line, char)] = prev
            char += char_change
            line += line_change
        return intersect
        # False (empty dictionary) returned if no intersect found

    # UNUSED FUNCTION
    # bulk place takes a list of words and inserts them
    def bulkPlace(self, wordlist):
        for word in wordlist:
            r_line, r_char = self.pickLocation()
            r_direction = self.pickDirection()
            # bounds check time
            # print("PROCESSING: %s" % wordlist[r_word])
            # print("r_direction: %s r_line: %s r_char %s" % (r_direction, r_line, r_char))
            if self.checkWord(word, r_direction, r_line, r_char):
                # true indicates the word fits
                word_intersect = self.checkWordIntersectPlus(word, r_direction, r_line, r_char)
                if not word_intersect:
                    # true here (false word_intersect) indicates no intersections detected!
                    self.putWordPlus(word, r_direction, r_line, r_char)
                    # print("successfully placed %s" % wordlist[r_word])
                else:
                    print("Could not place %s (Intersect)" % word)
                    print("Blocking characters:", word_intersect)
            else:
                print("Could not place %s (Bounds)" % word)
                # false here indicates out of bounds word 

    # fill in the empty stuff
    # This function does not check for the unintentional
    # addition of other, valid words.
    def fillPuzzle(self):
        for line in range(self.size[0]):
            for char in range(self.size[1]):
                if self.puzzle[line][char] == '+':
                    # we need to replace
                    self.puzzle[line][char] = chr(random.randint(65, 90))

    # function to search for words and solve puzzle
    # will be later used to ensure the absence of unwanted words
    def searcher(self, v=False):
        dirchange = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
        # check over grid first or words first?
        if v: print(f"Words to find:\n{self.words}")
        first_letters = set(i[0] for i in self.words)
        if v: print(first_letters)
        for line in range(self.size[0]):
            for char in range(self.size[1]):
                if v: print("Initial position", line, char)
                if self.puzzle[line][char] in first_letters:
                    for w in self.words:
                        if v: print("Possibility of", w)
                        if self.puzzle[line][char] == w[0]:
                            for d in range(1, 9):
                                if v: print("Direction, first letter", d, w[0])
                                if self.checkWord(w, d, line, char):
                                    fit = True
                                    char_change = dirchange[d - 1][0]
                                    line_change = dirchange[d - 1][1]
                                    line_2 = line + line_change
                                    char_2 = char + char_change
                                    for i in range(1, len(w)):
                                        if v: print("Letter and number, position to be checked", w[i], i, line_2, char_2)
                                        if self.puzzle[line_2][char_2] != w[i]:
                                            fit = False
                                            break
                                        char_2 += char_change
                                        line_2 += line_change
                                    if fit:
                                        print(f"\t{w} was found at ({line}, {char}).")
