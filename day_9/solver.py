import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]
lines = [[int(x) for x in line.split(" ")] for line in lines]   


def solve(line):
    last = [line[~0]]
    diff = []
    while True:
        for i in range(0, len(line) -1):
            diff.append(line[i+1] - line[i])
        if diff.count(diff[0]) == len(diff):
            break
        line = diff
        diff = []
        last.append(line[~0])
    diff = diff[0]
    while last:
        curr = last.pop(-1)
        diff += curr
    return diff


result = 0

for l in lines:
    result += solve(l)


# Part 1 = 
print(f"answer = {result}")

def solve(line):
    last = [line[~0]]
    diff = []
    while True:
        for i in range(0, len(line) -1):
            diff.append(line[i+1] - line[i])
        if diff.count(diff[0]) == len(diff):
            break
        line = diff
        diff = []
        last.append(line[~0])
    diff = diff[0]
    while last:
        curr = last.pop(-1)
        diff += curr
    return diff

result = 0

# Part 2 = 
print(f"answer = {result}")
