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
        layout[r, c] = ch


def find_exits(layout, loc):
    r, c = loc
    curr = layout[loc]
    exits = []
    if curr == "S":
        if layout.get((r - 1, c)) in ["|", "7", "F"]:
            exits.append((r - 1, c))
        if layout.get((r + 1, c)) in ["|", "J", "L"]:
            exits.append((r + 1, c))
        if layout.get((r, c - 1)) in ["-", "F", "L"]:
            exits.append((r, c - 1))
        if layout.get((r, c + 1)) in ["-", "J", "7"]:
            exits.append((r, c + 1))
    elif curr == "-":
        exits = [(r, c - 1), (r, c + 1)]
    elif curr == "|":
        exits = [(r - 1, c), (r + 1, c)]
    elif curr == "L":
        exits = [(r - 1, c), (r, c + 1)]
    elif curr == "J":
        exits = [(r - 1, c), (r, c - 1)]
    elif curr == "7":
        exits = [(r + 1, c), (r, c - 1)]
    elif curr == "F":
        exits = [(r + 1, c), (r, c + 1)]
    else:
        assert False, "D'oh!"

    assert len(exits) == 2, "Ooops"
    return exits


seen = {S: 0}
curr_1, curr_2 = find_exits(layout, S)
seen[curr_1] = 1
seen[curr_2] = 1
steps = 1
moving = True

while moving:
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
    if moving:
        steps += 1

# Part 1 = 6649
print(f"answer = {steps}")


def print_layout(layout, seen):
    for r in range(1000):
        row = []
        for c in range(1000):
            if (r, c) not in layout:
                continue
            if (r, c) in seen:
                row.append("#")
            else:
                row.append(layout.get((r, c), "."))
        if row:
            print("".join(row))
    print()


# Remove disconnected pipes to simplify part 2
for r in range(len(lines)):
    for c in range(len(lines[0])):
        if (r, c) not in seen:
            layout[r, c] = "."


curr, _ = find_exits(layout, S)
seen = {S, curr}
dots = {}
direction = (curr[0] - S[0], curr[1] - S[1])
moving = True

print_layout(layout, seen)

while moving:
    moving = False
    ch = layout[curr]
    r, c = curr
    if ch == "|" and direction[0] == 1:
        # going down
        if (r, c + 1) in layout and layout[r, c + 1] == ".":
            dots[r, c + 1] = "B"
        if (r, c - 1) in layout and layout[r, c - 1] == ".":
            dots[r, c - 1] = "A"
    elif ch == "|" and direction[0] == -1:
        # going up
        if (r, c - 1) in layout and layout[r, c - 1] == ".":
            dots[r, c - 1] = "B"
        if (r, c + 1) in layout and layout[r, c + 1] == ".":
            dots[r, c + 1] = "A"
    elif ch == "-" and direction[1] == 1:
        # going right
        direction = (0, 1)
        if (r - 1, c) in layout and layout[r - 1, c] == ".":
            dots[r - 1, c] = "B"
        if (r + 1, c) in layout and layout[r + 1, c] == ".":
            dots[r + 1, c] = "A"
    elif ch == "-" and direction[1] == -1:
        # going left
        direction = (0, -1)
        if (r + 1, c) in layout and layout[r + 1, c] == ".":
            dots[r + 1, c] = "B"
        if (r - 1, c) in layout and layout[r - 1, c] == ".":
            dots[r - 1, c] = "A"
    elif ch == "L" and direction[0] == 1:
        # going right
        direction = (0, 1)
        if (r + 1, c) in layout and layout[r + 1, c] == ".":
            dots[r + 1, c] = "A"
        if (r, c - 1) in layout and layout[r, c - 1] == ".":
            dots[r, c - 1] = "A"
    elif ch == "L" and direction[1] == -1:
        # going up
        direction = (-1, 0)
        if (r + 1, c) in layout and layout[r + 1, c] == ".":
            dots[r + 1, c] = "B"
        if (r, c - 1) in layout and layout[r, c - 1] == ".":
            dots[r, c - 1] = "B"
    elif ch == "J" and direction[0] == 1:
        # going left
        direction = (0, -1)
        if (r + 1, c) in layout and layout[r + 1, c] == ".":
            dots[r + 1, c] = "B"
        if (r, c + 1) in layout and layout[r, c + 1] == ".":
            dots[r, c + 1] = "B"
    elif ch == "J" and direction[1] == 1:
        # going up
        direction = (-1, 0)
        if (r + 1, c) in layout and layout[r + 1, c] == ".":
            dots[r + 1, c] = "A"
        if (r, c + 1) in layout and layout[r, c + 1] == ".":
            dots[r, c + 1] = "A"
    elif ch == "7" and direction[0] == -1:
        # going left
        direction = (0, -1)
        if (r - 1, c) in layout and layout[r - 1, c] == ".":
            dots[r - 1, c] = "A"
        if (r, c + 1) in layout and layout[r, c + 1] == ".":
            dots[r, c + 1] = "A"
    elif ch == "7" and direction[1] == 1:
        # going down
        direction = (1, 0)
        if (r - 1, c) in layout and layout[r - 1, c] == ".":
            dots[r - 1, c] = "B"
        if (r, c - 1) in layout and layout[r, c - 1] == ".":
            dots[r, c - 1] = "B"
    elif ch == "F" and direction[1] == -1:
        # going down
        direction = (1, 0)
        if (r - 1, c) in layout and layout[r - 1, c] == ".":
            dots[r - 1, c] = "A"
        if (r, c - 1) in layout and layout[r, c - 1] == ".":
            dots[r, c - 1] = "A"
    elif ch == "F" and direction[0] == -1:
        # going right
        direction = (0, 1)
        if (r - 1, c) in layout and layout[r - 1, c] == ".":
            dots[r - 1, c] = "B"
        if (r, c - 1) in layout and layout[r, c - 1] == ".":
            dots[r, c - 1] = "B"
    else:
        assert False, "oops"
    exits = find_exits(layout, curr)
    for ex in exits:
        if ex in seen:
            continue
        moving = True
        curr = ex
        seen.add(curr)

# Flood fill
while True:
    updated = False
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if (r, c) in seen:
                continue
            if (r, c) in dots:
                continue
            surrounds = 0
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                rr = r + dr
                cc = c + dc
                if (rr, cc) in dots:
                    dots[r, c] = dots[rr, cc]
                    updated = True
                    break
    if not updated:
        break

print_layout(layout, seen)

num_a = 0
num_b = 0
for v in dots.values():
    if v == "A":
        num_a += 1
    else:
        num_b += 1

# Because we flood the area the number enclosed will be the lower number
result = min(num_a, num_b)

# Part 2 = 601
print(f"answer = {result}")

# INTERNET SOLUTION
# Line counting algorithm
# Walls:
# | is clearly a wall
# FJ is a wall and so is F------------J
# L7 is a wall and so is L------------7
# F7 is technically two walls, so can be treated as 0 walls
#    -> F--------------------7
# LJ is the same
# Because we start from the left, we will hit a L or an F before J or 7

# For spaces inside the number of walls will be odd

result = 0
for r in range(len(lines)):
    potential_wall = ""
    count = 0
    for c in range(len(lines[0])):
        if layout[r, c] == "-":
            # Ignore dashes
            continue

        if layout[r, c] == ".":
            if count % 2 == 1:
                result += 1
        elif layout[r, c] == "|":
            count += 1
        elif layout[r, c] in ["F", "L"]:
            # could be start of wall
            potential_wall = layout[r, c]
            continue
        elif layout[r, c] == "J":
            if potential_wall == "F":
                count += 1
        elif layout[r, c] == "7":
            if potential_wall == "L":
                count += 1
        potential_wall = ""

print(f"internet answer = {result}")
