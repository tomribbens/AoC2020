#!/usr/bin/python

# Day 1, part 1 of Advent of Code
# https://adventofcode.com/2020/day/1

import sys

input_array = []
with open(str(sys.argv[1])) as input_file:
    for line in input_file:
        input_array.append(int(line))

for i in input_array:
    for j in input_array:
        try:
            number3 = input_array[input_array.index(2020-i-j)]
        except ValueError:
            continue
    
        number1 = i
        number2 = j

print("The three values that sum up to 2020 are", number1,", ", number2, " and ", number3, " which multiply to ", number1 * number2 * number3)

