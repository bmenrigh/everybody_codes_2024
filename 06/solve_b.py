#!/usr/bin/python3

import sys
import re

nodel_re = re.compile(r'^([A-Z]+):([A-Z@,]+)$')

tree = {}
with open(sys.argv[1]) as lines:
    for line in lines:
        line = line.rstrip("\n")

        m = re.match(nodel_re, line)

        if m is None:
            print(f"Unable to parse line {line}")
            continue

        node, ls = m.group(1), m.group(2)

        l = ls.split(",")

        tree[node] = l


def paths_to_apples(tree):

    paths_list = {}
    short_paths_list = {}

    def path_rec(node, d, pl):

        if not node in tree:
            return

        for nn in tree[node]:
            if nn != '@':
                path_rec(nn, d + 1, pl + [nn])
            else:
                pstr = "".join(pl + [nn])
                short_pstr = "".join(list(map(lambda x: x[0], pl + [nn])))
                #print(f"Adding length {d} path {pstr}")
                paths_list[pstr] = d
                short_paths_list[short_pstr] = d

    path_rec('RR', 0, ['RR'])

    uniq_dist = {}

    for _, v in paths_list.items():
        uniq_dist[v] = uniq_dist.get(v, 0) + 1

    for d in uniq_dist:
        if uniq_dist[d] == 1:
            for p, v in short_paths_list.items():
                if v == d:
                    print(f"Unique apple path: {p}")

paths_to_apples(tree)
