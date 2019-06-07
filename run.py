#!/usr/bin/env python3

from wordfind import Wordfind

wf = Wordfind()
wf.buildGrid(15,15)

wf.putWord('BRAVO',1,5,5)
wf.putWord('TOSS',1,14,14)
wf.putWord('ROTE',2,14,0)
wf.putWord('MITE',4,0,0)
wf.putWord('TACO',5,0,14)
wf.putWord('BOAT',6,0,12)
wf.putWord('BOTTOM',7,14,12)
wf.putWord('ROOK',8,9,3)

#print(wf.printCleanGrid(wf.puzzle))

#print(wf.checkWordOverlap('CAT',3,0,4))

if wf.checkWordIntersect('DOG', 3, 12, 12) == False:
    # this incidates there is an intersection
    print("check for overlap")

new_words = ['BEEP','BOOP','NOSE','WIND']
#print(wf.puzzle[4][0])
#print(wf.puzzle[4][1])
#print(wf.puzzle[4][2])
#print(wf.puzzle[4][3])
#r_line, r_char = wf.pickLocation()

wf.printCleanGrid_alt1(wf.puzzle)
print("Begin Word insertion")

for word in new_words:
    # lets get a direction and a location
    r_line, r_char = wf.pickLocation()
    r_direction = wf.pickDirection()

    # time for a bounds check
    if wf.checkWord(word, r_direction, r_line, r_char):
        # True indicates word will fit!
        # now we need to check intersection
        if wf.checkWordIntersect(word, r_direction, r_line, r_char):
            # no intersection found, we can safely place the word!
            #wf.putWord('ROOK',8,9,3)
            wf.putWord(word, r_direction, r_line, r_char)
            print("Successfully placed %s" % word)
        else:
            # word intersection found, need to check further
            pass
    else:
        # False indicates it will go out of bounds
        pass

print("Word insertion phase Complete")
wf.printCleanGrid_alt1(wf.puzzle)
