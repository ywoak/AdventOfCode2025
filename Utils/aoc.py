import subprocess
import os
import re

caller_location = os.path.dirname('.')
caller_path = os.path.abspath(caller_location)

match = re.search('Day+[0-9]', caller_path)
if not match:
    print('Big issue ! We\'re not in an AdventOfCode Day directory ... ')
    exit()

i = match.start() + 3
day = caller_path[i:]
print(f'day is {day}') 

if __name__ == '__main__':
    subprocess.run(['python', f'day_{day}.py'], stdin=open(f'input_{day}.txt'))
