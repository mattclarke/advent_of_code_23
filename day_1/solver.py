import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

result = 0

for l in lines:
    numbers = []
    for ch in l:
        if ch.isdigit():
            numbers.append(ch)
    first_last = numbers[0] + numbers[~0]
    result += int(first_last)

# Part 1 = 54644
print(f"answer = {result}")

result = 0

converter = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
    }

for l in lines:
    temp = ""
    numbers = []
    for ch in l:
        if ch.isdigit():
            numbers.append(ch)
        else:
            temp += ch
            for n, v in converter.items():
                if temp.endswith(n):
                    numbers.append(v)
                    break

    first_last = numbers[0] + numbers[~0]
    result += int(first_last)

# Part 2 = 53348
print(f"answer = {result}")
