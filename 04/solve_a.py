#!/usr/bin/python3

import sys

hits = 0
minlen = -1
ncount = 0
with open(sys.argv[1]) as lines:
    for line in lines:
        line = line.rstrip("\n")

        ncount += 1

        nlen = int(line)

        hits += nlen

        if nlen < minlen or minlen == -1:
            minlen = nlen


print(hits - (minlen * ncount))
