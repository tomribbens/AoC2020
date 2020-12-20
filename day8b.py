#!/usr/bin/python

# Day 8, part 1 of Advent of Code
# https://adventofcode.com/2020/day/8

import sys
import re
import copy

program = []

with open(str(sys.argv[1])) as input_file:
    for line in input_file:
        line = line.strip()
        
        program.append({ 
            "opcode" : line[:3],
            "argument" : int(line[4:]),
            "loop" : False
            })


pointer = 0
changepointer = 0
accumulator = 0
termination = len(program)

while changepointer < termination:
    changedprogram = copy.deepcopy(program)
    if changedprogram[changepointer]["opcode"] == "jmp":
        changedprogram[changepointer]["opcode"] = "nop"
    elif changedprogram[changepointer]["opcode"] == "nop":
        changedprogram[changepointer]["opcode"] = "jmp"
    else:
        changepointer += 1
        continue
    
    pointer = 0
    accumulator = 0

    while pointer < termination and changedprogram[pointer]["loop"] == False:
        changedprogram[pointer]["loop"] = True

        if changedprogram[pointer]["opcode"] == "nop": 
            pointer += 1
            continue
        elif changedprogram[pointer]["opcode"] == "acc":
            accumulator += changedprogram[pointer]["argument"]
            pointer += 1
            continue
        elif changedprogram[pointer]["opcode"] == "jmp":
            pointer += changedprogram[pointer]["argument"]
            continue
        else:
            print("Something went wrong, not supposed to hit this")

    if pointer == termination:
        break
    else:
        changepointer += 1


print("Accumulator: ", accumulator)
