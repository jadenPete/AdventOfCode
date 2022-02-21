#!/usr/bin/env python

with open("input.txt") as file:
	valid = 0

	for passport in file.read().split("\n\n"):
		current_fields = {field.split(":")[0] for field in passport.replace("\n", " ").split()}

		if {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}.issubset(current_fields):
			valid += 1

print(valid)
