#!/usr/bin/python3

import sys
import re

words_re = re.compile(r'^WORDS:(\S+)\s*$')


grid = []
words = None
with open(sys.argv[1]) as lines:
    gotwords = False
    for line in lines:
        line = line.rstrip("\n")

        if line == "":
            continue

        if not gotwords:

            m = re.match(words_re, line)

            if m is not None:
                words = m.group(1).split(",")
                gotwords = True
                continue

        if gotwords:
            grid.append(list(line))


H = len(grid)
W = len(grid[0])

def printgrid(grid):
    for l in grid:
        print(l)

def printgrid_masked(grid, mask):
    for y in range(H):
        for x in range(W):
            if mask[y][x] == 1:
                print(grid[y][x], end="")
            else:
                print(" ", end="")
        print("")


def getword(grid, x, y, d, l):

    w = []
    for i in range(l):
        ny = y + d[1] * i
        if ny < 0 or ny >= H:
            return ""

        w.append(grid[ny][(x + d[0] * i) % W])

    return "".join(w)


def setmask(mask, x, y, d, l):

    for i in range(l):
        mask[(y + d[1] * i) % H][(x + d[0] * i) % W] = 1

printgrid(grid)

mask = []
for l in grid:
    mask.append([0] * len(l))

for y in range(H):
    for x in range(W):
        for w in words:
            for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if w == getword(grid, x, y, d, len(w)):
                    setmask(mask, x, y, d, len(w))


printgrid_masked(grid, mask)

count = 0
for l in mask:
    count += sum(l)

print(count)
