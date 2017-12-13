# --- Part Two ---

# There are more programs than just the ones in the group containing program ID 0. The rest of them have no way of reaching that group, and still might have no way of reaching each other.

# A group is a collection of programs that can all communicate via pipes either directly or indirectly. The programs you identified just a moment ago are all part of the same group. Now, they would like you to determine the total number of groups.

# In the example above, there were 2 groups: one consisting of programs 0,2,3,4,5,6, and the other consisting solely of program 1.

# How many groups are there in total?

from collections import defaultdict

with open("12/input.txt") as input_file:
    lines = [line.strip().replace(',', '').split() for line in input_file]

programs = defaultdict(set)
for line in lines:
    programs[line[0]] = line[2:]

visisted = set()
groups = 0

for program in programs.keys():
    if not program in visisted:
        groups += 1
        visisted.add(program)
        arr = [program]
    while arr:
        current = arr.pop()
        for p in programs[str(current)]:
            if not p in visisted:
                visisted.add(p)
                arr.append(p)

print(groups)