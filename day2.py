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
    # print("Input line:", i)
    parts = regex.match(i).groups()
    # print("Parts: ", parts)
    num_char = parts[3].count(parts[2])
    # print("Times character appears: ", num_char)

    if num_char >= int(parts[0]) and num_char <= int(parts[1]):
        correct += 1

print("There were ", correct, " passwords according to policy")
