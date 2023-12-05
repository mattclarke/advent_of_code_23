import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n")]
print(lines)

_, s = lines[0].split(": ")
seeds = [int(x.strip()) for x in s.split(" ")]

lines.pop(0)
lines.pop(0)

seed_to_soil = []
soil_to_fert = []
fert_to_water = []
water_to_light = []
light_to_temp = []
temp_to_humid = []
humid_to_loc = []

index = 0
while index < len(lines):
    line = lines[index]
    if line.startswith("seed-"):
        index += 1
        while lines[index]:
            l = lines[index].split(" ")
            ans = [int(x.strip()) for x in l]
            seed_to_soil.append(ans)
            index += 1
    if line.startswith("soil-"):
        index += 1
        while lines[index]:
            l = lines[index].split(" ")
            ans = [int(x.strip()) for x in l]
            soil_to_fert.append(ans)
            index += 1
    if line.startswith("fertilizer-"):
        print("fert")
        index += 1
        while lines[index]:
            l = lines[index].split(" ")
            ans = [int(x.strip()) for x in l]
            fert_to_water.append(ans)
            index += 1
    if line.startswith("water-"):
        index += 1
        while lines[index]:
            l = lines[index].split(" ")
            ans = [int(x.strip()) for x in l]
            water_to_light.append(ans)
            index += 1
    if line.startswith("light-"):
        index += 1
        while lines[index]:
            l = lines[index].split(" ")
            ans = [int(x.strip()) for x in l]
            light_to_temp.append(ans)
            index += 1
    if line.startswith("temperature-"):
        index += 1
        while lines[index]:
            l = lines[index].split(" ")
            ans = [int(x.strip()) for x in l]
            temp_to_humid.append(ans)
            index += 1
    if line.startswith("humidity-"):
        index += 1
        while lines[index]:
            l = lines[index].split(" ")
            ans = [int(x.strip()) for x in l]
            humid_to_loc.append(ans)
            index += 1
    index += 1

result = 10000000000

current = list(seeds)

def solve(current, convert):
    result = []
    for s in current:
        ans = s
        for c in convert:
            dest, src, r = c
            if src <= s < src + r:
                diff = s - src
                ans = dest + diff
                break
        result.append(ans)
    return result

current = solve(current, seed_to_soil) 
current = solve(current, soil_to_fert) 
current = solve(current, fert_to_water) 
current = solve(current, water_to_light) 
current = solve(current, light_to_temp) 
current = solve(current, temp_to_humid) 
current = solve(current, humid_to_loc) 


# Part 1 = 227653707
print(f"answer = {min(current)}")

current = []
for i in range(0, len(seeds), 2):
    current.append([seeds[i], seeds[i] + seeds[i+1]-1])


def solve(current, convert):
    result = []
    queue = current
    while queue:
        changed = False
        l, h = queue.pop(0)
        print("1", l, h)
        for c in convert:
            dest, src, r = c
            print(c)
            if src + r <= l or h < src:
                print("out")
                # out of range
                continue
            elif src <= l < src + r and h < src + r:
                # both in range
                print("both")
                changed = True
                l_diff = l - src
                h_diff = h - src
                result.append([dest + l_diff, dest + h_diff])
            elif src <= l < src+r:
                # only l is in range
                print("l")
                changed = True
                l_diff = l - src
                result.append([dest + l_diff, dest + r - 1])
                queue.append([src + r, h])
            elif h >= src and h < src + r:
                # only h in range
                print("h")
                changed = True
                h_diff = h - src
                result.append([dest, dest + h_diff])
                queue.append([l, src - 1])
            else:
                assert False, "oops"
            print("res", result)
            print("q", queue)
        if not changed:
            result.append([l, h])
    return result

print("======")
print(current)
current = solve(current, seed_to_soil) 
print(current)
print("======")
current = solve(current, soil_to_fert) 
print(current)
print("======")
current = solve(current, fert_to_water) 
print(current)
print("======")
current = solve(current, water_to_light) 
print(current)
print("======")
current = solve(current, light_to_temp) 
print(current)
print("======")
# current = solve(current, temp_to_humid) 
# current = solve(current, humid_to_loc) 

# Part 2 = 78775051
print(f"answer = {min(current)}")
