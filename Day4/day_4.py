import sys
import pprint

type Directions = list[tuple[int, int]]
type Positions = list[tuple[int, int]]

def is_in_bound(row: int, col: int, row_length: int, col_length: int) -> bool:
    return True if ((row >= 0) and (row < row_length) and (col >= 0) and (col < col_length)) else False

def find_adjacent_rolls(lines: list[str], row_index: int, col_index: int) -> int:
    directions: Directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    adjacent_rolls: int = 0

    for row_offset, col_offset in directions:
        row_length: int = len(lines)
        col_length: int = len(lines[0])
        row: int = row_index + row_offset
        col: int = col_index + col_offset
        adjacent_rolls += 1 if (is_in_bound(row, col, row_length, col_length) and lines[row][col] == '@') else False
    return adjacent_rolls

def part1(lines: list[str]) -> int:
    forklitable: int = 0

    for row, line in enumerate(lines):
        for col, box in enumerate(line):
            if box == '@':
                adjacent_roll: int = find_adjacent_rolls(lines, row, col)
                forklitable += 1 if adjacent_roll < 4 else False
    return forklitable

def update_grid(lines: list[str], pos_to_remove: Positions) -> list[str]:
    for row, col in pos_to_remove:
        # Creating a new var to change a char in line[row] because str is immutable
        lines[row] = lines[row][:col] + '.' + lines[row][col + 1:]
    
    return lines

def part2(lines: list[str]) -> int:
    removable_rolls: int = 0
    something_to_remove: bool = True
    pos_to_remove: Positions = []

    turn = 0
    while something_to_remove:
        something_to_remove = False
        pprint.pprint(lines); print(f'turn is {turn}\n')
        for row, line in enumerate(lines):
            for col, _ in filter(lambda box : box[1] == '@', enumerate(line)): # box[1] because lambda doesnt accept
                adjacent_roll: int = find_adjacent_rolls(lines, row, col)
                if adjacent_roll < 4:
                    removable_rolls += 1 
                    something_to_remove = True
                    pos_to_remove.append((row, col))

        lines = update_grid(lines, pos_to_remove)
        pos_to_remove: Positions = []
        turn += 1

    return removable_rolls

if __name__ == '__main__':
    lines: list[str] = sys.stdin.read().strip().splitlines()
    print(f'The number of forklitable rolls of paper is {part1(lines)}')
    print(f'The number of cumulative removal rolls of paper is {part2(lines)}')
