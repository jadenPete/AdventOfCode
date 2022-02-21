#!/usr/bin/env python

import re

rules = {
	"byr": lambda v: re.match(r"\d{4}$", v) and 1920 <= int(v) <= 2002,
	"iyr": lambda v: re.match(r"\d{4}$", v) and 2010 <= int(v) <= 2020,
	"eyr": lambda v: re.match(r"\d{4}$", v) and 2020 <= int(v) <= 2030,
	"hgt": lambda v: re.match(r"\d+(?:cm|in)$", v) and ((150 <= int(v[:-2]) <= 193) if v[-2:] == "cm" else (59 <= int(v[:-2]) <= 76)),
	"hcl": lambda v: re.match(r"#[0-9a-f]{6}$", v),
	"ecl": lambda v: v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
	"pid": lambda v: re.match(r"\d{9}$", v)
}

valid = 0

with open("input.txt") as file:
	for passport in file.read().split("\n\n"):
		present_fields = set()

		for field in passport.replace("\n", " ").split():
			key, value = field.split(":")
			
			if key in rules and rules[key](value):
				present_fields.add(key)
		
		if {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}.issubset(present_fields):
			valid += 1

print(valid)
