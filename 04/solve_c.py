#!/usr/bin/python3

import sys

nails = []
with open(sys.argv[1]) as lines:
    for line in lines:
        line = line.rstrip("\n")

        nlen = int(line)

        nails.append(nlen)


nails.sort()

nmed = nails[len(nails) // 2]

print(f"Median found {nmed} for {len(nails)} nails")

hits = 0
for nlen in nails:
    if nlen < nmed:
        hits += nmed - nlen
    else:
        hits += nlen - nmed

print(hits)

