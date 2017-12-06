# --- Day 4: High-Entropy Passphrases ---

# A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

# To ensure security, a valid passphrase must contain no duplicate words.

# For example:

#     aa bb cc dd ee is valid.
#     aa bb cc dd aa is not valid - the word aa appears more than once.
#     aa bb cc dd aaa is valid - aa and aaa count as different words.

# The system's full passphrase list is available as your puzzle input. How many passphrases are valid?


def valid_passphrase(line):
    seen = set()
    uniq = []
    for word in line:
        if word not in seen:
            seen.add(word)
        else:
            return False
    return True

with open("4/input_4_1.txt") as input_file:
    lines = [line.split() for line in input_file]

valid = 0

for line in lines:
    if valid_passphrase(line):
        valid += 1

print(valid)