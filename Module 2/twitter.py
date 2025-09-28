from random import random

import matplotlib.pyplot as plt


N = 100_000


def twitter():
	x1 = -0.5
	y1 = -0.4
	x2 = 0.5
	y2 = 1.0
	func = lambda x, y: (x ** 2 + y ** 2) ** 0.5 + 2 / 3 * (
			x ** 2 + (5 / 6 - y) ** 2) ** 0.5

	ax = plt.gca()
	ax.set_aspect('equal', adjustable='box')

	green = 0
	xrange = x2 - x1
	yrange = y2 - y1
	for i in range(N):
		x = random() * xrange + x1
		y = random() * yrange + y1
		if func(x, y) < 1:
			green += 1
			plt.plot(x, y, 'go')
		else:
			plt.plot(x, y, 'ro')

	plt.show()
	return (green / N) * xrange * yrange


twitter()
