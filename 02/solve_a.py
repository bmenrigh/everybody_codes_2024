#!/usr/bin/python3

import sys
import re

words_re = re.compile(r'^WORDS:(\S+)\s*$')


def find_all_word_offsets(s, w):

    o = 0
    while o >= 0 and o < len(s):
        o = s.find(w, o)

        if o < 0:
            return

        yield o

        o += 1

count = 0
with open(sys.argv[1]) as lines:
    gotwords = False
    words = None
    for line in lines:
        line = line.rstrip("\n")

        if not gotwords:

            m = re.match(words_re, line)

            if m is not None:
                words = m.group(1).split(",")
                gotwords = True
                continue

        if gotwords:
            for w in words:
                count += len(list(find_all_word_offsets(line, w)))

print(count)
