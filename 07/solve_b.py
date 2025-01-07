#!/usr/bin/python3

import sys
import re

tracks_re = re.compile(r'^([A-Z]+):([,+=-]+)$')
maintrack_ud_re = re.compile(r'^[S+=-]+$')
maintrack_lr_re = re.compile(r'^([+=-])\s+([+=-])$')

maintrack = []

with open(sys.argv[1]) as lines:

    main_u = []
    main_l = []
    main_r = []
    main_d = []

    gottop = False

    for line in lines:
        line = line.rstrip("\n")

        if not gottop:
            m = re.match(maintrack_ud_re, line)

            if m is None:
                print(f"Failed to parse top track line {line}")
                continue

            gottop = True
            main_u = list(line)
            continue

        m = re.match(maintrack_lr_re, line)

        if m is None:
            m = re.match(maintrack_ud_re, line)

            if m is None:
                print(f"Failed to parse bottom track line {line}")
                continue

            main_d = list(line)
            continue

        main_r.append(m.group(1))
        main_l.append(m.group(2))

    main_d.reverse()
    main_r.reverse()

    maintrack = main_u[1:] + main_l + main_d + main_r + main_u[0:1]

#print("".join(maintrack))

tracks = {}
with open(sys.argv[2]) as lines:
    for line in lines:
        line = line.rstrip("\n")

        m = re.match(tracks_re, line)

        if m is None:
            print(f"Unable to pares line {line}")
            continue

        name = m.group(1)
        trackstr = m.group(2)

        tracklist = trackstr.split(",")

        tracks[name] = tracklist


def score_track(maintrack, track, p, l):

    score = 0
    tlen = len(track)
    mtlen = len(maintrack)

    for i in range(l * mtlen):
        t_op = maintrack[i % mtlen]

        if t_op == "S" or t_op == "=":
            t_op = track[i % tlen]

        if t_op == '+':
            p += 1
        elif t_op == '-':
            p -= 1
            p = max(p, 0)

        score += p

    return score

scores = {}
for track in tracks:
    scores[track] = score_track(maintrack, tracks[track], 10, 10)
    #print(f"Score for track {track}: {scores[track]}")


ranking = "".join(sorted(tracks.keys(), key = lambda x: scores[x], reverse = True))

print(ranking)
