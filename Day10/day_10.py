from pprint import pprint as p
from ipdb import set_trace
import sys

type Pos = tuple[int, int]
type Positions = list[Pos]
type Coord = tuple[int, ...]
type Coords = list[Coord]
type Map = list[list[str]]

def print_map(map: Map) -> None:
    for row in map:
        print("".join(row))

def f() -> None:
    pass

def part1(map: Map) -> int:
    return 0

def format_input(data):#: Map):
    formatted = []

    return formatted

#set_trace(context=5)
if __name__ == '__main__':
    input: list[str] = sys.stdin.read().splitlines()
    #input: list[str] = open('test_10.txt').read().splitlines()
    data = format_input(input)
    print(f'Part 1 result is: {part1(data)}\n')
#    print_map(map)
#    print(f'part2 result is {part2(f)}')
