def is_prime(num: int):
	return not any(num % x == 0 for x in range(2, num))


def all_primes_until_int(num: int):
	for i in range(1, num):
		if is_prime(i):
			print(i)


def nth_prime(num: int):
	if num < 0:
		return 2
	primes_encountered: int = 0
	n: int = 1
	while True:
		if is_prime(n):
			if primes_encountered == num:
				return n
			primes_encountered += 1
		n += 1


def priem_of_niet(N: int):
	return is_prime(N)


def alle_priem_tot(N: int):
	all_primes_until_int(N)


def zoveelste_priem(N: int):
	return nth_prime(N)


num = int(input())
print(nth_prime(num))
