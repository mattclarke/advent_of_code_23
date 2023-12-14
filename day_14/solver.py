import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [[x for x in line] for line in PUZZLE_INPUT.split("\n") if line]

result = 0

layout = {}
for r in range(len(lines)):
    for c in range(len(lines[0])):
        layout[r, c] = lines[r][c]


def generate_hashable(layout):
    total = ""
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            total += layout[row, col]
    return total


def tilt_north(layout):
    for r in range(len(lines)):
        if r == 0:
            continue
        for c in range(len(lines[0])):
            v = layout[r, c]
            if v == "O":
                cr = r
                while cr > 0:
                    if layout[cr - 1, c] == ".":
                        layout[cr, c] = "."
                        layout[cr - 1, c] = "O"
                        cr -= 1
                    else:
                        break
    return layout


def tilt_south(layout):
    for r in range(len(lines) - 1, -1, -1):
        if r == len(lines) - 1:
            continue
        for c in range(len(lines[0])):
            v = layout[r, c]
            if v == "O":
                cr = r
                while cr < len(lines) - 1:
                    if layout[cr + 1, c] == ".":
                        layout[cr, c] = "."
                        layout[cr + 1, c] = "O"
                        cr += 1
                    else:
                        break
    return layout


def tilt_west(layout):
    for c in range(len(lines[0])):
        if c == 0:
            continue
        for r in range(len(lines)):
            v = layout[r, c]
            if v == "O":
                cc = c
                while cc > 0:
                    if layout[r, cc - 1] == ".":
                        layout[r, cc] = "."
                        layout[r, cc - 1] = "O"
                        cc -= 1
                    else:
                        break
    return layout


def tilt_east(layout):
    for c in range(len(lines[0]) - 1, -1, -1):
        if c == len(lines[0]) - 1:
            continue
        for r in range(len(lines)):
            v = layout[r, c]
            if v == "O":
                cc = c
                while cc < len(lines[0]) - 1:
                    if layout[r, cc + 1] == ".":
                        layout[r, cc] = "."
                        layout[r, cc + 1] = "O"
                        cc += 1
                    else:
                        break
    return layout


new_layout = tilt_north(copy.copy(layout))

for r in range(len(lines)):
    for c in range(len(lines[0])):
        if new_layout[r, c] == "O":
            result += len(lines) - r

# Part 1 = 113525
print(f"answer = {result}")

seen = {}
repeats = None

new_layout = copy.copy(layout)
for i in range(1000000000):
    new_layout = tilt_north(copy.copy(new_layout))
    new_layout = tilt_west(copy.copy(new_layout))
    new_layout = tilt_south(copy.copy(new_layout))
    new_layout = tilt_east(copy.copy(new_layout))
    hashable = generate_hashable(new_layout)
    if hashable in seen:
        repeats = i - seen[hashable]
        break
    seen[hashable] = i

remaining_turns = (1000000000 - i - 1) % repeats

for i in range(remaining_turns):
    new_layout = tilt_north(copy.copy(new_layout))
    new_layout = tilt_west(copy.copy(new_layout))
    new_layout = tilt_south(copy.copy(new_layout))
    new_layout = tilt_east(copy.copy(new_layout))


result = 0
for r in range(len(lines)):
    for c in range(len(lines[0])):
        if new_layout[r, c] == "O":
            result += len(lines) - r

# Part 2 = 101292
print(f"answer = {result}")
