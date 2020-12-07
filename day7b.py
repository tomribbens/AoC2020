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


def count_bags(bag, data):
    total = 1

    for i in data[bag].split(', '):
        amount, containedbag = i.split(' ', 1)

        if amount == "no":
            continue
        else:
            containedlist = containedbag.split(' ')
            containedbag = ' '.join(containedlist[0:2])
            total += int(amount) * count_bags(containedbag.strip(),data)

    return total



containedin = defaultdict(list)
containing = defaultdict(list)

with open(str(sys.argv[1])) as input_file:
    for line in input_file:
        line = line.strip()

        linelist = line.split(' contain ')
        containing[linelist[0][:-5]] = linelist[1]

bag = 'shiny gold'
#import pdb; pdb.set_trace()
print("You need ", count_bags(bag, containing) - 1, "bags")
