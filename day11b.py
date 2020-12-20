#!/usr/bin/python

# Day 11, part 1 of Advent of Code
# https://adventofcode.com/2020/day/11

import sys


def countadjacent(seats, x, y):
    counts = {"." : 0, "L" : 0, "#" : 0}
    directions = [
            [-1, -1], # Left up diagonal
            [-1, 0],  # Straight up
            [-1, 1],  # right up diagonal
            [0, -1],  # Left
            [0, 1],   # Right
            [1, -1],  # Left down diagonal
            [1, 0],   # Down
            [1, 1]   # Right down diagonal
            ]

    for i,j in directions:
        newx = x + i
        newy = y + j
        
        while 0 <= newx < len(seats) and 0 <= newy < len(seats[newx]):
            if seats[newx][newy] == '.':
                newx += i
                newy += j
                continue
            elif seats[newx][newy] == 'L':
                counts['L'] += 1
                break
            elif seats[newx][newy] == '#':
                counts['#'] += 1
                break


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
                if counts['#'] >= 5:
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
