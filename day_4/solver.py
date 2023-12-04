import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

result = 0
# For part 2
cards = []
wins = []

for i, l in enumerate(lines):
    _, l = l.split(": ")
    winning, hand = l.split(" | ")
    winning = [x for x in winning.split(" ") if x.strip()]
    hand = [x for x in hand.split(" ") if x.strip()]
    cards.append((winning, hand))
    matches = set(winning) & set(hand)
    wins.append(len(matches))
    if matches:
        result += pow(2, len(matches) - 1)

# Part 1 = 23750
print(f"answer = {result}")

num_cards = [1 for _ in cards]
index = 0

while True:
    winning, hand = cards[index % len(cards)]
    matches = wins[index % len(cards)]
    for num in range(num_cards[index]):
        for i in range(1, matches + 1):
            if index + i > len(num_cards):
                num_cards.append(1)
            else:
                num_cards[index + i] += 1
    index += 1
    if index == len(num_cards):
        break


# Part 2 = 13261850
print(f"answer = {sum(num_cards)}")
