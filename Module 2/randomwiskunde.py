from random import random


result = 0
for i in range(1_000_000):
	randomsum = 0
	while randomsum < 1:
		result += 1
		randomsum += random()

print(f"Het gemiddeld aantal worpen (op basis van 1 miljoen trials) is: {(result / 1_000_000):.4f}")
