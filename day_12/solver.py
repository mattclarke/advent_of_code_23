import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

def is_legal(line, orig):
    for l, o in zip(line, orig):
        if o == "." and l != ".":
            return 0
        if o == "#" and l != "!":
            return 0
        if l == "!" and o == ".":
            return 0
    return 1

def solve(line, numbers):
    def _recurse(line, numbers, index, orig):
        if not numbers:
            leg = is_legal(line, orig)
            return leg
        n = numbers.pop(0)
        if index + n > len(line):
            return 0
        total = 0
        for i in range(index, len(line)-n+1):
            ch = line[i]
            if ch == ".":
                continue
            temp = line[:i] + "!"*n + line[i+n:]
            if is_legal(temp[i:i+n], orig[i:i+n]):
                total += _recurse(temp, numbers[:], i + n + 1, orig)
        return total

    return _recurse(line, numbers, 0, line)


result = 0

for l in lines:
    pattern, numbers = l.split(" ")
    numbers = [int(x) for x in numbers.split(",")]
    result = solve(pattern, numbers)
    print(result)
    input()


# Part 1 = 6871
print(f"answer = {result}")

result = 0

# Part 2 = 
print(f"answer = {result}")
