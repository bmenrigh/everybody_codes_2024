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


def dance_rounds_cycle(cols):

    orig_calls = copy.deepcopy(cols)

    biggest = 0
    i = 0
    while True:
        if i % N == 0:
            prev_calls = copy.deepcopy(cols)

        dance(cols, i % N)
        i += 1

        #if i % 1000 == 0:
        #print_cols(cols)

        row = []
        for c in range(N):
            row.append(cols[c][0])

        rint = int(''.join(list(map(str, row))))

        if rint > biggest:
            biggest = rint
            print(f"New biggest: {biggest}")


        # Ugh to do this right I need a proper cycle finding
        # algorithm. Seems like too much work for a problem
        # where I already have the correct answer...

        if cols_equal(cols, orig_calls):
            print(f"Found cycle after {i} dances")
            return biggest

        if cols_equal(cols, prev_calls):
            print(f"Found fixed point after {i} dances")
            return biggest



print_cols(cols)


ans = dance_rounds_cycle(cols)
print(ans)
