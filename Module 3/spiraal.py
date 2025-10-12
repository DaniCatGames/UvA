import matplotlib.pyplot as plt
import numpy

plt.figure()
ax = plt.gca()

ax.set_aspect('equal')

ax.set_xlim(-12, 12)
ax.set_ylim(-12, 12)

ax.grid(True, alpha=0.3)

alpha = 0
while alpha <= 20:
	R = 10 - 0.5 * alpha

	x = R * numpy.cos(alpha)
	y = R * numpy.sin(alpha)

	ax.set_xlim(-12, 12)
	ax.set_ylim(-12, 12)
	ax.set_aspect('equal')
	ax.grid(True, alpha=0.3)

	ax.plot(x, y, 'ro', markersize=10)

	ax.set_title(f'Spiraal: α = {alpha:.1f} rad, R = {R:.1f}')

	plt.pause(0.05)
	alpha += 0.1

plt.show()
