def riemann(func, a, b, N):
	if b < a: return None

	dx = (b - a) / N
	result = 0

	for i in range(N):
		left = func(a + i * dx)
		right = func(a + (i + 1) * dx)
		result += (right + left) / 2 * dx

	return result


print(riemann(lambda x: x ** 2, 0, 1, 1000))
