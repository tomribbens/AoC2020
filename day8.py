#!/usr/bin/python

# Day 8, part 1 of Advent of Code
# https://adventofcode.com/2020/day/8

import sys
import re

program = []

with open(str(sys.argv[1])) as input_file:
    for line in input_file:
        line = line.strip()
        
        program.append({ 
            "opcode" : line[:3],
            "argument" : line[4:],
            "loop" : False
            })


pointer = 0
accumulator = 0

while program[pointer]["loop"] == False:
    program[pointer]["loop"] = True

    if program[pointer]["opcode"] == "nop": 
        pointer += 1
        continue
    elif program[pointer]["opcode"] == "acc":
        accumulator += int(program[pointer]["argument"])
        pointer += 1
        continue
    elif program[pointer]["opcode"] == "jmp":
        pointer += int(program[pointer]["argument"])
        continue
    else:
        print("Something went wrong, not supposed to hit this")


print("Accumulator: ", accumulator)


