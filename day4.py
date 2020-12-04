#!/usr/bin/python

# Day 4, part 1 of Advent of Code
# https://adventofcode.com/2020/day/3

import sys

passports = []
i = 0
passports.append({})
with open(str(sys.argv[1])) as input_file:
    for line in input_file:
        line = line.strip()
        if line == "": 
            i += 1
            passports.append({})
            continue

        passports[i].update(dict(x.split(":") for x in line.split(" ")))

validPassport = 0
requiredFields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

for passport in passports:
    if not all ( k in passport for k in requiredFields): continue
    validPassport += 1

print("Valid passports: ", validPassport)
