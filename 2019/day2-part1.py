#!/usr/bin/env python3

with open("day2.txt", "r") as file:
	state = list(map(int, file.readline().split(",")))
	state[1] = 12
	state[2] = 2

	for i in range(0, len(state), 4):
		if state[i] == 1:
			state[state[i + 3]] = state[state[i + 1]] + state[state[i + 2]]
		elif state[i] == 2:
			state[state[i + 3]] = state[state[i + 1]] * state[state[i + 2]]
		else:
			break

	print(state[0])
