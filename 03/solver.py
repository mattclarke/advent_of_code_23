import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

valid_items = []
potential_cogs = {}

for y, l in enumerate(lines):
    in_number = False
    number = ""
    valid = False
    is_cog = False
    for x, ch in enumerate(l):
        if ch.isdigit() and not in_number:
            number = ch
            in_number = True
            valid = False
            is_cog = False
        elif ch.isdigit():
            number += ch
        elif not ch.isdigit() and in_number:
            in_number = False
            if valid:
                valid_items.append(int(number))
        if in_number:
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    ny = y + dy
                    nx = x + dx
                    if ny < 0 or ny >= len(lines):
                        continue
                    if nx < 0 or nx >= len(lines[0]):
                        continue
                    if lines[ny][nx].isdigit():
                        continue
                    if lines[ny][nx] == ".":
                        continue
                    if lines[ny][nx] == "*" and not is_cog:
                        temp = potential_cogs.get((ny, nx), [])
                        temp.append(len(valid_items))
                        potential_cogs[(ny, nx)] = temp
                        is_cog = True

                    valid = True
        if x == len(l) - 1 and valid and in_number:
            valid_items.append(int(number))

# Part 1 = 532445
print(f"answer = {sum(valid_items)}")

result = 0

for n, v in potential_cogs.items():
    if len(v) == 2:
        result += valid_items[v[0]] * valid_items[v[1]]

# Part 2 = 79842967
print(f"answer = {result}")
