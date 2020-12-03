#!/usr/bin/python

# Day 3, part 2 of Advent of Code
# https://adventofcode.com/2020/day/3

import sys

input_array = []
with open(str(sys.argv[1])) as input_file:
    for line in input_file:
        input_array.append(line)

slopes = [[1,1],[3, 1], [5, 1], [7, 1], [1, 2]]
count = 0
multiplication = 1

map_height = len(input_array)
map_width = len(input_array[0]) - 1

for slope in slopes:
    right = slope[0]
    down = slope[1]

    for y, topo in enumerate(input_array):
        if y % down == 0:
            x = (y * right) % map_width
            if topo[x] == "#":
                count += 1

    multiplication *= count
    count = 0


print("Multiplication:", multiplication)
