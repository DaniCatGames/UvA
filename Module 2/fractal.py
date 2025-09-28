import matplotlib.colors as mcolors
import matplotlib.pyplot as plt

rmin = -2.
rmax = 1.
imin = -1.5
imax = 1.5
max_iterations = 400

colors = ['black', 'blue', 'white']
cmap = mcolors.LinearSegmentedColormap.from_list('fractalcolors', colors, N=100)


# Helper functions
def square(real, imaginary):
	return real ** 2 - imaginary ** 2, 2 * real * imaginary


def f(real, imaginary, rstart, istart):
	return square(real, imaginary)[0] + rstart, square(real, imaginary)[1] + istart


def fractal():
	ax = plt.gca()
	ax.set_aspect('equal', adjustable='box')

	rdots = []
	idots = []
	iterations = []

	# loop for every pixel
	for i in range(500):
		real = i * (rmax - rmin) / 500 + rmin
		for i in range(500):
			imaginary = i * (imax - imin) / 500 + imin
			iterations_to_blow_up = 0
			rtemp = real
			itemp = imaginary

			# loop until value has exploded
			while abs(rtemp) < 1e50 and abs(itemp) < 1e50:
				rtemp, itemp = f(rtemp, itemp, real, imaginary)
				iterations_to_blow_up += 1
				if iterations_to_blow_up > max_iterations:
					iterations_to_blow_up = 0
					break

			rdots.append(real)
			idots.append(imaginary)
			iterations.append(iterations_to_blow_up)

	norm = mcolors.PowerNorm(gamma=0.35)  # scale colors

	plt.scatter(rdots, idots, c=iterations, cmap=cmap, norm=norm)
	plt.show()


fractal()
