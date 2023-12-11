import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

new_lines = []
for line in lines:
    if "#" in line:
        new_lines.append(line)
    else:
        new_lines.append(line)
        new_lines.append(line)

count = 1
lines2 = []
G = {}
for y in range(len(new_lines)):
    line = []
    for x in range(len(new_lines[0])):
        col_empty = True
        for r in range(len(new_lines)):
            if new_lines[r][x] == "#":
                col_empty = False
        if col_empty:
            line.append(".")
        if new_lines[y][x] == "#":
            G[count] = (y, len(line))
            line.append(count)
            count += 1
        else:
            line.append(".")
    lines2.append(line)




result = 0

# for l in lines2:
#     print(l)
#     pass
#
# print(G)

for k1,v1 in G.items():
    for k2,v2 in G.items():
        if k1 == k2:
            continue
        dist = abs(v1[0] - v2[0]) + abs(v1[1] - v2[1])
        print(dist)
        result += dist


# Part 1 = 10228230
print(f"answer = {result//2}")

result = 0

# Part 2 = 
print(f"answer = {result}")
