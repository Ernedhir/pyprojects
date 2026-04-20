import subprocess
import sys

sep = 'https://'
i = 0
output = ''

for p in sys.argv[1].split(sep):
    if p:
        i += 1
        output += sep + p + '\n'

print(i)
subprocess.run('clip', input=output, text=True)
