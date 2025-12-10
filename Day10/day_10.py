from pprint import pprint as p
from itertools import product
from ipdb import set_trace
#set_trace(context=5)

import sys
import re

type Map = list[list[str]]
type Goal = list[bool]
type Button = list[int]
type Buttons = list[Button]
type Formatted = tuple[Goal, Buttons]

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with: ")
        p(args)
        if kwargs: p(kwargs)
        result = func(*args, **kwargs)
        print(f"Function format {func.__name__} returned: {result}\n")
        return result
    return wrapper

def print_map(map: Map) -> None:
    for row in map:
        print("".join(row))

def format_machine(machine: str) -> Formatted:
    goal = [True if char == '#' else False for char in re.findall(r'\[([.#]+)\]', machine.strip())[0]]
    buttons = [
        [int(n) for n in group.split(',')]
        for group in re.findall(r'\((\S+)\)', machine.strip())
    ]

    return (goal, buttons)

def toggle(goal: Goal, button) -> Goal:
    for pos in button:
        goal[pos] = not goal[pos]
    return goal

def find_fewer(goal: Goal, buttons: Buttons) -> int:
    L = [0, 1]

    combinations: list[tuple[int, ...]]= []

    for combination in product(L, repeat=len(buttons)):
        a_goal = [False for _ in goal]
        for i, e in enumerate(combination):
            if e == True:
                a_goal = toggle(a_goal, buttons[i])
        if a_goal == goal: combinations.append(combination)

    return(min([combination.count(1) for combination in combinations]))

def part1(machines: list[str]) -> int:
    fewer = 0
    for machine in machines:
        goal, buttons = format_machine(machine)
        fewer += find_fewer(goal, buttons)
    return fewer

if __name__ == '__main__':
    machines: list[str] = sys.stdin.read().splitlines()
    print(f'Part 1 result is: {part1(machines)}')
