from pprint import pprint as p
from ipdb import set_trace
import sys

type Pos = tuple[int, int]
type Positions = list[Pos]
type Coord = tuple[int, ...]
type Coords = list[Coord]
type Map = list[list[str]]

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with: ")
        p(args)
        if kwargs: p(kwargs)
        result = func(*args, **kwargs)
        print(f"Function format {func.__name__} returned: {result}\n")
        return result
    return wrapper

@debug
def print_map(map: Map) -> None:
    for row in map:
        print("".join(row))

def f() -> None:
    pass

def part1(map: Map) -> int:
    return 0

@debug
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
