import sys

invalid_ids: int = 0

def part1():
    for line in sys.stdin.readlines():
        ranges: list[str] = line.split(',')
        for range_ in ranges:
            ids = range_.split('-')
            if len(ids) < 2:
                break
            for id in range(int(ids[0]), int(ids[1]) + 1):
                id = str(id)
                length = len(id)
                i, j = 0, length // 2
                if length % 2 != 0:
                    continue
                while j < length and id[i] == id[j]:
                    i += 1
                    j += 1
                if j >= length:
                    invalid_ids += int(id)
                    #print(f'invalid is now on {id} !')
    print(f'invalid is {invalid_ids} !')

def part2(invalid_ids: int):
    for line in sys.stdin.readlines():
        ranges: list[str] = line.split(',')
        for range_ in ranges:
            ids = range_.split('-')
            if len(ids) < 2:
                break
            for id in range(int(ids[0]), int(ids[1]) + 1):
                id = str(id)
                last_start = to_reach = i = j = 0
                length = len(id)
                while i < length:
                    j = i + 1
                    if j == length:
                        break
                    elif id[j] == id[i]:
                        invalid_ids += 1
                        i += 1
                        continue
                    while j < length and id[j] != id[i]:
                        j += 1
                    if j >= length:
                        break
                    last_start = i
                    to_reach = j
                    if j - i <= length - j:
                        while (i < to_reach):
                            if id[i] == id[j]:
                                i += 1
                                j += 1
                            else:
                                i = last_start + 1
                                continue
                    i += 1
    print(f'invalid is {invalid_ids} !')

part2(invalid_ids)
