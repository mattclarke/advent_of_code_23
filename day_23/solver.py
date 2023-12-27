import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]
L = {}
for r, row in enumerate(lines):
    for c, ch in enumerate(row):
        if ch != "#":
            L[(r,c)] = ch

def pprint(layout, seen):
    for r in range(len(lines)):
        line = ""
        for c in range(len(lines[0])):
            if (r,c) in seen:
                line += "O"
            else:
                line += layout.get((r,c), "#")
        print(line)
    print("=============")

S = (0,1)
Q = [(0,1,0, {(0,1)})]
GOAL =  (len(lines)-1, len(lines[0]) -2)
result = 0

while Q:
    r,c,steps, seen = Q.pop(0)
    for dr, dc in [(-1, 0), (1,0), (0, -1), (0, 1)]:
        rr = r + dr
        cc = c + dc
        if (rr, cc) == GOAL:
            result = max(result, steps+1)
            continue
        if (rr, cc) in seen:
            continue
        ch = L.get((rr,cc), "#")
        if ch == "#":
            continue
        cseen = copy.copy(seen)
        cseen.add((rr, cc))
        if ch == ">":
            if c > cc:
                # cannot go up it
                continue
            cseen.add((rr, cc + 1))
            Q.append((rr, cc + 1, steps +2, cseen))
        elif ch == "<":
            if c < cc:
                # cannot go up it
                continue
            cseen.add((rr, cc - 1))
            Q.append((rr, cc - 1, steps +2, cseen))
        elif ch == "^":
            if r < rr:
                # cannot go up it
                continue
            cseen.add((rr-1, cc))
            Q.append((rr-1, cc, steps +2, cseen))
        elif ch == "v":
            if r > rr:
                # cannot go up it
                continue
            cseen.add((rr+1, cc))
            Q.append((rr+1, cc, steps +2, cseen))
        else:
            Q.append((rr, cc, steps +1, cseen))



# Part 1 = 2130
print(f"answer = {result}")

result = 0

# Part 2 = 
print(f"answer = {result}")
