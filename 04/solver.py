import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

result = 0
# For part 2
wins = []

for i, l in enumerate(lines):
    _, l = l.split(": ")
    winning, hand = l.split(" | ")
    winning = [x for x in winning.split(" ") if x.strip()]
    hand = [x for x in hand.split(" ") if x.strip()]
    matches = set(winning) & set(hand)
    wins.append(len(matches))
    if matches:
        result += pow(2, len(matches) - 1)

# Part 1 = 23750
print(f"answer = {result}")

num_cards = [1 for _ in lines]
result = 0

for i, l in enumerate(lines):
    result += num_cards[i]
    matches = wins[i]
    for j in range(1, matches + 1):
        num_cards[i + j] += num_cards[i]

# Part 2 = 13261850
print(f"answer = {result}")
