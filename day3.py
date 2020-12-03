#!/usr/bin/python

# Day 3, part 1 of Advent of Code
# https://adventofcode.com/2020/day/3

import sys

input_array = []
with open(str(sys.argv[1])) as input_file:
    for line in input_file:
        input_array.append(line)

right = int(sys.argv[2])
down = int(sys.argv[3])
count = 0

map_height = len(input_array)
map_width = len(input_array[0]) - 1

for y, topo in enumerate(input_array):
    if y % down == 0:
        x = (y * right) % map_width
        if topo[x] == "#":
            count += 1


print("On this map, to go right ", right, " and down ", down, " you would hit ", count, " trees.")
