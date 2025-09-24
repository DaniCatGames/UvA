import matplotlib.pyplot as plt
import numpy


def f(x):
	return x ** x


x_coords = numpy.arange(0, 1.5, 0.01)
y_coords = []
min_x, min_y = 0, f(0)
for x in x_coords:
	y = f(x)
	y_coords.append(y)
	if y < min_y:
		min_y = y
		min_x = x
print(f"(xmin, ymin) = ({min_x}, {min_y:.2f})")

plt.plot(x_coords, y_coords, 'g-')
plt.plot(min_x, min_y, 'ro')
plt.text(0.2, 1.0, f"(xmin, ymin) = ({min_x}, {min_y:.2f})")
plt.show()
