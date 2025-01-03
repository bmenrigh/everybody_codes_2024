#!/usr/bin/python3

import sys

grid = []
with open(sys.argv[1]) as lines:
    for line in lines:
        line = line.rstrip("\n")

        grid.append(line)



dirt = []
for l in grid:
    dirt.append([0] * len(l))

H = len(dirt)
W = len(dirt[0])

removed = 0
still_digging = True
while still_digging:

    still_digging = False
    for y in range(H):
        for x in range(W):

            if grid[y][x] != '#':
                continue

            nh = dirt[y][x] + 1

            candig = True
            for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + d[0], y + d[1]

                if nh - dirt[ny][nx] > 1:
                    candig = False
                    break

            if candig:
                dirt[y][x] = nh
                removed += 1
                still_digging = True

print(removed)
