banks = [line.strip() for line in open(0)]

def find_first_max(bank, length):
    result = {'max': 0, 'pos': 0}
    for i in range(length - 1):
        voltage = int(bank[i])
        if (voltage > result['max']):
            result['max'] = voltage
            result['pos'] = i
    return result

def find_second_max(bank, pos, length):
    result = {'max': 0, 'pos': 0}
    for i in range(pos + 1, length):
        voltage = int(bank[i])
        if (voltage > result['max']): 
            result['max'] = voltage
            result['pos'] = i
    return result

def part1():
    global banks
    output = 0
    for bank in banks:
        length_bank = len(bank)
        first_max = find_first_max(bank, length_bank)
        second_max = find_second_max(bank, first_max['pos'], length_bank)
        res = str(first_max['max']) + str(second_max['max'])
        output += int(res)
    print(output)

def add_in_result(result, max):
    for i in range(12):
        if result[i] == 0:
            result[i] = max
            return result
    return result

def find_max(bank_to_slice):
    res = {'max': 0, 'pos': 0}
    for i in range(len(bank_to_slice)):
        if int(bank_to_slice[i]) > res['max']:
            res['max'] = int(bank_to_slice[i])
            res['pos'] = i
    return res

def find_next_max(bank, current_idx, length_bank, remainer_to_skip):
    end = length_bank if length_bank - current_idx <= remainer_to_skip else current_idx + remainer_to_skip + 1
    bank_to_slice = bank[current_idx:end]
    next_max = find_max(bank_to_slice)
    return next_max

def part2():
    res = 0
    global banks
    for bank in banks:
        result: list[int] = [0 for _ in range(12)]
        length_bank = len(bank)
        last_max_pos = 0
        remainer_to_skip = length_bank - 12
        while 0 in result:
            max_obj = find_next_max(bank, last_max_pos, length_bank, remainer_to_skip)
            add_in_result(result, max_obj['max'])
            last_max_pos += max_obj['pos'] + 1
            remainer_to_skip -= max_obj['pos']
        voltage = ''.join(map(str, result))
        res += int(voltage)
    print(res)

if __name__ == '__main__':
    part1()
    part2()
