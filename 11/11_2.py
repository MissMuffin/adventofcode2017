# --- Part Two ---

# How many steps away is the furthest he ever got from his starting position?

with open("11/input.txt") as input_file:
    steps = input_file.read().strip().split(',')

pos = [0,0] #y, x
dist = 0
max_dist = 0

for step in steps:
    if step == "n":
        pos[0] += 2
    elif step == "s":
        pos[0] -= 2
    elif step == "nw":
        pos[0] += 1
        pos[1] -= 1
    elif step == "ne":
        pos[0] += 1
        pos[1] += 1
    elif step == "sw":
        pos[0] -= 1
        pos[1] -= 1
    elif step == "se":
        pos[0] -= 1
        pos[1] += 1

    dist = (abs(pos[0]) + abs(pos[1])) // 2
    max_dist = max(dist, max_dist)

print(dist)
print(max_dist)