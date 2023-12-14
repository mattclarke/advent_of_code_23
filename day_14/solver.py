import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [[x for x in line] for line in PUZZLE_INPUT.split("\n") if line]


def print_layout(layout):
    for row in range(len(lines)):
        line = ""
        for col in range(len(lines[0])):
            line += layout[row,col]
        print(line)
    print()

result = 0

layout = {}
for r in range(len(lines)):
    for c in range(len(lines[0])):
        layout[r,c] = lines[r][c]
print_layout(layout)


for r in range(len(lines)):
    if r == 0:
        continue
    for c in range(len(lines[0])):
        v = layout[r,c]
        if v == "O":
            cr = r
            while cr > 0:
                if layout[cr - 1, c] == ".":
                    layout[cr, c] = "."
                    layout[cr-1,c] = "O"
                    cr -= 1
                else:
                    break
                

print_layout(layout)

for r in range(len(lines)):
    for c in range(len(lines[0])):
        if layout[r,c] == "O":
            result += len(lines) - r
# Part 1 = 
print(f"answer = {result}")

result = 0

# Part 2 = 
print(f"answer = {result}")
