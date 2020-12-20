#!/usr/bin/python

# Day 10, part 1 of Advent of Code
# https://adventofcode.com/2020/day/10

import sys
import re
from collections import Counter
import numpy


adapters = [0]

with open(str(sys.argv[1])) as input_file:
    for line in input_file:
        line = line.strip()
        
        adapters.append(int(line))

adapters.append(max(adapters) + 3)
adapters.sort()
options = []

i = 0
while i < len(adapters) - 1:
    options.append(len([x for x in adapters if adapters[i] < x < adapters[i] + 4]))

    i += 1


i = len(options) - 1
previous = []
totaloptions = [1]

while i >= 0:
    if options[i] == 1:
        totaloptions.append(totaloptions[-1])
        i -= 1
    elif options[i] == 2:
        totaloptions.append(totaloptions[-1] + totaloptions[-2])
        i -= 1
    elif options[i] == 3:
        totaloptions.append(totaloptions[-1] + totaloptions[-2] + totaloptions[-3])
        i -= 1

print(totaloptions[-1])
