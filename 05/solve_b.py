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


def dance_rounds_until(cols, rep):

    row_count = {}

    i = 0
    while True:
        dance(cols, i % N)

        row = []
        for c in range(N):
            row.append(cols[c][0])

        rint = int(''.join(list(map(str, row))))
        row_count[rint] = row_count.get(rint, 0) + 1

        if row_count[rint] >= rep:
            print(f"Round {i + 1} shouted {rint} {rep} times")
            return (i + 1) * rint

        i += 1




print_cols(cols)

ans = dance_rounds_until(cols, 2024)
print(ans)
