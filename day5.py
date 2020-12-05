#!/usr/bin/python

# Day 5, part 1 of Advent of Code
# https://adventofcode.com/2020/day/1

import sys

boarding_passes = []
maxseatid = 0
with open(str(sys.argv[1])) as input_file:
    for line in input_file:
        line = line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
        row = int(line[0:7], 2)
        column = int(line[7:10], 2)
        seatid = (row * 8) + column
        boarding_passes.append({
            "row": row,
            "column": column,
            "seatid": seatid
 
        })

        if seatid > maxseatid:
            maxseatid = seatid


print("Highest Seat ID is: ", maxseatid)

        



