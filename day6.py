#!/usr/bin/python

# Day 6, part 1 of Advent of Code
# https://adventofcode.com/2020/day/6

import sys

groups = []
i = 0
groups.append('')
with open(str(sys.argv[1])) as input_file:
    for line in input_file:
        line = line.strip()
        if line == "": 
            i += 1
            groups.append('')
            continue
        groups[i] += line

total = 0
for group in groups:
    total += len(set(group))


print("Total: ", total)


