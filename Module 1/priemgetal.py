def priem_of_niet(num: int):
	# maak een array van booleans voor elk getal van 2 tot num of het een deler is van num
	# als er een deler is, return false, anders true
	return not any(num % x == 0 for x in range(2, num))


def alle_priem_tot(num: int):
	for i in range(1, num):
		if priem_of_niet(i):
			print(i)


def zoveelste_priem(num: int):
	if num < 0:
		return 2
	primes_encountered: int = 0
	n: int = 1
	while True:
		if priem_of_niet(n):
			if primes_encountered == num:
				return n
			primes_encountered += 1
		n += 1


num = int(input())
print(zoveelste_priem(num))
