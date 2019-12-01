#!/usr/bin/env python3

with open("day1.txt", "r") as file:
	print(sum(mass // 3 - 2 for mass in map(int, file)))
