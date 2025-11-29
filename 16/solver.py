import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

WIDTH = len(lines[0])
HEIGHT = len(lines)


def solve(start, initial_dir):
    seen = set()
    Q = [(start, initial_dir)]
    while Q:
        (r, c), d = Q.pop(0)
        while r < HEIGHT and c < WIDTH and r >= 0 and c >= 0:
            if (r, c, d) in seen:
                break
            seen.add((r, c, d))
            if lines[r][c] == ".":
                if d == "R":
                    c += 1
                elif d == "L":
                    c -= 1
                elif d == "D":
                    r += 1
                elif d == "U":
                    r -= 1
                else:
                    assert False
            elif lines[r][c] == "/":
                if d == "R":
                    r -= 1
                    d = "U"
                elif d == "L":
                    r += 1
                    d = "D"
                elif d == "D":
                    c -= 1
                    d = "L"
                elif d == "U":
                    c += 1
                    d = "R"
                else:
                    assert False
            elif lines[r][c] == "\\":
                if d == "R":
                    r += 1
                    d = "D"
                elif d == "L":
                    r -= 1
                    d = "U"
                elif d == "D":
                    c += 1
                    d = "R"
                elif d == "U":
                    c -= 1
                    d = "L"
                else:
                    assert False
            elif lines[r][c] == "|" and d in ["L", "R"]:
                Q.append(((r + 1, c), "D"))
                r -= 1
                d = "U"
            elif lines[r][c] == "-" and d in ["U", "D"]:
                Q.append(((r, c + 1), "R"))
                c -= 1
                d = "L"
            elif lines[r][c] == "|" and d in ["U", "D"]:
                if d == "U":
                    r -= 1
                else:
                    r += 1
            elif lines[r][c] == "-" and d in ["L", "R"]:
                if d == "L":
                    c -= 1
                else:
                    c += 1
            else:
                print(lines[r][c], r, c, d)
                assert False
    squares = set()
    for r, c, _ in seen:
        squares.add((r, c))
    return len(squares)


# Part 1 = 7632
print(f"answer = {solve((0,0), 'R')}")

result = 0

for r in range(HEIGHT):
    for c in range(WIDTH):
        if (r, c) == (0, 0):
            result = max(result, solve((r, c), "R"))
            result = max(result, solve((r, c), "D"))
        elif (r, c) == (HEIGHT - 1, 0):
            result = max(result, solve((r, c), "R"))
            result = max(result, solve((r, c), "U"))
        elif (r, c) == (0, WIDTH - 1):
            result = max(result, solve((r, c), "L"))
            result = max(result, solve((r, c), "D"))
        elif (r, c) == (HEIGHT - 1, WIDTH - 1):
            result = max(result, solve((r, c), "L"))
            result = max(result, solve((r, c), "U"))
        elif r == 0:
            result = max(result, solve((r, c), "D"))
        elif r == HEIGHT - 1:
            result = max(result, solve((r, c), "U"))
        elif c == 0:
            result = max(result, solve((r, c), "R"))
        elif c == WIDTH - 1:
            result = max(result, solve((r, c), "L"))


# Part 2 = 8023
print(f"answer = {result}")
