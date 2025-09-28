from random import random

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('Agg')


def som_random_getallen():
	sums = []
	for i in range(10_000):
		randomsum = 0
		for i in range(100):
			randomsum += random()
		sums.append(randomsum)

	under40 = 0
	over60 = 0
	for i in sums:
		if i < 40:
			under40 += 1
		if i > 60:
			over60 += 1

	plt.xlim(30, 70)
	plt.hist(sums, bins=40)
	plt.savefig('histogram.png')
	print(f"under40 = {under40 / 10_000 * 100}")
	print(f"over60 = {over60 / 10_000 * 100}")


som_random_getallen()
