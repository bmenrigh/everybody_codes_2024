#!/usr/bin/python3

import sys

costs = {'A': 0, 'B': 1, 'C': 3, 'D': 5}
potions = 0

with open(sys.argv[1]) as lines:
    for line in lines:
        line = line.rstrip("\n")

        for i in range(0, len(line), 2):
            if line[i] != 'x' and line[i + 1] != 'x':
                potions += 2

            if line[i] in costs:
                potions += costs[line[i]]

            if line[i + 1] in costs:
                potions += costs[line[i + 1]]


print(potions)
