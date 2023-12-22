import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]
lines = [[x for x in line] for line in lines]

S= None
for r, row in enumerate(lines):
    for c, ch in enumerate(row):
        if ch == "S":
            S = (r, c)
            break
    if S:
        break
lines[S[0]][S[1]] = "."


possible = {S} 
for _ in range(64):
    new_possible = set()
    for p in possible:
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r = p[0] + dr
            c = p[1] + dc
            if dr ==0 and dc == 0:
                continue
            if r <0 or r >= len(lines):
                continue
            if c <0 or c >= len(lines[0]):
                continue
            if lines[r][c] != "#":
                new_possible.add((r,c))
    possible = new_possible


# Part 1 = 3858
print(f"answer = {len(possible)}")

def print_layout(layout, start=S):
    sor = sorted(layout)
    min_r = min(sor[0][0], 0)
    max_r = max(sor[~0][0], len(lines))
    for r in range(min_r - 1, max_r + 1):
        line = ""
        for c in range(min_r - 1, max_r + 1):
            if (r,c) == S:
                line += "S"
            elif (r,c) in layout:
                line += "O"
            else:
                line += lines[r% len(lines)][c% len(lines)]
        print(line)
    print("================")
    print("size", len(layout))
    print("================")

# print_layout(possible)
# input()

# possible = {S} 
# for i in range(50):
#     # print_layout(possible)
#     # print(i, len(possible))
#     # input()
#     new_possible = set()
#     for p in possible:
#         for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             r = p[0] + dr
#             c = p[1] + dc
#             if dr ==0 and dc == 0:
#                 continue
#             # if r <0 or r >= len(lines):
#             #     continue
#             # if c <0 or c >= len(lines[0]):
#             #     continue
#             rr = r % len(lines)
#             cc = c % len(lines[0])
#             if lines[rr][cc] != "#":
#                 new_possible.add((r,c))
#     possible = new_possible
# print_layout(possible)
# print(len(possible))
# input()

# It forms a diamond and from the start position there are no rocks in the N, S, E, W directions
turns = 25
min_r = S[0] - turns
max_r = S[0] + turns
min_c = S[1] - turns
max_c = S[1] + turns


# count the number of positions in the diamond
# result = 0
# for r in range(0, turns+1):
#     rr = S[0] - r
#     even = True
#     for c in range(-turns + r, turns + 1 - r):
#         cc = S[1] + c
#         # print(rr-S[0], cc-S[1])
#         if lines[rr][cc] != "#" and even:
#             result += 1
#         even = not even
#
# for r in range(1, turns+1):
#     rr = S[0] + r
#     even = True
#     for c in range(-turns + r, turns + 1 - r):
#         cc = S[1] + c
#         # print(rr-S[0], cc-S[1])
#         if lines[rr][cc] != "#" and even:
#             result += 1
#         even = not even
#
# print("result", result)

# The point of the diamond travels 202300 "squares"
# and a half so it is touching the edge of the last square.
REQUIRED = 26501365
NUM_SQUARES = REQUIRED // len(lines)
print(REQUIRED % len(lines))

num_steps_full_square_with_corners = 7780
num_steps_full_square_without_corners = 7769
num_steps_east_tip = 5866
num_steps_west_tip = 5846
num_steps_south_tip = 5853
num_steps_north_tip = 5859
ne_diag_1 = 1030
ne_diag_2 = 6818
se_diag_1 = 1025
se_diag_2 = 6817
sw_diag_1 = 1017
sw_diag_2 = 6805
nw_diag_1 = 1018
nw_diag_2 = 6810

# Internal squares
type_1 = 0
type_2 = 0
temp = NUM_SQUARES * 2
type_1 = temp // 2 + 1
type_2 = temp // 2 
temp -= 2
result = 0

while temp >= 0:
    type_1 += 2*(temp // 2 + 1)
    type_2 += 2*(temp // 2)
    temp -= 2
print(type_1, type_2)
# I think on odd numbers the corners aren't filled (could be wrong though)
result += type_1 *num_steps_full_square_without_corners
result += type_2 * num_steps_full_square_with_corners
print(result)
print("========")
result = 636344188655069

# Diamond tips
result += num_steps_north_tip + num_steps_south_tip + num_steps_east_tip + num_steps_west_tip

# Diagonals
# num squares = manhatten - 1?
num_diagonals = 2 * NUM_SQUARES-1
# NE
result += ne_diag_1 * (num_diagonals + 1)
result += ne_diag_2 * (num_diagonals)
# SE
result += se_diag_1 * (num_diagonals + 1)
result += se_diag_2 * (num_diagonals)
# SW
result += sw_diag_1 * (num_diagonals + 1)
result += sw_diag_2 * (num_diagonals)
# NW
result += nw_diag_1 * (num_diagonals + 1)
result += nw_diag_2 * (num_diagonals)


# 318208381843854 too low
# 318208383866854 too low
# 636404083472624 too high
# 
# 636363162228634 wrong
# 636363157778023 wrong
# 636356868877923 wrong
# 636356868815243 wrong

# Part 2 = 
print(f"answer = {result}")


def solve(start, steps, limit=True):
    possible = {start} 
    for i in range(steps):
        # print_layout(possible)
        # print(i, len(possible))
        # input()
        new_possible = set()
        for p in possible:
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r = p[0] + dr
                c = p[1] + dc
                if dr ==0 and dc == 0:
                    continue
                if limit:
                    if r <0 or r >= len(lines):
                        continue
                    if c <0 or c >= len(lines[0]):
                        continue
                rr = r % len(lines)
                cc = c % len(lines[0])
                if lines[rr][cc] != "#":
                    new_possible.add((r,c))
        possible = new_possible
    return possible


full_square_with_corners = solve(S, 132)
full_square_without_corners = solve(S,133)
num_steps_full_square_with_corners = len(full_square_with_corners)
num_steps_full_square_without_corners = len(full_square_without_corners)

ne_corner_small = solve((130, 0), 65)
ne_corner_big = solve((130,0), 195)
se_corner_small = solve((0,0), 65)
se_corner_big = solve((0,0), 195)
sw_corner_small = solve((0,130), 65)
sw_corner_big = solve((0,130), 195)
nw_corner_small = solve((130, 130), 65)
nw_corner_big = solve((130, 130), 195)

e_point = solve((65, 0), 130)
w_point = solve((65, 130), 130)
n_point = solve((130, 65), 130)
s_point = solve((0, 65), 130)

rounds = 1
# x_rounds = solve(S, 131*rounds + 65, False)
x_rounds = solve(S, 500, False)
print_layout(x_rounds)

# Sanity check
ans = len(x_rounds)
ans -= len(e_point)
ans -= len(w_point)
ans -= len(n_point)
ans -= len(s_point)
ans -= len(ne_corner_small) * rounds
ans -= len(ne_corner_big) * (rounds - 1)
ans -= len(nw_corner_small) * rounds
ans -= len(nw_corner_big) * (rounds - 1)
ans -= len(sw_corner_small) * rounds
ans -= len(sw_corner_big) * (rounds - 1)
ans -= len(se_corner_small) * rounds
ans -= len(se_corner_big) * (rounds - 1)
assert False, ans / 1

# print_layout(one_round)
# After one round the centre square is without corners
# After two rounds the centre square has corners, and so on
num_squares = 1
num_diags = 0
for i in range(0, NUM_SQUARES):
    num_squares += 4 * i
    if num_diags == 0:
        num_diags = 1
    else:
        num_diags += 2

print("diags", num_diags, NUM_SQUARES * 2 + 1)
num_same_as_middle = num_squares // 2 + 1
num_different_to_middle = num_squares // 2
print(num_same_as_middle, num_different_to_middle)

total = 0
if REQUIRED % 2 == 1:
    # Middle square is without corners
    total += num_same_as_middle * num_steps_full_square_without_corners
    total += num_different_to_middle * num_steps_full_square_with_corners
else:
    assert False

print(total)

