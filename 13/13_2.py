# --- Part Two ---

# Now, you need to pass through the firewall without being caught - easier said than done.

# You can't control the speed of the packet, but you can delay it any number of picoseconds. For each picosecond you delay the packet before beginning your trip, all security scanners move one step. You're not in the firewall during this time; you don't enter layer 0 until you stop delaying the packet.

# In the example above, if you delay 10 picoseconds (picoseconds 0 - 9), you won't get caught:

# State after delaying:
#  0   1   2   3   4   5   6
# [ ] [S] ... ... [ ] ... [ ]
# [ ] [ ]         [ ]     [ ]
# [S]             [S]     [S]
#                 [ ]     [ ]

# Picosecond 10:
#  0   1   2   3   4   5   6
# ( ) [S] ... ... [ ] ... [ ]
# [ ] [ ]         [ ]     [ ]
# [S]             [S]     [S]
#                 [ ]     [ ]

#  0   1   2   3   4   5   6
# ( ) [ ] ... ... [ ] ... [ ]
# [S] [S]         [S]     [S]
# [ ]             [ ]     [ ]
#                 [ ]     [ ]


# Picosecond 11:
#  0   1   2   3   4   5   6
# [ ] ( ) ... ... [ ] ... [ ]
# [S] [S]         [S]     [S]
# [ ]             [ ]     [ ]
#                 [ ]     [ ]

#  0   1   2   3   4   5   6
# [S] (S) ... ... [S] ... [S]
# [ ] [ ]         [ ]     [ ]
# [ ]             [ ]     [ ]
#                 [ ]     [ ]


# Picosecond 12:
#  0   1   2   3   4   5   6
# [S] [S] (.) ... [S] ... [S]
# [ ] [ ]         [ ]     [ ]
# [ ]             [ ]     [ ]
#                 [ ]     [ ]

#  0   1   2   3   4   5   6
# [ ] [ ] (.) ... [ ] ... [ ]
# [S] [S]         [S]     [S]
# [ ]             [ ]     [ ]
#                 [ ]     [ ]


# Picosecond 13:
#  0   1   2   3   4   5   6
# [ ] [ ] ... (.) [ ] ... [ ]
# [S] [S]         [S]     [S]
# [ ]             [ ]     [ ]
#                 [ ]     [ ]

#  0   1   2   3   4   5   6
# [ ] [S] ... (.) [ ] ... [ ]
# [ ] [ ]         [ ]     [ ]
# [S]             [S]     [S]
#                 [ ]     [ ]


# Picosecond 14:
#  0   1   2   3   4   5   6
# [ ] [S] ... ... ( ) ... [ ]
# [ ] [ ]         [ ]     [ ]
# [S]             [S]     [S]
#                 [ ]     [ ]

#  0   1   2   3   4   5   6
# [ ] [ ] ... ... ( ) ... [ ]
# [S] [S]         [ ]     [ ]
# [ ]             [ ]     [ ]
#                 [S]     [S]


# Picosecond 15:
#  0   1   2   3   4   5   6
# [ ] [ ] ... ... [ ] (.) [ ]
# [S] [S]         [ ]     [ ]
# [ ]             [ ]     [ ]
#                 [S]     [S]

#  0   1   2   3   4   5   6
# [S] [S] ... ... [ ] (.) [ ]
# [ ] [ ]         [ ]     [ ]
# [ ]             [S]     [S]
#                 [ ]     [ ]


# Picosecond 16:
#  0   1   2   3   4   5   6
# [S] [S] ... ... [ ] ... ( )
# [ ] [ ]         [ ]     [ ]
# [ ]             [S]     [S]
#                 [ ]     [ ]

#  0   1   2   3   4   5   6
# [ ] [ ] ... ... [ ] ... ( )
# [S] [S]         [S]     [S]
# [ ]             [ ]     [ ]
#                 [ ]     [ ]

# Because all smaller delays would get you caught, the fewest number of picoseconds you would need to delay to get through safely is 10.

# What is the fewest number of picoseconds that you need to delay the packet to pass through the firewall without being caught?

from collections import defaultdict
from copy import deepcopy

def do_step(wall):
    for f in wall.values():
        if f:
            if f[2] == 0:
                f[0] += 1
                if f[0] == f[1]-1:
                    f[2] = 1
            elif f[2] == 1:
                f[0] -= 1
                if f[0] == 0:
                    f[2] = 0
    return wall

def gets_caught(firewall):
    wall = deepcopy(firewall)
    for i in range(end):
        f = wall[str(i)]
        # print(i, f)
        if f:
            if f[0] == 0:
                # print("CAUGHT")
                return True
        wall = do_step(wall)
    return False

def find_delay(firewall):
    delay = 0
    while True:#delay < 13:
        if gets_caught(firewall):
            # print("DELAY", delay)
            delay += 1
            if delay % 10000 == 0:
                print(delay)
            firewall = do_step(firewall)
        else:
            return delay

with open("13/input.txt") as input_file:
    inp = [line.strip().replace(':', '').split() for line in input_file]

# determine how many steps
end = int(inp[len(inp) - 1][0]) + 1

# fill defualtdcit with values form input
firewall = defaultdict(list)
for line in inp:
    firewall[line[0]] = [0, int(line[1]), 0] #current position, length, 0:increment | 1:decrement

result = find_delay(firewall)
print(result)