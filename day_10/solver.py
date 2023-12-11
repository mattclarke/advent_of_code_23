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


curr, _ = find_exits(layout, S)
seen = {S, curr}
dots = {}
direction = (curr[0] - S[0], curr[1] - S[1])
print(direction)

while True:
    for r in range(10):
        row = []
        for c in range(10):
            if (r,c) in seen:
                row.append("$")
            else:
                row.append(layout.get((r,c), '.'))
        print(row)
    print()
    input()
    moving = False
    ch = layout[curr]
    print(ch, curr, direction)
    if ch == "|" and direction[0] == 1:
        # going down
        pass
    elif ch == "|" and direction[0] == -1:
        # going up
        pass
    elif ch == "-" and direction[1] == 1:
        # going right
        direction = (0, 1)
        pass
    elif ch == "-" and direction[1] == -1:
        # going left
        direction = (0, -1)
        pass
    elif ch == "L" and direction[0] == 1:
        # going right
        direction = (0, 1)
        pass
    elif ch == "L" and direction[1] == -1:
        # going up
        direction = (-1, 0)
        pass
    elif ch == "J" and direction[0] == 1:
        # going left
        direction = (0, -1)
        pass
    elif ch == "J" and direction[1] == 1:
        # going up
        direction = (-1, 0)
        pass
    elif ch == "7" and direction[0] == -1:
        # going left
        direction = (0, -1)
        pass
    elif ch == "7" and direction[1] == 1:
        # going down
        direction = (1, 0)
        pass
    elif ch == "F" and direction[1] == -1:
        # going down
        direction = (1, 0)
        pass
    elif ch == "F" and direction[0] == -1:
        # going right
        direction = (0, 1)
        pass
    else:
        assert False, "oops"
    exits = find_exits(layout, curr)
    for ex in exits:
        if ex in seen:
            continue
        moving = True
        curr = ex
        seen.add(curr)





#
# water = set()
#
# # Surround layout with water
# for r in range(-1, len(lines)+ 1):
#     if r == -1:
#         for c in range(-1, len(lines[0])+1):
#             water.add((r,c))
#     elif r == len(lines):
#         for c in range(-1, len(lines[0])+1):
#             water.add((r,c))
#     else:
#         water.add((r,-1))
#         water.add((r,len(lines[0])))
#
# # Coarse fill
# while True:
#     to_add = set()
#     for w in water:
#         for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             cc = w[1] + dc
#             rr = w[0] + dr
#             if (rr, cc) in layout:
#                 if layout[(rr, cc)] == "." and (rr, cc) not in water:
#                     to_add.add((rr, cc))
#     if not to_add:
#         break
#     water= water.union(to_add)
#
# visited = set()
# while True:
#     to_add = set()
#     for w in water:
#         for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             cc = w[1] + dc
#             rr = w[0] + dr
#             if (rr, cc) in layout:
#                 while layout[(rr,cc)] != "." and (rr, cc) not in visited:
#                     print("hello")
#                     while (rr, cc) not in visited:
#                         ch = layout[(rr,cc)]
#                         if ch == "-":
#                             if w[0] > rr:
#                                 # Left is clockwise
#                                 visited.add((rr, cc))
#                                 if (rr + 1, cc) in layout and layout[rr + 1, cc] == ".":
#                                     to_add.add((rr+1, cc))
#                                 cc -= 1
#                             else:
#                                 # Right is clockwise
#                                 visited.add((rr, cc))
#                                 if (rr - 1, cc) in layout and layout[rr - 1, cc] == ".":
#                                     to_add.add((rr-1, cc))
#                                 cc += 1
#                         elif ch == "|":
#                             if w[1] > cc:
#                                 # down is clockwise
#                                 visited.add((rr, cc))
#                                 if (rr, cc+1) in layout and layout[rr, cc+1] == ".":
#                                     to_add.add((rr, cc+1))
#                                 rr -= 1
#                             else:
#                                 # up is clockwise
#                                 visited.add((rr, cc))
#                                 if (rr, cc-1) in layout and layout[rr, cc-1] == ".":
#                                     to_add.add((rr, cc-1))
#                                 rr += 1
#                         elif ch == "L":
#                                 visited.add((rr, cc))
#                                 if (rr, cc-1) in layout and layout[rr, cc-1] == ".":
#                                     to_add.add((rr, cc-1))
#                                 if (rr+1, cc) in layout and layout[rr+1, cc] == ".":
#                                     to_add.add((rr+1, cc))
#                                 rr -= 1
#                         else:
#                             break
#
#
#
#
#
#
#                         for r in range(-1, 10):
#                             row = []
#                             for c in range(-1, 10):
#                                 if (r, c) == (rr, cc):
#                                     row.append("$")
#                                 elif (r,c) in water:
#                                     row.append("O")
#                                 else:
#                                     row.append(layout.get((r,c), '.'))
#                             print(row)
#                         print("")
#         
#                         input()
#

result = 0

# Part 2 = 
print(f"answer = {result}")
