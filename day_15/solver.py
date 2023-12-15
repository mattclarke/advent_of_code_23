import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line][0]

codes = lines.split(",")

result = 0

for code in codes:
    total = 0
    for ch in code:
        v = ord(ch)
        total += v
        total *= 17
        total = total % 256
    result += total

        



# Part 1 = 513158
print(f"answer = {result}")

result = 0

# Part 2 = 
print(f"answer = {result}")
