#!/usr/bin/env python3

import sys

with open("day2.txt", "r") as file:
	state = list(map(int, file.readline().split(",")))

	for noun in range(0, 100):
		for verb in range(0, 100):
			memory = state.copy()
			memory[1] = noun
			memory[2] = verb

			for i in range(0, len(memory), 4):
				if memory[i] == 1:
					memory[memory[i + 3]] = memory[memory[i + 1]] + memory[memory[i + 2]]
				elif memory[i] == 2:
					memory[memory[i + 3]] = memory[memory[i + 1]] * memory[memory[i + 2]]
				else:
					break

			if memory[0] == 19690720:
				print(100 * noun + verb)
				sys.exit()
