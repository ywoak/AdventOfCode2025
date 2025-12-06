import sys

def part1(ranges, ids):
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
    

if __name__ == '__main__':
    data: list[str] = sys.stdin.read().strip().split('\n\n')
    ranges, ids = data[0], data[1]

    print(f'The number of fresh ingredient is {part1(ranges, ids)}')
