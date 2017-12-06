# --- Part Two ---

# Out of curiosity, the debugger would also like to know the size of the loop: starting from a state that has already been seen, how many block redistribution cycles must be performed before that same state is seen again?

# In the example above, 2 4 1 2 is seen again after four cycles, and so the answer in that example would be 4.

# How many cycles are in the infinite loop that arises from the configuration in your puzzle input?

inp = open("6/input_1.txt").read().strip().split('\t')
inp = [int(number) for number in inp]

seen = {}
cycle = 0
state = ''.join(str(e) for e in inp)

while state not in seen:
    seen[state] =  cycle
    max_val = max(inp)
    max_index = inp.index(max_val)
    inp[max_index] = 0
    cycle += 1
    for i in range(max_index + 1, max_index + max_val + 1):
        inp[i % len(inp)] += 1
    state = ''.join(str(e) for e in inp)

print(cycle - seen[state])