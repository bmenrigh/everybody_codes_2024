#!/usr/bin/python3

import sys

grid = []
with open(sys.argv[1]) as lines:
    for line in lines:
        line = line.rstrip("\n")

        grid.append(list(map(int, line.split(" "))))


cols = list(map(list, zip(*grid)))

N = len(cols)

#print(f"grid: {grid}")

def print_cols(cols):
    havemore = True
    r = 0
    while havemore:
        havemore = False

        row = []

        for c in range(N):
            if r < len(cols[c]):
                row.append(str(cols[c][r]))
                havemore = True
            else:
                row.append(" ")

        print(" ".join(row))
        r += 1

#print_cols(cols)


def dance(cols, c):

    d = cols[c][0]
    cols[c] = cols[c][1:]

    nc = (c + 1) % N

    p = (d - 1) % len(cols[nc])
    if ((d - 1) // len(cols[nc])) % 2 == 1:
        p = len(cols[nc]) - p

    cols[nc] = cols[nc][:p] + [d] + cols[nc][p:]


def dance_rounds(cols, n):

    top_rows = []
    for i in range(n):
        dance(cols, i % N)
        row = []
        for c in range(N):
            row.append(cols[c][0])
        top_rows.append(row)
        print_cols(cols)

    return top_rows


print_cols(cols)
top_rows = dance_rounds(cols, 10)

for i in range(len(top_rows)):
    print(f"{i + 1 :2d}: {''.join(list(map(str, top_rows[i])))}")
