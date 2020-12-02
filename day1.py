#!/usr/bin/python

# Day 1, part 1 of Advent of Code
# https://adventofcode.com/2020/day/1

import sys

input_array = []
with open(str(sys.argv[1])) as input_file:
    for line in input_file:
        input_array.append(int(line))

for i in input_array:
    try:
        number2 = input_array[input_array.index(2020-i)]
    except ValueError:
        continue
    
    number1 = i

print("The two values that sum up to 2020 are", number1, " and ", number2, " which multiply to ", number1 * number2)

