from collections import deque

from pprint import pprint as p
import sys

type Pos = tuple[int, int]
type Manifold = list[list[str]]
type Beams = list[Pos] 

def find_start(manifold: Manifold) -> Pos:
    for y, el in enumerate(manifold[0]):
        if el == 'S':
            return 0, y
    raise RuntimeError

def tachyon_travel(manifold: Manifold, start: Pos, H: int):
    H, W = len(manifold), len(manifold[0])
    dist: int = 0
    split: int = 0

    beams_head: deque[Pos] = deque([start])
    beam_present: set[Pos] = {start}

    while beams_head:
        x, y = beams_head.popleft()
        if x == H - 1: continue

        if (0 <= x + 1 < H) and manifold[x + 1][y] != '^':
            beam_present.add((x, y))
            beams_head.append((x + 1, y))
            manifold[x + 1][y] = '|'
        else:
            if (0 <= y - 1 < W) and ((x + 1, y - 1) not in beam_present):
                inc_split = True
                beam_present.add((x + 1, y - 1))
                beams_head.append((x + 1, y - 1))
                manifold[x + 1][y - 1] = '|'
            if (0 <= y + 1 < W) and ((x + 1, y + 1) not in beam_present):
                inc_split = True
                beam_present.add((x + 1, y + 1))
                beams_head.append((x + 1, y + 1))
                manifold[x + 1][y + 1] = '|'
            if inc_split: split += 1; inc_split = False

        #p(manifold)
        #print('\n')
        dist += 1

    return split

def part1(data: list[str]) -> int:
    H = len(data)
    #p(manifold := [[char for char in line] for line in manifold])
    manifold: Manifold = [[char for char in line] for line in data]
    start = find_start(manifold)
    return tachyon_travel(manifold, start, H)

def part2():
    pass

if __name__ == '__main__':
    manifold: list[str] = sys.stdin.read().splitlines()
    print(f'We split {part1(manifold)} times')
    #print(f'We split {part2(manifold)} times')
