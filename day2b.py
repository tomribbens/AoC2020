#!/usr/bin/python

# Day 2, part 1 of Advent of Code
# https://adventofcode.com/2020/day/2

import sys
import re

input_array = []
with open(str(sys.argv[1])) as input_file:
    for line in input_file:
        input_array.append(line)

correct = 0

regex = re.compile("(\d+)-(\d+) (.): (.+)")
for i in input_array:
    parts = regex.match(i).groups()
    pos1 = int(parts[0]) - 1
    pos2 = int(parts[1]) - 1

    if (parts[3][pos1] != parts[2] and parts[3][pos2] != parts[2]) or (parts[3][pos1] == parts[2] and parts[3][pos2] == parts[2]):
        continue

    correct += 1

print("There were ", correct, " passwords according to policy")
