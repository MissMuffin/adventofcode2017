# --- Part Two ---

# To be safe, the CPU also needs to know the highest value held in any register during this process so that it can decide how much memory to allocate to these operations. For example, in the above instructions, the highest value ever held was 10 (in register c after the third instruction was evaluated).

from collections import defaultdict

with open("8/input.txt") as input_file:
    lines = [line.split() for line in input_file]

highest = 0

def inc(register, val):
    global highest
    registers[register] += val
    highest = max(highest, registers[register])

def dec(register, val):
    global highest
    registers[register] -= val
    highest = max(highest, registers[register])

registers = defaultdict(int)

for line in lines:
    register = line[0]
    func = line[1]
    val = line[2]
    function_call = func + "('" + register + "', " + val + ")"
    condition = "registers['" + line[4] + "'] "  + line[5] + " " + line[6]
    if eval(condition):
        eval(function_call)
 
print(highest)