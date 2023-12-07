import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

result = 0
hands = []

for l in lines:
    cards, bid = l.split(" ")
    hands.append((cards, int(bid)))

def score(hand):
    ac = sorted(hand)
    if ac[0] == ac[4]:
        # five of a kind
        score = 7
    elif ac[0] == ac[3] or ac[1] == ac[4]:
        # four of a kind
        score = 6
    elif ac[0] == ac[2] and ac[3] == ac[4]:
        # full house
        score = 5
    elif ac[0] == ac[1] and ac[2] == ac[4]:
        # full house
        score = 5
    elif ac[0] == ac[2] or ac[1] == ac[3] or ac[2] == ac[4]:
        # three of a kind
        score = 4
    else:
        s = set(ac)
        if len(s) == 3:
            # two pair
            score = 3
        elif len(s) == 4:
            # one pair
            score = 2
        else:
            # high card
            score = 1
    return score


values = {
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14
        }


def compare_hands(a, b):
    a = a[0]
    b = b[0]
    score_a = score(a)
    score_b = score(b)
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
                return - 1
        assert False, "Ooops!"


import functools

ranked = sorted(hands, key=functools.cmp_to_key(compare_hands))

print(ranked)

result = 0
for i, (h, sc) in enumerate(ranked, 1):
    result += i * sc

# Part 1 = 253933213
print(f"answer = {result}")

result = 0

# Part 2 = 
print(f"answer = {result}")
