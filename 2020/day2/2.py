#!/usr/bin/env python

with open("input.txt") as file:
	n = 0
	
	for line in file:
		times, char, password = line.split()
		
		i, j = map(int, times.split("-"))
		char = char[:-1]

		if (password[i - 1] == char) != (password[j - 1] == char):
			n += 1

print(n)
		
