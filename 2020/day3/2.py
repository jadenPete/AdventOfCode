#!/usr/bin/env python

with open("input.txt") as file:
	lines = file.readlines()


for i in range(len(lines)):
	lines[i] = lines[i][:-1]

def trees(delta_y, delta_x):
	y, x = 0, 0
	count = 0

	while y < len(lines):
		if lines[y][x % len(lines[0])] == "#":
			count += 1

		y += delta_y
		x += delta_x

	return count

print(trees(1, 1) * trees(1, 3) * trees(1, 5) * trees(1, 7) * trees(2, 1))
