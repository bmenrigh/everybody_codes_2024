#!/usr/bin/python3

import sys
import re
import math

tracks_re = re.compile(r'^([A-Z]+):([,+=-]+)$')


def unwind_maintrack(mtg):

    mt = []

    h = len(mtg)
    w = len(mtg[0])

    def unwind_rec(cx, cy, px, py):

        if any([cx < 0, cx >= w, cy < 0, cy >= h]):
            return

        if mtg[cy][cx] in "+-=S":
            mt.append(mtg[cy][cx])
        else:
            return

        if mtg[cy][cx] == 'S':
            return

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

            nx, ny = cx + dx, cy + dy

            if nx == px and ny == py:
                continue

            unwind_rec(nx, ny, cx, cy)


    unwind_rec(1, 0, 0, 0)

    return mt


def printgrid(mtg):

    h = len(mtg)
    w = len(mtg[0])

    for y in range(h):
        for x in range(w):
            print(mtg[y][x], end="")
        print("")

def pad_grid(mtg):

    mlen = max([len(x) for x in mtg])

    for x in mtg:
        if len(x) < mlen:
            x.extend([' '] * (mlen - len(x)))


maintrackgrid = []
with open(sys.argv[1]) as lines:

    for line in lines:
        line = line.rstrip("\n")

        if line == "":
            continue

        maintrackgrid.append(list(line))

pad_grid(maintrackgrid)
#printgrid(maintrackgrid)
maintrack = unwind_maintrack(maintrackgrid)

#print(maintrack)


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


def score_track(maintrack, track, p):

    score = 0
    tlen = len(track)
    mtlen = len(maintrack)

    for i in range(math.lcm(tlen, mtlen)):
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


def count_all_tracks(maintrack, best, p, m, e, l):

    better = 0

    def make_track_rec(cp, cm, ce, cl, track):

        nonlocal better

        if cl >= l:
            #print(f'Made track {"".join(track)}')
            score = score_track(maintrack, track, 10)

            if score > best:
                better += 1

            return

        if cp < p:
            make_track_rec(cp + 1, cm, ce, cl + 1, track + ['+'])

        if cm < m:
            make_track_rec(cp, cm + 1, ce, cl + 1, track + ['-'])

        if ce < e:
            make_track_rec(cp, cm, ce + 1, cl + 1, track + ['='])

    make_track_rec(0, 0, 0, 0, [])

    return better


scores = {}
for track in tracks:
    scores[track] = score_track(maintrack, tracks[track], 10)
    #print(f"Score for track {track}: {scores[track]}")

bestscore = max([scores[x] for x in scores])

print(f"Best score to beat: {bestscore}")

better = count_all_tracks(maintrack, bestscore, 5, 3, 3, 11)

print(f"Better scoring tracks: {better}")

#ranking = "".join(sorted(tracks.keys(), key = lambda x: scores[x], reverse = True))

#print(ranking)
