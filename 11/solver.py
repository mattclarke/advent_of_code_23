import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]


empty_rows = []
for r, line in enumerate(lines):
    if "#" not in line:
        empty_rows.append(1)
    else:
        empty_rows.append(0)

count = 1
empty_cols = []
seen = set()
G = {}

for y in range(len(lines[0])):
    for x in range(len(lines[0])):
        col_empty = True
        for r in range(len(lines)):
            if lines[r][x] == "#":
                col_empty = False
        if col_empty and x not in seen:
            seen.add(x)
            empty_cols.append(1)
        elif x not in seen:
            seen.add(x)
            empty_cols.append(0)
        if lines[y][x] == "#":
            G[count] = (y, x)
            count += 1


def solve(G, empty_rows, empty_cols, scale=2):
    result = 0
    scale = scale - 1

    for k1, v1 in G.items():
        for k2, v2 in G.items():
            if k1 == k2:
                continue
            cols_jumped = 0
            if v1[0] < v2[0]:
                cols_jumped = sum(empty_rows[v1[0] : v2[0]])
            elif v2[0] < v1[0]:
                cols_jumped = sum(empty_rows[v2[0] : v1[0]])
            rows_jumped = 0
            if v1[1] < v2[1]:
                rows_jumped = sum(empty_cols[v1[1] : v2[1]])
            elif v2[1] < v1[1]:
                rows_jumped = sum(empty_cols[v2[1] : v1[1]])

            dist = abs(v1[0] - v2[0]) + abs(v1[1] - v2[1])
            dist += cols_jumped * scale + rows_jumped * scale
            result += dist
    # Double counting
    return result // 2


result = solve(G, empty_rows, empty_cols)

# Part 1 = 10228230
print(f"answer = {result}")

result = solve(G, empty_rows, empty_cols, 1000000)

# Part 2 = 447073334102
print(f"answer = {result}")
