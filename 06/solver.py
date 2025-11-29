races = [(38, 234), (67, 1027), (76, 1157), (73, 1236)]


def calc(t_hold, t_total):
    speed = t_hold
    return speed * (t_total - t_hold)


result = 1

for race in races:
    t, dist = race
    tt = 0
    first = None
    last = None
    while True:
        ans = calc(tt, t)
        if not first and ans > dist:
            first = tt
        elif first and ans > dist:
            last = tt
        elif first and last and ans <= dist:
            result *= last - first + 1
            break
        tt += 1

# Part 1 = 303600
print(f"answer = {result}")

t = 38677673
dist = 234102711571236
p = 0

# Find a value where we are winning so we can start a binary search
while True:
    ans = calc(p, t)
    if ans <= dist:
        p += 100
    else:
        break

# Find the lower limit
l = 0
h = p

while True:
    m = l + (h - l) // 2
    ans = calc(m, t)
    if ans > dist:
        h = m
    else:
        l = m
    if (h - l) == 1:
        break
low = l

# Find the upper limit
l = p
h = t

while True:
    m = l + (h - l) // 2
    ans = calc(m, t)
    if ans > dist:
        l = m
    else:
        h = m
    if (h - l) == 1:
        break
high = l

# Part 2 = 23654842
print(f"answer = {high - low}")
