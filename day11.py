#!/usr/bin/python

# Day 11, part 1 of Advent of Code
# https://adventofcode.com/2020/day/11

import sys


def countadjacent(seats, x, y):
    counts = {"." : 0, "L" : 0, "#" : 0}
    for i, j in [[x - 1, y - 1],[x - 1, y],[x - 1, y + 1],[x, y - 1],[x, y + 1], [x + 1, y - 1], [x + 1, y], [x + 1, y + 1]]:
        if i < 0 or j < 0:
            continue
        elif i >= len(seats):
            continue
        elif j >= len(seats[i]):
            continue
        elif seats[i][j] == ".":
            counts["."] += 1
        elif seats[i][j] == "L":
            counts["L"] += 1
        elif seats[i][j] == "#":
            counts["#"] += 1

    return counts






def seating(seats):
    newseats = []
    i = 0

    while i < len(seats):
        j = 0
        newrow = []
        while j < len(seats[i]):
            counts = countadjacent(seats, i, j)

            if seats[i][j] == '.':
                newrow.append('.')
            elif seats[i][j] == 'L':
                if counts["#"] == 0:
                    newrow.append('#')
                else:
                    newrow.append('L')
            elif seats[i][j] == '#':
                if counts['#'] >= 4:
                    newrow.append('L')
                else:
                    newrow.append('#')
            j += 1
        
        newseats.append(newrow)
        i += 1


    return newseats








seats = []

with open(str(sys.argv[1])) as input_file:
    for line in input_file:
        line = line.strip()
        
        seats.append(list(line))
         

newseats = seating(seats)

while newseats != seats:
    seats = newseats
    del newseats
    newseats = seating(seats)

taken = 0
for line in seats:
    for seat in line:
        if seat == '#':
            taken += 1

print(taken)
