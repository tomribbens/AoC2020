#!/usr/bin/python

# Day 9, part 1 of Advent of Code
# https://adventofcode.com/2020/day/8

import sys
import re

encoding_length = 25

encoding = []

with open(str(sys.argv[1])) as input_file:
    for line in input_file:
        line = line.strip()
        
        encoding.append(int(line))


i = encoding_length
invalid = 0

while i < len(encoding):
    valid = False

    j = i - encoding_length

    while j < i:
        k = j + 1
        while k < i:
            if encoding[j] + encoding[k] == encoding[i]:
                valid = True

            k += 1

        j += 1

    if not valid:
        invalid = encoding[i]
        break

    i += 1
    

i = 0
j = 0

while i < len(encoding):
    j = i
    accumulator = 0

    while accumulator < invalid and j < len(encoding):
        accumulator += encoding[j]

        j += 1

    if accumulator == invalid:
        break

    i += 1

print(max(encoding[i:j+1]) + min(encoding[i:j+1]))
