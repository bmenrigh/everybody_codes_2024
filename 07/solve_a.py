#!/usr/bin/python3

import sys
import re

track_re = re.compile(r'^([A-Z]+):([,+=-]+)$')

tracks = {}
with open(sys.argv[1]) as lines:
    for line in lines:
        line = line.rstrip("\n")

        m = re.match(track_re, line)

        if m is None:
            print(f"Unable to pares line {line}")
            continue

        name = m.group(1)
        trackstr = m.group(2)

        tracklist = trackstr.split(",")

        tracks[name] = tracklist


def score_track(track, p, l):

    score = 0
    tlen = len(track)

    for i in range(l):
        t_op = track[i % tlen]

        if t_op == '+':
            p += 1
        elif t_op == '-':
            p -= 1
            p = max(p, 0)

        score += p

    return score


ranking = "".join(sorted(tracks.keys(), key = lambda x: score_track(tracks[x], 10, 10), reverse = True))

print(ranking)
