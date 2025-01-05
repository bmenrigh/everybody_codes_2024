#!/usr/bin/python3

import sys
import copy

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

def cols_equal(cols_a, cols_b):

    return all([a == b for a, b in zip(cols_a, cols_b)])


def dance(cols, c):

    d = cols[c][0]
    cols[c] = cols[c][1:]

    nc = (c + 1) % N

    p = (d - 1) % len(cols[nc])
    if ((d - 1) // len(cols[nc])) % 2 == 1:
        p = len(cols[nc]) - p

    cols[nc] = cols[nc][:p] + [d] + cols[nc][p:]


def get_int(cols):
    row = []
    for c in range(N):
        row.append(cols[c][0])

        rint = int(''.join(list(map(str, row))))

    return rint


def dance_rounds_cycle(cols):

    saved_cols = copy.deepcopy(cols)

    pow_lim = 1

    biggest = get_int(cols)

    c = 0
    while True:

        for i in range(N):
            dance(cols, i % N)
            biggest = max(biggest, get_int(cols))

        c += 1

        if cols_equal(cols, saved_cols):
            print(f"Found cycle at {c} steps ({c * N} dances)")
            return biggest

        if c >= pow_lim:
            print(f"Increasing Brent cycle finding limit to {pow_lim} and saving state")
            saved_cols = copy.deepcopy(cols)
            pow_lim *= 2



print_cols(cols)


ans = dance_rounds_cycle(cols)
print(ans)
