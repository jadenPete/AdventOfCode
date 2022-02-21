#!/usr/bin/env python

with open("input.txt") as file:
	i = 0	
	
	for line in file:
		times, char, password = line.split()
		
		min_, max_ = map(int, times.split("-"))
		char = char[:-1]

		if min_ <= password.count(char) <= max_:
			i += 1

print(i)
		
