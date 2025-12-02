import subprocess

def test_test():
    r = subprocess.run(['python', '../Utils/aoc.py', 'test'], stdout=subprocess.PIPE)
    print(r.stdout)

def test_test2():
    subprocess.run(['python', '../Utils/aoc.py', 'test_suite'], capture_output=True)
