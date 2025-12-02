import sys
import math

pos: int = 50
password: int = 0
distance: int = 0

for line in sys.stdin.readlines():
    distance = int(line[1:])
    with_mod = 0
    start_with_zero: bool = pos == 0
    if line[0] == 'L':
        pos -= distance
        if (pos == 0):
            password += 1
        elif (start_with_zero):
            if distance > 99:
                how_much = math.trunc(abs(pos / 100))
                if pos % 100 == 0:
                    how_much += 1
                password += how_much
        elif (with_mod != pos):
            how_much = abs(pos // 100)
            if pos % 100 == 0:
                how_much += 1
            password += how_much
        pos = pos % 100
    else:
        pos += distance
        if (pos == 0):
            password += 1
        with_mod = pos % 100
        we_move = (start_with_zero and distance > 99) or not start_with_zero
        if (pos != with_mod and we_move):
            how_much = abs(pos // 100)
            password += how_much
        pos = pos % 100

print(f'password is {password}')
