import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]
lines = [[x for x in line] for line in lines]

S= None
for r, row in enumerate(lines):
    for c, ch in enumerate(row):
        if ch == "S":
            S = (r, c)
            break
    if S:
        break
lines[S[0]][S[1]] = "."


possible = {S} 
for _ in range(64):
    new_possible = set()
    for p in possible:
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r = p[0] + dr
            c = p[1] + dc
            if dr ==0 and dc == 0:
                continue
            if r <0 or r >= len(lines):
                continue
            if c <0 or c >= len(lines[0]):
                continue
            if lines[r][c] != "#":
                new_possible.add((r,c))
    possible = new_possible


# Part 1 = 3858
print(f"answer = {len(possible)}")

result = 0

# Part 2 = 
print(f"answer = {result}")
