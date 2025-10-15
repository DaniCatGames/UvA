from random import random
import matplotlib.pyplot as plt


N = 100_000


def montecarlo(func, x1, y1, x2, y2):
	correct = 0
	xrange = x2 - x1
	yrange = y2 - y1
	
	for i in range(N):
		x = random() * xrange + x1
		y = random() * yrange + y1
		if 0 < y < func(x):
			correct += 1
			plt.plot(x, y, "go")
		elif 0 > y > func(x):
			correct -= 1
			plt.plot(x, y, "bo")
		else:
			plt.plot(x, y, "ro")
			
	plt.show()
	return (correct / N) * xrange * yrange
