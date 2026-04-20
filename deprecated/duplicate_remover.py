"""
It just removes the duplicates in a text file, essential for word game.
You may ask, why does words get duplicated in the first place.
There could be multiple reason:
Sometimes both API's can be very very slow or unresponsive, more than one person wrote the same word,
one person wrote the same word multiple times (spammed) or maybe just home computer froze for a couple seconds.
"""

import sys
#Filename will be first argument.

tmplist = []

with open(sys.argv[1], 'r') as f:
    contents = f.read()
    contents = contents.split()
    f.close()
for word in contents:
    if word not in tmplist:
        tmplist.append(word)

tmpstring = '\n'.join(tmplist)
print(tmpstring)
with open(sys.argv[1], 'w') as f:
    f.write(tmpstring)
