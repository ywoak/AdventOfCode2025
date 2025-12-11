from collections import deque
from pprint import pprint as p
from itertools import product
from ipdb import set_trace

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
        #print(set(row))
        #print("".join(row))
        print(row)

def format_input(devices):
    f = {}
    for line in devices:
        devices, output = line.split(': ')
        output = output.strip().split(' ')
        f[devices] = output

    return f

#set_trace(context=5)
def dfs(graph, start):
    q = deque([start])
    vis = set()

    paths = 0
    while q:
        node = q.popleft()
        if node in vis: continue
        if node == 'out': paths += 1; continue
        for o in graph[node]:
            q.append(o)
    return paths

#set_trace(context=5)
def dfs_2(graph, start):
    q = deque([start])
    vis = set()
    #paths = []

    #new_path = []
    paths = 0
    while q:
        node = q.popleft()
        #new_path.append(node)
        if node == 'out': vis = set(); paths += 1; continue
        for o in graph[node]:
            if o in vis: continue
            q.append(o)
            vis.add(o)
    return paths

def part1(devices: list[str]) -> int:
    f = format_input(devices)
    return dfs(f, 'you')

def part2(devices: list[str]) -> int:
    f = format_input(devices)
    paths = dfs_2(f, 'svr')
    #paths = dfs(f, 'svr')
    #print_map(paths)
    #return len(paths)
    return paths
    #p(paths)
    #return paths.__len__()

if __name__ == '__main__':
    devices: list[str] = sys.stdin.read().splitlines()
    #devices: list[str] = open('test_2.txt').read().splitlines()
    #print(f'Part 1 result is: {part1(devices)}')
    print(f'Part 2 result is: {part2(devices)}')
