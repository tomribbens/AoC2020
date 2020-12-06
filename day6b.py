#!/usr/bin/python

# Day 6, part 2 of Advent of Code
# https://adventofcode.com/2020/day/6

import sys

total = 0
answers = ""
reset = True
with open(str(sys.argv[1])) as input_file:
    for line in input_file:
        line = line.strip()
        if line == "": 
            total += len(answers)
            reset = True
            continue

        if reset:
            answers = line
            reset = False
        else:
            toRemove = ''
            for char in answers:
                index = line.find(char)
                if index == -1:
                    toRemove += char

            translation_table = dict.fromkeys(map(ord, toRemove), None)
            answers = answers.translate(translation_table)

    total += len(answers)
            
            





print("Total: ", total)


