import os
import sys
import platform

IS_WINDOWS = platform.system() == "Windows"

FILE_NAME = sys.argv[1]
LIMIT = 2000

os.makedirs("msgs", exist_ok=True)

def duplicate_remover(linklist): # ITS NOT OPTIMIZED YES I KNOW
    tmplist = []

    for word in linklist:
        if word not in tmplist:
            tmplist.append(word)
    return tmplist

with open(FILE_NAME, 'r', encoding='utf-8') as f:
    conts = f.read().splitlines()

contents = []
for c in conts:
    if c[:8] == 'https://':
        contents.append(c)
contents = duplicate_remover(contents)

chunk = ''
file_index = 0

for p in contents:
    candidate = chunk + p + ('\r\n' if IS_WINDOWS else '\n')

    if len(candidate) < LIMIT:
        chunk = candidate
        print(f'Appended: {p} (at msg_{file_index}.txt ({len(chunk)}))')
    else:
        filename = os.path.join('msgs', f'msg_{file_index}.txt')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(chunk)
        print(f'Wrote: {filename} ({len(chunk)})')
        file_index += 1
        chunk = p + ('\r\n' if IS_WINDOWS else '\n')

if chunk:
    filename = os.path.join('msgs', f'msg_{file_index}.txt')
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(chunk)
    print(f'Wrote: {filename} ({len(chunk)})')
