#!/usr/bin/python

# Day 4, part 1 of Advent of Code
# https://adventofcode.com/2020/day/3

import sys
import re

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
    if not (int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002): continue
    if not (int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020): continue
    if not (int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030): continue
    if not passport['ecl'] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"): continue
    if not re.fullmatch("#[0-9a-f]{6}", passport['hcl']): continue
    if not re.fullmatch("\d{9}", passport['pid']): continue
    if not re.fullmatch("(\d{2,3})(cm|in)", passport['hgt']): continue

    height = re.match("^(\d{2,3})(cm|in)$", passport['hgt']).groups()
    if height[1] == "in":
        if not (int(height[0]) >= 59 and int(height[0]) <= 76): continue
    if height[1] == "cm":
        if not (int(height[0]) >= 150 and int(height[0]) <= 193): continue
    
    print(passport)
    validPassport += 1


print("Valid passports: ", validPassport)
