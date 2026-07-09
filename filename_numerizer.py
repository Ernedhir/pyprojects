"""
This script will change every file in only the given directory. Every file will be 20 chars long. Filetype does not matter.
Every 70 files, first number will be changed. It's for indexing.
"""

import os
import math
import secrets

folder = input("Dir Path:")

used = []
i = 1

for filename in os.listdir(folder):
    path = os.path.join(folder, filename)

    if not os.path.isfile(path):
        continue

    ext = os.path.splitext(filename)[1]

    while True:
        k = (i-1)//70 + 1
        number = (str(k) if not k > 9 else (str(k)+"_")) + "".join(str(secrets.randbelow(10)) for _ in range(18 if k > 9 else 19))
        if number not in used:
            used.append(number)
            i +=1
            break

    os.rename(path, os.path.join(folder, number + ext))
