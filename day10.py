#!/usr/bin/python

# Day 10, part 1 of Advent of Code
# https://adventofcode.com/2020/day/10

import sys
import re
from collections import Counter


adapters = [0]

with open(str(sys.argv[1])) as input_file:
    for line in input_file:
        line = line.strip()
        
        adapters.append(int(line))


adapters.sort()
differences = []

i = 1
while i < len(adapters):
    differences.append(adapters[i] - adapters [i - 1])
    i += 1

# Add one more for the difference from the origin, and one for the final device
differences.append(3)

difference_counts = Counter(differences)


print(difference_counts[1] * difference_counts[3])
