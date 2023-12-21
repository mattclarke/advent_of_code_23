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

def print_layout(layout):
    for r in range(len(lines)):
        line = ""
        for c in range(len(lines[0])):
            if (r,c) in layout:
                line += "O"
            else:
                line += lines[r][c]
        print(line)
    print("================")

possible = {S} 
for _ in range(25):
    # print_layout(possible)
    new_possible = set()
    for p in possible:
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r = p[0] + dr
            c = p[1] + dc
            if dr ==0 and dc == 0:
                continue
            rm = r % len(lines[0])
            cm = c % len(lines)
            if lines[rm][cm] != "#":
                new_possible.add((r,c))
    possible = new_possible
print_layout(possible)

# It forms a diamond and from the start position there are no rocks in the N, S, E, W directions
turns = 25
min_r = S[0] - turns
max_r = S[0] + turns
min_c = S[1] - turns
max_c = S[1] + turns


# count the number of positions in the diamond
result = 0
for r in range(0, turns+1):
    rr = S[0] - r
    even = True
    for c in range(-turns + r, turns + 1 - r):
        cc = S[1] + c
        # print(rr-S[0], cc-S[1])
        if lines[rr][cc] != "#" and even:
            result += 1
        even = not even

for r in range(1, turns+1):
    rr = S[0] + r
    even = True
    for c in range(-turns + r, turns + 1 - r):
        cc = S[1] + c
        # print(rr-S[0], cc-S[1])
        if lines[rr][cc] != "#" and even:
            result += 1
        even = not even

print("result", result)

# Part 2 = 
print(f"answer = {len(possible)}")
