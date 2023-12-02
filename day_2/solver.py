import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

result_1= 0
result_2= 0

for i, l in enumerate(lines, start=1):
    _, info = l.split(": ")
    hands = info.split("; ")
    max_blue = 0
    max_red = 0
    max_green = 0
    for hand in hands:
        parts = hand.split(", ")
        for part in parts:
            num, colour = part.split(" ")
            if colour == "blue":
                max_blue = max(max_blue, int(num))
            elif colour == "red":
                max_red = max(max_red, int(num))
            elif colour == "green":
                max_green = max(max_green, int(num))
    result_2 += max_green * max_blue * max_red
    if max_red > 12 or max_blue > 14 or max_green > 13:
        continue
    result_1 += i 

# Part 1 = 2377
print(f"answer = {result_1}")

# Part 2 = 71220
print(f"answer = {result_2}")
