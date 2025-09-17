def is_prime(num: int):
	# maak een array van booleans voor elk getal van 2 tot num of het een deler is van num
	# als er een deler is, return false, anders true
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
	print("geen goldbach gevonden")
	return None


for i in range(4, 1001, 2):
	j, k = goldbach(i)
	print(f"{i} = {j} + {k}")
