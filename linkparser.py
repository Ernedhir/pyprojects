"""
This is a CLI tool for managing and processing link collections.

BUILT FOR PERSONAL USE.

Provides utilities for:
    - Converting concatenated links into readable newline-separated format (makeline)
    - Splitting large link collections into fixed-size message chunks (message_maker)
    - Removing duplicates from files or lists (duplicate_remover)

Designed to help organize, clean, and prepare link data for sharing and archival purposes
(e.g. Discord messages, personal backups, or external storage systems).
"""

import sys
import subprocess
import os
import platform

IS_WINDOWS = platform.system() == "Windows"

def duplicate_remover(linklist): # ITS NOT OPTIMIZED YES I KNOW
    tmplist = []

    for word in linklist:
        if word not in tmplist:
            tmplist.append(word)
    return tmplist

def remove_duplicate_from_file(fn: str): # ITS NOT OPTIMIZED YES I KNOW
    tmplist = []

    with open(fn, 'r', encoding='utf-8') as f:
        contents = f.read().splitlines()
    for word in contents:
        if word not in tmplist:
            tmplist.append(word)

    with open(fn, 'w', encoding='utf-8') as f:
        for word in tmplist:
            f.write(word + '\n')

def makeline(links, sep='https://'):
    i = 0
    output = ''

    for p in links.split(sep):
        if p:
            i += 1
            output += sep + p + '\n'

    print(i)
    subprocess.run('clip', input=output, text=True)

def message_maker(fn, limit=2000):
    contents = []
    os.makedirs("msgs", exist_ok=True)

    with open(fn, 'r', encoding='utf-8') as f:
        conts = f.read().splitlines()

    for c in conts:
        if c[:8] == 'https://':
            contents.append(c)
    contents = duplicate_remover(contents)
    
    chunk = ''
    file_index = 0

    for p in contents:
        candidate = chunk + p + ('\r\n' if IS_WINDOWS else '\n')

        if len(candidate) < limit:
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

def parse_message_args(args):
    limit = 4000
    file = None

    i=0
    while i < len(args):
        if args[i] == '-l' or args[i] == '--limit':
            i += 1
            limit = int(args[i])
            assert limit < 4000, "LIMIT EXCEEDED"
        else: file = args[i]
        i += 1

    if file is None: raise ValueError("PROVIDE INPUT FILE")
    return file, limit

def parse_line_args(args):
    sep = 'https://'
    file = None

    i=0
    while i < len(args):
        if args[i] == '-s' or args[i] == '--sep':
            i += 1
            sep = args[i]
        else: file = args[i]
        i += 1

    if file is None: raise ValueError("PROVIDE INPUT FILE")
    return file, sep

usage = """USAGE:
        \n    message <file> [--limit N] -  Extract all the links, split them into chunks (default 4000) and write them to \"msgs\" folder
        \n    line <links> [--sep <SEPARATOR>] -  Form a readable string from a concatenated string. Custom separator can be added. (default 'https://')
        \n    duplicate <file>                 -  Extract all the lines from a file, remove duplicates from them and rewrite the file."""

def main():
    match sys.argv[1].lower():
        case 'line':
            assert len(sys.argv) > 2, f"ERROR: NOT ENOUGH ARGUMENTS.\n{usage}"
            file_name, sep = parse_line_args(sys.argv[2:])
            makeline(file_name, sep)
        case 'message':
            assert len(sys.argv) > 2, f"ERROR: NOT ENOUGH ARGUMENTS.\n{usage}"
            file_name, limit = parse_message_args(sys.argv[2:])
            message_maker(file_name, limit)
        case 'duplicate':
            assert len(sys.argv) == 3, f"ERROR: PROVIDE INPUT FILE"
            remove_duplicate_from_file(sys.argv[2])
        case _:
            print(f"ERROR: SUBCOMMAND ({sys.argv[1]}) CANNOT BE FOUND\n\n{usage}")

if __name__ == '__main__':
    main()
