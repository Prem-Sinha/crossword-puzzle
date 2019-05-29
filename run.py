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

print(wf.printCleanGrid(wf.puzzle))
