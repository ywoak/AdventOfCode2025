import sys

def part1(ranges: str, ids: str) -> int:
    return sum(
        [
            1
            for id in ids.split('\n')
            if any(
                [
                    int(id) in range(*[
                            elem + 1 if idx == 1 else elem
                            for idx, elem in enumerate(map(int,_range.split('-')))
                        ]
                    )
                    for _range in ranges.split('\n')
                 ]
            )
        ]
    )
    
def create_merge(start_m: int, end_m: int, start: int, end: int) -> list[int]:
    low: int = start if start < start_m else start_m
    high: int = end if end > end_m else end_m
    return [low, high]

def overlap(start_m: int, end_m: int, start: int, end: int) -> bool:
    return (start_m <= start <= end_m) or (start_m <= end <= end_m) or (start <= start_m <= end) or (start <= end_m <= end)

def update_merged(merged) -> list[tuple[int, int]]:
    for comparee, (start_merge, end_merge) in enumerate(merged):
        for compared, (start_remainer, end_remainer) in enumerate(merged[comparee + 1:]):
            if (overlap(start_merge, end_merge, start_remainer, end_remainer)):
                new_merge = create_merge(start_merge, end_merge, start_remainer, end_remainer)
                del merged[comparee]
                del merged[comparee + compared]
                merged.append(new_merge)
                update_merged(merged)
                return merged
    return merged

def part2(ranges: str) -> int:
    merged: list[tuple[int, int]] = []
    for _range in ranges.split('\n'):
        overlapped = False
        splitrange: list[int] = list(map(int, _range.split('-')))
        start, end = splitrange
        for i, (start_m, end_m) in enumerate(merged):
            if overlap(start_m, end_m, start, end):
                new_start, new_end = create_merge(start_m, end_m, start, end)
                del merged[i]
                merged.append((new_start, new_end))
                merged = update_merged(merged)
                overlapped = True
        if not overlapped:
            merged.append((start, end))

    acc = 0
    for merge in merged:
        acc += int(merge[1]) + 1 - int(merge[0])
    return acc

if __name__ == '__main__':
    data: list[str] = sys.stdin.read().strip().split('\n\n')
    ranges, ids = data[0], data[1]

    print(f'The number of fresh ingredient is {part1(ranges, ids)}')
    print(f'The number of fresh ingredient possible is {part2(ranges)}')
