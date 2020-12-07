#!/usr/bin/python

# Day 7, part 1 of Advent of Code
# https://adventofcode.com/2020/day/6

import sys
import re
from collections import defaultdict

def give_parents(key, data):
    parents = []
    for i in data[key]:
        parents.append(i)
        parents += give_parents(i, data)
    return parents

containedin = defaultdict(list)

with open(str(sys.argv[1])) as input_file:
    for line in input_file:
        line = line.strip()

        linelist = line.split(' contain ')
        for inside in linelist[1].split(', '):
            if inside == "no other bags.":
                continue
            contents = inside[2:].split()
            containedin[contents[0] + " " + contents[1]].append(linelist[0][:-5])


print(len(set(give_parents('shiny gold', containedin))))
