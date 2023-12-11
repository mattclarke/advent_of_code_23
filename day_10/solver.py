import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

layout = {}
S = None
for r, l in enumerate(lines):
    for c, ch in enumerate(l):
        if ch == "S":
            S = (r, c)
        layout[(r,c)] = ch
print(S)



def find_exits(layout, loc):
    r, c = loc
    curr = layout[loc]
    exits = []
    if curr == "S":
        if layout.get((r-1,c)) in ["|", "7", "F"]:
            exits.append((r-1, c))
        if layout.get((r+1,c)) in ["|", "J", "L"]:
            exits.append((r+1, c))
        if layout.get((r,c-1)) in ["-", "F", "L"]:
            exits.append((r, c-1))
        if layout.get((r,c+1)) in ["-", "J", "7"]:
            exits.append((r, c+1))
    elif curr == "-":
        exits = [(r, c-1), (r, c+1)]
    elif curr == "|":
        exits = [(r-1, c), (r+1, c)]
    elif curr == "L":
        exits = [(r-1, c), (r, c+1)]
    elif curr == "J":
        exits = [(r-1, c), (r, c-1)]
    elif curr == "7":
        exits = [(r+1, c), (r, c-1)]
    elif curr == "F":
        exits = [(r+1, c), (r, c+1)]
    else:
        assert False, "D'oh!"

    assert len(exits) == 2, "Ooops"
    return exits


seen = {S: 0
        }

curr_1, curr_2 = find_exits(layout, S)
seen[curr_1] = 1
seen[curr_2] = 1

steps = 2

while True:
    moving = False
    exits = find_exits(layout, curr_1)
    for ex in exits:
        if ex in seen:
            continue
        moving = True
        curr_1 = ex
        seen[curr_1] = steps

    exits = find_exits(layout, curr_2)
    for ex in exits:
        if ex in seen:
            continue
        moving = True
        curr_2 = ex
        seen[curr_2] = steps
    if not moving:
        break
    steps += 1

result = steps-1

# for r in range(10):
#     row = []
#     for c in range(10):
#         if (r,c) in seen:
#             row.append(seen[(r,c)])
#         else:
#             row.append(layout.get((r,c), '.'))
#     print(row)
#         


# Part 1 = 6649
print(f"answer = {result}")

result = 0

# Part 2 = 
print(f"answer = {result}")
