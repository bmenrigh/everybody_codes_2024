#!/usr/bin/python3

import sys

costs = {'A': 0, 'B': 1, 'C': 3}
potions = 0

with open(sys.argv[1]) as lines:
    for line in lines:
        line = line.rstrip("\n")

        for abc in line:
            if abc in costs:
                potions += costs[abc]

print(potions)
