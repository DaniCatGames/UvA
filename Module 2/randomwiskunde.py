from random import random


def randomwiskunde():
	result = 0
	for i in range(1_000_000):
		randomsum = 0
		tries = 0
		while randomsum < 1:
			tries += 1
			randomsum += random()
		result += tries
	print(f"Het gemiddeld aantal worpen (op basis van 1 miljoen trials) is: {(result / 1_000_000):.4f}")


randomwiskunde()
