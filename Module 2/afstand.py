from random import random


def vierkant(N):
	distance = 0
	for i in range(N):
		x1 = random()
		y1 = random()
		x2 = random()
		y2 = random()
		distance += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
	return distance / N
