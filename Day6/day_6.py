import sys

type Problem = tuple[str]
type Problems = list[Problem]
#type Cephalopod_Problems = list[list[list[Problem]]]
type Cephalopod_Problems = list

def is_not_empty(elem):
    empty = True
    for e in elem:
        if e.strip():
            empty = False
            break
    return not empty

def get_cephalopod_data(data: str) -> Cephalopod_Problems:
    a = list(map(list, zip(*[line for line in data.split('\n') if line])))

    res = []
    one_problem = []

    length = len(a)
    for i, elem in enumerate(a):
        if is_not_empty(elem):
            one_problem.append(elem)
            if i == length - 1:
                res.append(one_problem)
        elif one_problem:
            res.append(one_problem)
            one_problem = []

    return res

def format_cephalopod_expression(cephalopod_data):
    sign = cephalopod_data[0].pop()

    res = []
    for operand_to_parse in cephalopod_data:
        s = ''
        for elem in operand_to_parse:
            if elem.strip():
                s += elem
        res.append(s)

    to_ret = sign.join(res)
    return to_ret

def get_data(data: str) -> Problems:
    return list(zip(*[[num for num in lines.split(' ') if num] for lines in data.split('\n')]))

def format_expression(problem: Problem):
    return problem[-1].join(problem[:-1])

def part1(data: str):
    problems: Problems =  get_data(data)
    return sum(map(eval, map(format_expression, problems)))

def part2(data: str):
    cephalopod_data: Cephalopod_Problems = get_cephalopod_data(data)
    return sum(map(eval, map(format_cephalopod_expression, cephalopod_data)))

if __name__ == '__main__':
    data = sys.stdin.read()
    print(f'Part 1 solution is {part1(data.strip())}')
    print(f'Part 2 solution is {part2(data)}')
