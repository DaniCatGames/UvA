from random import random

import matplotlib.pyplot as plt


N = 100_000


def montecarlo(func, x1, y1, x2, y2):
	pos = 0
	neg = 0
	xrange = x2 - x1
	yrange = y2 - y1
	for i in range(N):
		x = random() * xrange + x1
		y = random() * yrange + y1
		if 0 < y < func(x):
			pos += 1
			plt.plot(x, y, "go")
		elif 0 > y > func(x):
			neg += 1
			plt.plot(x, y, "bo")
		else:
			plt.plot(x, y, "ro")
	plt.show()
	return ((pos - neg) / N) * xrange * yrange
