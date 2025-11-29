import copy
import sys
from heapq import heappop, heappush


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]
L = {}
for r, row in enumerate(lines):
    for c, ch in enumerate(row):
        if ch != "#":
            L[(r, c)] = ch


def pprint(layout, seen):
    for r in range(len(lines)):
        line = ""
        for c in range(len(lines[0])):
            if (r, c) in seen:
                line += "O"
            else:
                line += layout.get((r, c), "#")
        print(line)
    print("=============")


def solve(layout):
    S = (0, 1)
    Q = [(0, 1, 0, {(0, 1)})]
    GOAL = (len(lines) - 1, len(lines[0]) - 2)
    result = 0

    while Q:
        r, c, steps, seen = Q.pop(0)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr = r + dr
            cc = c + dc
            if (rr, cc) == GOAL:
                result = max(result, steps + 1)
                continue
            if (rr, cc) in seen:
                continue
            ch = layout.get((rr, cc), "#")
            if ch == "#":
                continue
            cseen = copy.copy(seen)
            cseen.add((rr, cc))
            if ch == ">":
                if c > cc:
                    # cannot go up it
                    continue
                cseen.add((rr, cc + 1))
                Q.append((rr, cc + 1, steps + 2, cseen))
            elif ch == "<":
                if c < cc:
                    # cannot go up it
                    continue
                cseen.add((rr, cc - 1))
                Q.append((rr, cc - 1, steps + 2, cseen))
            elif ch == "^":
                if r < rr:
                    # cannot go up it
                    continue
                cseen.add((rr - 1, cc))
                Q.append((rr - 1, cc, steps + 2, cseen))
            elif ch == "v":
                if r > rr:
                    # cannot go up it
                    continue
                cseen.add((rr + 1, cc))
                Q.append((rr + 1, cc, steps + 2, cseen))
            else:
                Q.append((rr, cc, steps + 1, cseen))
    return result


# Part 1 = 2130
print(f"answer = {solve(L)}")

result = 0

# There is only a certain number of points when there is a choice of direction
choice_points = set()

for r, row in enumerate(lines):
    for c, ch in enumerate(row):
        if ch == "#":
            continue
        count = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr = r + dr
            cc = c + dc
            if L.get((rr, cc), "#") != "#":
                count += 1
        if count > 2:
            choice_points.add((r, c))

# Add the start and end to these points
choice_points.add((0, 1))
GOAL = (len(lines) - 1, len(lines[0]) - 2)
choice_points.add(GOAL)

# Calculate the distance between the points
distances = {}

for ch in choice_points:
    Q = [(ch, 0, {ch})]
    while Q:
        (r, c), steps, seen = Q.pop(0)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr = r + dr
            cc = c + dc
            if (rr, cc) in choice_points and (rr, cc) != ch:
                temp = distances.get(ch, [])
                temp.append(((rr, cc), steps + 1))
                distances[ch] = temp
                continue

            if (rr, cc) in seen:
                continue
            if L.get((rr, cc), "#") == "#":
                continue
            cseen = copy.copy(seen)
            cseen.add((rr, cc))
            Q.append(((rr, cc), steps + 1, cseen))


# BFS from the start. Cannot visit the same point twice.
result = 0
Q = [(0, (0, 1), set())]

while Q:
    steps, (r, c), seen = heappop(Q)
    cseen = copy.copy(seen)
    cseen.add((r, c))
    steps = abs(steps)
    if (r, c) == GOAL:
        result = max(steps, result)
        continue
    for pt, d in distances[(r, c)]:
        if pt in cseen:
            continue
        # Max heap works best
        heappush(Q, (-(steps + d), pt, cseen))

# Part 2 = 6710
print(f"answer = {result}")
