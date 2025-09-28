import math

import matplotlib.pyplot as plt
import numpy


def f(x):
	return x ** 2 + 2 * x - 10


def nulpunten(a, b, c):
	D = b ** 2 - 4 * a * c
	if D == 0:
		return [(-b) / (2 * a)]
	elif D < 0:
		return []
	elif D > 0:
		return [(-b + math.sqrt(D)) / (2 * a), (-b - math.sqrt(D)) / (2 * a)]


x_coords = numpy.arange(-6, 5, 0.01)
y_coords = []

for x in numpy.arange(-6, 5, 0.01):
	y_coords.append(f(x))

plt.plot(x_coords, y_coords, "b-")
plt.plot(nulpunten(1, 2, -10)[0], f(nulpunten(1, 2, -10)[0]), "ro")
plt.plot(nulpunten(1, 2, -10)[1], f(nulpunten(1, 2, -10)[1]), "ro")
plt.show()
