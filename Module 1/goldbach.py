def is_prime(num: int):
	return not any(num % x == 0 for x in range(2, num))


primes = []

for i in range(2, 1001):
	if is_prime(i):
		primes.append(i)


def goldbach(num: int):
	for i in primes:
		for j in primes:
			if j > i:
				break
			if i + j == num:
				return i, j


for i in range(4, 1001, 2):
	j, k = goldbach(i)
	print(f"{i} = {j} + {k}")
