#!/usr/bin/env python3


with open("day3.txt", "r") as file:
	def crawl_wire():
		loc = [0, 0]
		steps = 0

		for move in file.readline().split(","):
			delta = {"L": (0, -1), "R": (0, 1), "U": (1, 1), "D": (1, -1)}[move[0]]

			for _ in range(int(move[1:])):
				loc[delta[0]] += delta[1]
				steps += 1

				yield tuple(loc), steps

	visited = {}

	for loc, steps in crawl_wire():
		if loc not in visited:
			visited[loc] = steps

	print(min(steps + visited[loc] for loc, steps in crawl_wire() if loc in visited))
