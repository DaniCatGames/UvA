import random

primes = [2]


def is_prime(num: int):
	return not any(num % x == 0 for x in range(2, num))


def generate_new_prime():
	i = 2
	if len(primes) > 0: i = primes[-1] + 1
	while True:
		if is_prime(i):
			primes.append(i)
			return i
		i += 1


def get_prime(iteration: int):
	if len(primes) > iteration:
		return primes[iteration]
	return generate_new_prime()


def factor(num: int):
	factors = []
	iteration = 0
	while num != 1:
		i = get_prime(iteration)
		while (num / i) % 1 == 0:
			num /= i
			factors.append(i)
		iteration += 1
	return factors


def divisors(a: int, b: int):
	factors_a = factor(a)
	factors_b = factor(b)

	divisors_num = 0

	for i in factors_a:
		if i in factors_b:
			divisors_num += 1

	return divisors_num


def experiment():
	iterations = 0
	shared = 0

	for i in range(1, 10000):
		a = random.randint(10000, 100000)
		b = random.randint(10000, 100000)
		if divisors(a, b) != 0: shared += 1
		iterations += 1

	return 1 - shared / iterations  # geen gemeenschappelijke deler


def voorspelling():
	return 0.608


print("De kans dat twee random getallen geen gemeenschappelijke deler hebben is:")
print(f"\t - voorspelling (wiskunde): {str(voorspelling())}")
print(f"\t - empirisch (Python): {experiment():.3f}")
