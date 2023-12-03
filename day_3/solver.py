import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

result = 0
table = []
parts = []

for y, l in enumerate(lines):
    in_number = False
    number = ""
    for x, ch in enumerate(l):
        if ch.isdigit() and not in_number:
            number = ch
            in_number = True
        elif ch.isdigit():
            number += ch
        elif ch == "." and in_number:
            in_number = False
            parts.append((number,y, (x - len(number), x - 1)))
        elif in_number:
            in_number = False
            parts.append((number,y, (x - len(number), x - 1)))
    if in_number:
        in_number = False
        parts.append((number, y, (len(l) - len(number), len(l) - 1)))

print(parts)

valid = []

for v in parts:
    n, y, (xl, xh) = v
    ignore = set(range(xl, xh+1))
    for y1 in range(y-1, y +2):
        for x1 in range(xl-1, xh +2):
            if x1 < 0 or x1 >= len(lines[0]):
                continue
            if y1 < 0 or y1 >= len(lines):
                continue
            # print(lines[y1][x1], y, x)
            if lines[y1][x1] == ".":
                continue
            if y1 == y and x1 in ignore:
                # print("ignored")
                continue
            # if lines[y1][x1].isdigit():
            #     continue
            valid.append(n)
    # input()

print(valid)
result = 0

for v in valid:
    result += int(v)




# Part 1 = 
print(f"answer = {result}")

result = 0

# Part 2 = 
print(f"answer = {result}")
