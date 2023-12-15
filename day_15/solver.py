import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line][0]
codes = lines.split(",")


def hashit(code):
    total = 0
    for ch in code:
        v = ord(ch)
        total += v
        total *= 17
        total = total % 256
    return total


result = 0

for code in codes:
    total = hashit(code)
    result += total

# Part 1 = 513158
print(f"answer = {result}")

boxes = {}

for code in codes:
    if "=" in code:
        seq, num = code.split("=")
        num = int(num)
        hsh = hashit(seq)
        box = boxes.get(hsh, {})
        box[seq] = num
        boxes[hsh] = box
    else:
        seq = code[:-1]
        hsh = hashit(seq)
        box = boxes.get(hsh, {})
        if seq in box:
            del box[seq]
        boxes[hsh] = box

result = 0

for i, box in boxes.items():
    for j, slot in enumerate(box.values()):
        value = (i + 1) * (j + 1) * slot
        result += value

# Part 2 = 200277
print(f"answer = {result}")
