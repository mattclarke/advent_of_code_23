import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]
print(lines)

route = lines.pop(0)

M = {}

for l in lines:
    l = l.replace(" = ", " ").replace("(", "").replace(")", "").replace(",", "")
    pos, left, right = l.split(" ")
    M[pos] = (left, right)

result = 0
loc = "AAA"
index = 0

while loc != "ZZZ":
    choice = route[index % len(route)]
    if choice == "L":
        loc = M[loc][0]
    else:
        loc = M[loc][1]
    index += 1
    result += 1



# Part 1 = 
print(f"answer = {result}")

result = 0

# Part 2 = 
print(f"answer = {result}")
