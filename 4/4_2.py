# --- Part Two ---

# For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

# For example:

#     abcde fghij is a valid passphrase.
#     abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
#     a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
#     iiii oiii ooii oooi oooo is valid.
#     oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.

# Under this new system policy, how many passphrases are valid?

import itertools

def valid_passphrase(line):
    for a,b in itertools.combinations(line, 2):
        if is_permutation(a, b):
            return False
    return True

def is_permutation(a, b):
    if len(a) != len(b):
        return False
    if sort_word(a) != sort_word(b):
        return False
    return True

def sort_word(word):
    return ''.join(sorted(word))
        

with open("4/input.txt") as input_file:
    lines = [line.split() for line in input_file]

valid = 0

for line in lines:
    if valid_passphrase(line):
        valid += 1

print(valid)