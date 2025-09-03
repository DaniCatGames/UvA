def priem_of_niet(num: int):
	return not any(num % x == 0 for x in range(2, num))


def alle_priems(num: int):
	return


def reeks_niet_priem(num: int):
	start, end, size = 0, 0, 0
	for i in range(1, num):
		newStart, newEnd, newSize = range_not_prime(i, num)
		if newSize > size:
			start, end, size = newStart, newEnd, newSize
	print(
		f"De langste reeks niet-priemgetallen onder de 10,000 begint op {start} en eindigt bij {end}")
	print(f"De reeks is {size} lang.")


def range_not_prime(start: int, end: int):
	current: int = start
	while not priem_of_niet(current) and current < end:
		current += 1
	return start, current - 1, current - start


reeks_niet_priem(10000)
