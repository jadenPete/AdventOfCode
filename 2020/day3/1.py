#!/usr/bin/env python

with open("input.txt") as file:
	lines = file.readlines()


for i in range(len(lines)):
	lines[i] = lines[i][:-1]

y, x = 0, 0
count = 0

while y < len(lines):
	if lines[y][x % len(lines[0])] == "#":
		count += 1

	y += 1
	x += 3

print(count)
