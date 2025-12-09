from collections import defaultdict
from IPython import embed
from pprint import pprint as p
import math
import sys

type Pos = tuple[int, ...]
type Coords = list[Pos]
type Circuit = defaultdict[str, Coords]

def find_smallest(a: Pos, b: Pos) -> float:
    res: float = math.sqrt(sum(((a[0] - b[0]) ** 2, (a[1] - b[1]) ** 2, (a[2] - b[2]) ** 2)))
    print(f'The straight line distance for {a} and {b} is {res}')
    return res

def _find_smallest(coord, lists):
    smallest = (0, (0))

    for coord in lists:
        for e in lists[coord+1:]:
            res = math.sqrt(sum(((e[0] - coord[0]) **2, (e[1] - coord[1]) **2, (e[2] - coord[2]) **2)))
            if smallest[0] == 0 or res < smallest[0]: smallest = (res, e)
        print(f'The smallest for {coord} is {smallest}')
    return smallest

def part1(coords):#: Coords) -> int:
    #circuit: Circuit = defaultdict()
    circuit = defaultdict(list)

    '''
    - On itere sur chaque coord de la liste quoi qu'il
    - On trouve le plus petit vis a vis des autres
    - On verifie si:
        - les deux sont deja dans un meme circuit, on fais rien
        - sinon on fusionne le circuit de l'un et le circuit de l'autre
    '''

    length = len(coords)
    i = 0 # number of turn
    while i < 10:
        i += 1
        print(f'\n\n Before the {i} turn, we have circuit:')
        p(circuit)
        print(f'\n')
        for j, coord in enumerate(coords):
            #import ipdb; ipdb.set_trace(context=10)
            _, smallest = find_smallest(coord, coords[j + 1:])

            if (smallest in circuit[coord]) or (coord in circuit[smallest]): continue#print(f'we shouldnt be here'); continue
            else:
                #print(f'\nWe should be here and circuit is {circuit}')
                circuit[coord].append(smallest)
                circuit[smallest].append(coord)

    print('\n\n')
    p(circuit)
    #lens = find_largest_lens(circuit)
    return 0

if __name__ == '__main__':
    #coords: Coords = [tuple((int(coord) for coord in line.split(','))) for line in sys.stdin.read().splitlines()]
    #coords = [tuple((int(coord) for coord in line.split(','))) for line in sys.stdin.read().splitlines()]
    #data = open('test_1.txt')
    data = open('test_8.txt')
    #data = open('input_8.txt')
    #embed()
    coords = [tuple((int(coord) for coord in line.split(','))) for line in data.read().splitlines()]
    print(f'List of coords is {coords}')
    print(f'\nThe Part 1 result is: {part1(coords)}')
