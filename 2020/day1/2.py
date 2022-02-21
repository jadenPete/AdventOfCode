#!/usr/bin/env python

with open("input.txt") as file:
	entries = list(sorted(map(int, file.readlines())))

for i, e1 in enumerate(entries):
	for j, e2 in enumerate(entries):
		if i == j:
			break

		for k, e3 in enumerate(entries):
			if i != k and j != k and e1 + e2 + e3 == 2020:
				print(e1 * e2 * e3)
				exit()
