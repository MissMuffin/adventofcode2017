# --- Part Two ---

# Now, you're ready to remove the garbage.

# To prove you've removed it, you need to count all of the characters within the garbage. The leading and trailing < and > don't count, nor do any canceled characters or the ! doing the canceling.

#     <>, 0 characters.
#     <random characters>, 17 characters.
#     <<<<>, 3 characters.
#     <{!>}>, 2 characters.
#     <!!>, 0 characters.
#     <!!!>>, 0 characters.
#     <{o"i!a,<{i<a>, 10 characters.

# How many non-canceled characters are within the garbage in your puzzle input?

import re

with open("9/input_1.txt") as input_file:
    inp = input_file.read() #read whole file as string

#remove all invalid chars (leading !)
inp = re.sub(r"!.", "", inp)

level = 0
score = 0
in_garbage = False
garbage_counter = 0

for char in inp:
    if in_garbage:
        if char == '>':
            in_garbage = False
        else:
            garbage_counter += 1            
    elif char == '<':
        in_garbage = True
    elif char == '{':
        level += 1
    elif char == '}':
        score += level
        level -= 1

print(garbage_counter)