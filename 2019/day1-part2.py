#!/usr/bin/env python3

with open("day1.txt", "r") as file:
	total = 0

	for mass in map(int, file):
		fuel = mass // 3 - 2

		while fuel > 0:
			total += fuel
			fuel = fuel // 3 - 2

	print(total)
