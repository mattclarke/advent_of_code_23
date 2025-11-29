import copy
import functools
import sys
from collections import Counter, defaultdict


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

hands = []

for l in lines:
    cards, bid = l.split(" ")
    hands.append((cards, int(bid)))

values = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}


def score(hand, pt2=False):
    counts = Counter(hand)
    if pt2:
        num_j = counts["J"]
        if num_j == 5:
            return 7
        del counts["J"]
        in_order = sorted(counts.values())
        in_order[~0] += num_j
    else:
        in_order = sorted(counts.values())

    if len(in_order) == 1:
        # five of a kind
        return 7
    elif in_order[~0] == 4:
        # four of a kind
        return 6
    elif in_order[0] == 2 and in_order[~0] == 3:
        # full house
        return 5
    elif in_order[~0] == 3:
        # three of a kind
        return 4
    elif in_order[~0] == 2 and in_order[~1] == 2:
        # two pair
        return 3
    elif in_order[~0] == 2:
        # one pair
        return 2
    else:
        # high card
        return 1


def compare_hands(a, b, pt2=False):
    a = a[0]
    b = b[0]
    score_a = score(a, pt2)
    score_b = score(b, pt2)
    if score_a < score_b:
        return -1
    elif score_a > score_b:
        return 1
    else:
        for aa, bb in zip(a, b):
            va = values.get(aa)
            vb = values.get(bb)
            va = int(aa) if va is None else va
            vb = int(bb) if vb is None else vb

            if va > vb:
                return 1
            elif vb > va:
                return -1
        assert False, "Ooops!"


ranked = sorted(hands, key=functools.cmp_to_key(compare_hands))


result = 0
for i, (h, sc) in enumerate(ranked, 1):
    result += i * sc

# Part 1 = 253933213
print(f"answer = {result}")

values["J"] = 0
compare_func = lambda a, b: compare_hands(a, b, True)
ranked = sorted(hands, key=functools.cmp_to_key(compare_func))

result = 0
for i, (h, sc) in enumerate(ranked, 1):
    result += i * sc


# Part 2 = 253473930
print(f"answer = {result}")
