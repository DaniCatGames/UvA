def appel():
	g = 9.81
	dt = 0.01

	x = 100
	v = 0
	t = 0

	tijd_100kmh = None

	while x > 0:
		a = g

		v_nieuw = v + a * dt

		if tijd_100kmh is None and v_nieuw >= 100 / 3.6:
			tijd_100kmh = t

		x_nieuw = x - v_nieuw * dt

		v = v_nieuw
		x = x_nieuw
		t = t + dt

	snelheid_grond_kmh = v * 3.6

	print(f"{t:.2f} s tot de appel de grond raakt")
	print(
		f"{snelheid_grond_kmh:.1f} km/uur is de snelheid waarmee de appel de grond raakt")
	print(f"{tijd_100kmh:.2f} s duurt het tot de appel 100 km/uur gaat")


appel()
