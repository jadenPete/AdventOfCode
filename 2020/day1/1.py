#!/usr/bin/env python

with open("input.txt") as file:
	entries = list(sorted(map(int, file.readlines())))

for i, e1 in enumerate(entries):
	for j, e2 in enumerate(entries):
		if i != j and e1 + e2 == 2020:
			print(e1 * e2)
			exit()
