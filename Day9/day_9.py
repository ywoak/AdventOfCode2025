from pprint import pprint as p
from ipdb import set_trace
import sys

type Coord = tuple[int, ...]
type Coords = list[Coord]
type Map = list[list[str]]

def print_map(map: Map) -> None:
    for row in map:
        print("".join(row))

def draw_rectangle(map, largest):
    (x1, y1), (x2, y2)= largest['rectangle']

    for j in range(min(x2, x1), max(x2, x1) + 1):
        for i in range(min(y2, y1), max(y2, y1) + 1):
            map[i][j] = 'O'

    print_map(map)

def find_largest(to_check, coords):
    largest = {'area': 0, 'rectangle': [(0, 0), (0, 0)]}

    for coord in coords:
        if coord == to_check: continue
        x = abs(to_check[1] - coord[1]) + 1
        y = abs(to_check[0] - coord[0]) + 1
        area = x * y
        if area > largest['area']:
            largest['area'] = area
            largest['rectangle'] = (coord, to_check)
    return largest

def part1(coords: Coords, map: Map) -> dict:
    largest: dict = {'area': 0, 'rectangle': [(0, 0), (0, 0)]}

    for coord in coords:
        res = find_largest(coord, coords)
        if res['area'] > largest['area']:
            largest = res
    #draw_rectangle(map, largest)
    return largest

def part2(coords) -> int:
    return 0

def format_input(coords: Coords):
    print(coords)
    f = []

    curr = []
    last_x = coords[0][0] # Initial var
    for x, y in coords:
        if x == last_x:
            curr.append((x, y))
        else:
            f.append(curr)
            curr = []
            last_x = x
            curr.append((x, y))

    f.append(curr)
    return f

#set_trace(context=5)
if __name__ == '__main__':
    data: list[str] = sys.stdin.read().splitlines()
    #data: list[str] = open('test_9.txt').read().splitlines()
    coords: Coords = [tuple(map(int, (coord for coord in line.split(',')))) for line in data]
    swap_coords: Coords = [(y, x) for x, y in coords]
    map: Map = [['.' for c in range(14)] for _ in range(9)]
    #for y, x in coords: map[x][y] = '#'
#    part_1: dict = part1(coords, map)
#    print(f'The largest area possible is: {part_1['area']}\nFor the two coords: {part_1['rectangle']}')
    f = format_input(sorted(swap_coords))
    print(f)
    print_map(map)
    print(f'part2 result is {part2(f)}')
