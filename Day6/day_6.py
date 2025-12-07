import sys

type Cephalopod_Problem = list[list[str]]
type Cephalopod_Problems = list[Cephalopod_Problem]
type Problem = tuple[str]
type Problems = list[Problem]

def is_not_empty(elem: list[str]) -> bool:
    empty: bool = True
    e: str
    for e in elem:
        if e.strip():
            empty = False
            return not empty
    return not empty

def get_cephalopod_data(data: str) -> Cephalopod_Problems:
    initial_zip: list[list[str]] = list(map(list, zip(*[line for line in data.split('\n') if line])))

    res: Cephalopod_Problems = []
    one_problem: Cephalopod_Problem = []

    length = len(initial_zip)
    for i, elem in enumerate(initial_zip):
        if is_not_empty(elem):
            one_problem.append(elem)
            if i == length - 1:
                res.append(one_problem)
        elif one_problem:
            res.append(one_problem)
            one_problem = []

    return res

def format_cephalopod_expression(cephalopod_data: Cephalopod_Problem) -> str :
    sign: str = cephalopod_data[0].pop()

    res: list[str] = []
    operand_to_parse: list[str]
    for operand_to_parse in cephalopod_data:
        s: str = ''
        elem: str
        for elem in operand_to_parse:
            if elem.strip():
                s += elem
        res.append(s)

    to_ret: str = sign.join(res)
    return to_ret

def get_data(data: str) -> Problems:
    return list(zip(*[[num for num in lines.split(' ') if num] for lines in data.split('\n')]))

def format_expression(problem: Problem):
    return problem[-1].join(problem[:-1])

def part1(data: str) -> int:
    problems: Problems =  get_data(data)
    return sum(map(eval, map(format_expression, problems)))

def part2(data: str) -> int:
    cephalopod_data: Cephalopod_Problems = get_cephalopod_data(data)
    return sum(map(eval, map(format_cephalopod_expression, cephalopod_data)))

if __name__ == '__main__':
    data: str = sys.stdin.read()
    print(f'Part 1 solution is {part1(data.strip())}')
    print(f'Part 2 solution is {part2(data)}')
