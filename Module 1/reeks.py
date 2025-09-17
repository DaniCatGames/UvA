def priem_of_niet(num: int):
	# maak een array van booleans voor elk getal van 2 tot num of het een deler is van num
	# als er een deler is, return false, anders true
	return not any(num % x == 0 for x in range(2, num))


def alle_priems(num: int):
	return


def reeks_niet_priem(num: int):
	start, end, size = 0, 0, 0
	for i in range(1, num):
		# zoek hoelang de reeks vanaf i is
		new_start, new_end, new_size = range_not_prime_from_x_to_y(i, num)
		if new_size > size:
			# als de reeks langer is, zet de current streak naar de nieuwe reeks
			start, end, size = new_start, new_end, new_size
	print(
		f"De langste reeks niet-priemgetallen onder de 10,000 begint op {start} en eindigt bij {end}")
	print(f"De reeks is {size} lang.")


# Zoek hoelang de reeks de reeks niet priemgetallen vanaf x tot y is
def range_not_prime_from_x_to_y(start: int, end: int):
	current: int = start
	while not priem_of_niet(current) and current < end:
		current += 1
	return start, current - 1, current - start


reeks_niet_priem(10000)
