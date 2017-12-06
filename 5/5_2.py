# --- Part Two ---

# Now, the jumps are even stranger: after each jump, if the offset was three or more, instead decrease it by 1. Otherwise, increase it by 1 as before.

# Using this rule with the above example, the process now takes 10 steps, and the offset values after finding the exit are left as 2 3 2 3 -1.

# How many steps does it now take to reach the exit?

with open("5/input_1.txt") as input_file:
    jumps = [int(i) for i in input_file]

counter = 0
current_index = 0
end_of_jumps = len(jumps)

while current_index < end_of_jumps:
    offset = jumps[current_index]
    if offset >= 3:
        jumps[current_index] -= 1
    else:
        jumps[current_index] += 1
    current_index += offset
    counter += 1

print(counter)