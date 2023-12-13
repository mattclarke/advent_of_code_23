import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

def is_legal(line, orig):
    # print(line, orig)
    for l, o in zip(line, orig):
        if o == "." and l != ".":
            return 0
        if o == "#" and l != "!":
            return 0
        if l == "!" and o == ".":
            return 0
    return 1

def solve(line, numbers):
    def _recurse(line, numbers, index, orig, cache):
        nc = numbers[:]
        cached = cache.get((line, tuple(numbers)))
        if cached is not None:
            return cached
        if not numbers:
            leg = is_legal(line, orig)
            return leg
        n = numbers.pop(0)
        if n > len(line):
            return 0
        total = 0
        for i in range(0, len(line)-n+1):
            ch = line[i]
            if ch == ".":
                continue
            temp = line[:i] + "!"*n + line[i+n:]
            if i+n < len(temp) and temp[i+n] == "#":
                pass
            elif is_legal(temp[:i+n], orig[:i+n]):
                total += _recurse(temp[i+n+1:], numbers[:], i + n + 1, orig[i+n+1:], cache)

        cache[(line, tuple(nc))] = total
        return total

    return _recurse(line, numbers, 0, line, {})


result = 0

for l in lines:
    pattern, numbers = l.split(" ")
    numbers = [int(x) for x in numbers.split(",")]
    temp = solve(pattern, numbers)
    result += temp
    # input()


# Part 1 = 6871
print(f"answer = {result}")

result = 0

# Part 2 = 
print(f"answer = {result}")
