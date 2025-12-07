from collections import deque

from IPython import embed
import pdb

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

def tachyon_travel(manifold: Manifold, start: Pos):
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

def part1(manifold: Manifold) -> int:
    #p(manifold := [[char for char in line] for line in manifold])
    start = find_start(manifold)
    return tachyon_travel(manifold, start)

def in_bound(H: int, W: int, x: int, y: int) -> bool:
    return 0 <= x < H and 0 <= y < W

def quantum_tachyon_travel(
    manifold: list[list[str]],
    current_pos: tuple[int, int],
    H: int,
    W: int,
    beam_present: set[tuple[int, int]],
    paths: int
) -> int:

    x, y = current_pos

    # Sort de l’espace : on termine un chemin
    if not in_bound(H, W, x, y):
        return paths + 1

    # Boucle : on ne revisite pas un nœud déjà pris dans ce faisceau
    if (x, y) in beam_present:
        return paths

    # Nouvel ensemble pour éviter la mutation globale
    new_beam = beam_present | {(x, y)}

    # Si c’est un split '^'
    if manifold[x][y] == '^':
        for dy in [-1, +1]:
            ny = y + dy
            paths = quantum_tachyon_travel(
                manifold, (x, ny), H, W, new_beam, paths
            )

    # Sinon on descend
    else:
        manifold[x][y] = '|'
        paths = quantum_tachyon_travel(
            manifold, (x + 1, y), H, W, new_beam, paths
        )

    return paths

def part2(manifold: Manifold) -> int:
    start = find_start(manifold)
    paths: int = quantum_tachyon_travel(manifold, start, len(manifold), len(manifold[0]), set(), paths=0)
    return paths

if __name__ == '__main__':
    data: list[str] = sys.stdin.read().splitlines()
    manifold: Manifold = [[char for char in line] for line in data]
    print(f'We split {part1(manifold)} times')
    print(f'There is {part2(manifold)} path')
