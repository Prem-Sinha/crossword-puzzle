#!/usr/bin/env python3

from wordfind import Wordfind

words_cache = open("Oxford5000.txt", "r")

'''# words_cache = "Oxford5000.txt"
wf.build_cache(words_cache)'''

# wf = Wordfind(15, 15, "Oxford5000.txt")
wf = Wordfind(15, 15, words_cache)

print(wf.cache)

wf.putWordPlus('BRAVO', 1, 5, 5)
wf.putWordPlus('TOSS', 1, 14, 14)
wf.putWordPlus('ROTE', 3, 14, 0)
wf.putWordPlus('MITE', 4, 0, 0)
wf.putWordPlus('TACO', 5, 0, 14)
wf.putWordPlus('BOAT', 6, 0, 12)
wf.putWordPlus('BOTTOM', 7, 14, 12)
wf.putWordPlus('ROOK', 8, 9, 3)
wf.putWordPlus('SPLIT', 6, 6, 7)
wf.putWordPlus('SPREAD', 4, 6, 7)

NW = input("Enter more words: ")
if NW:
    new_words = NW.split()
else:
    new_words = ['BEEP', 'BOOP', 'NOSE', 'WIND']

wf.printCleanGrid_alt1()
print("Begin Word insertion")

for word in new_words:
    # lets get a direction and a location
    r_line, r_char = wf.pickLocation()
    r_direction = wf.pickDirection()

    # time for a bounds check
    if wf.checkWord(word, r_direction, r_line, r_char):
        # True indicates word will fit!
        # now we need to check intersection
        WordIntersect = wf.checkWordIntersectPlus(word, r_direction, r_line, r_char)
        if not WordIntersect:
            # no intersection found, we can safely place the word!
            # wf.putWordPlus('ROOK',8,9,3)
            wf.putWordPlus(word, r_direction, r_line, r_char)
            print("Successfully placed %s" % word)
        else:
            print("Could not place %s (Intersect)" % word)
            print("Blocking characters:", WordIntersect)
            # word intersection found, need to check further
    else:
        print("Could not place %s (Bounds)" % word)
        # False indicates it will go out of bounds

print("Word insertion phase Complete")
wf.printCleanGrid_alt1()

print("\nGrid filled with letters")
wf.fillPuzzle()
wf.printCleanGrid_alt1()

print("Running searcher function to solve puzzle.")
wf.searcher()

words_cache.close()
