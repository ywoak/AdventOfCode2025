import sys

type Problem = tuple[str]
type Problems = list[Problem]

def get_data(data: str) -> Problems:
    return list(zip(*[[num for num in lines.split(' ') if num] for lines in data.split('\n')]))

def format_expression(problem: Problem):
    return problem[-1].join(problem[:-1])

def part1(data: str):
    problems: Problems =  get_data(data)

    return sum(map(eval, map(format_expression, problems)))

if __name__ == '__main__':
    data = sys.stdin.read().strip()
    print(f'Part 1 solution is {part1(data)}')
