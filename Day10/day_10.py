from pprint import pprint as p
import re
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

type Goal = list[bool]
type Button = list[int]
type Buttons = list[Button]
type Formatted = tuple[Goal, Buttons]

@debug
def format_machine(machine: str) -> Formatted:
    goal = [True if char == '#' else False for char in re.findall(r'\[([.#]+)\]', machine.strip())[0]]
    print(goal)
    buttons = [
        [int(n) for n in group.split(',')]
        for group in re.findall(r'\((\S+)\)', machine.strip())
    ]

    return (goal, buttons)

def toggle(goal: Goal, button: Button) -> Goal:
    for pos in button:
        goal[pos] = not goal[pos]
    return goal

def find_fewer(goal: Goal, buttons: Buttons) -> int:
    fewer = 0
    to_find = goal[:]

    # Doesnt work, sometimes we dont click
    for i, current_button in enumerate(buttons):
        print(f'\nWe change button to try with {current_button}')
        test = buttons[i + 1:]
        goal = toggle(goal, current_button)
        for button in test:
            print(f'curr: {button}')
            print(f'goal before toggle: {goal}')
            goal = toggle(goal, button)
            print(f'goal after toggle: {goal}')
            if to_find == goal: print('YEEES')
    return 0

# We assume the input is correct
def part1(map: list[str]) -> int:
    fewer = 0
    for machine in machines:
        goal, buttons = format_machine(machine)
        fewer += find_fewer(goal, buttons)
    return fewer

#set_trace(context=5)

# [] -> light diagram           # . means off, # means on, c'est montre en goal mais de base ils sont tous off
# () -> button wiring           # toggle the lights in the button, on if off and off if on
# {} -> joltage requirements    #
# return the fewest total press required
if __name__ == '__main__':
    #machines: list[str] = sys.stdin.read().splitlines()
    machines: list[str] = open('test_10_min.txt').read().splitlines()
    #data = format_input(machines)
    print(f'Part 1 result is: {part1(machines)}\n')
#    print_map(map)
#    print(f'part2 result is {part2(f)}')
