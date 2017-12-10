# --- Part Two ---

# The programs explain the situation: they can't get down. Rather, they could get down, if they weren't expending all of their energy trying to keep the tower balanced. Apparently, one program has the wrong weight, and until it's fixed, they're stuck here.

# For any program holding a disc, each program standing on that disc forms a sub-tower. Each of those sub-towers are supposed to be the same weight, or the disc itself isn't balanced. The weight of a tower is the sum of the weights of the programs in that tower.

# In the example above, this means that for ugml's disc to be balanced, gyxo, ebii, and jptl must all have the same weight, and they do: 61.

# However, for tknk to be balanced, each of the programs standing on its disc and all programs above it must each match. This means that the following sums must all be the same:

#     ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
#     padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
#     fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243

# As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the other two. Even though the nodes above ugml are balanced, ugml itself is too heavy: it needs to be 8 units lighter for its stack to weigh 243 and keep the towers balanced. If this change were made, its weight would be 60.

# Given that exactly one program is the wrong weight, what would its weight need to be to balance the entire tower?

# Given that exactly one program is the wrong weight, what would its weight need to be to balance the entire tower?

from collections import defaultdict, Counter

class Node(object):
    def __init__(self):
        self.parent = None
        self.name = ''
        self.weight = 0
        self.children = []

    def find_root(self):
        node = self
        while node.parent:
            node = node.parent
        return node

    def find_unbalanced_child(self):
        if not self.children:
            return self
        children_sums = defaultdict(list)
        for child in self.children:
            children_sums[child.sum_recursion()].append(child)
        for weight, children in children_sums.items():
            if len(children) == 1:
                return children[0].find_unbalanced_child()
            elif len(children) == len(self.children):
                return self
    
    def sum_recursion(self):
        return self.weight + sum(child.sum_recursion() for child in self.children)

    def __str__(self):
        return self.name + " (" + str(self.weight) + ")" 
    
with open("7/input.txt") as input_file:
    lines = [line.strip().replace(',', '').split() for line in input_file]

nodes = defaultdict(Node)

for line in lines:
    name = line[0]
    node = nodes[name]
    node.name = name
    node.weight = int(line[1].replace('(', '').replace(')', ''))
    if len(line) > 2:
        children = line[3:]
        for child in children:
            nodes[child].parent = node
            nodes[child].name = child
        node.children = [nodes[child] for child in children]

unbalanced = node.find_root().find_unbalanced_child()
child_sum = unbalanced.children[0].sum_recursion() * len(unbalanced.children)
sibling_sum = 0

for sibling in unbalanced.parent.children:
    if sibling.name != unbalanced.name:
        sibling_sum = sibling.sum_recursion()
        break

corrected_weight = sibling_sum - child_sum

print(corrected_weight)


