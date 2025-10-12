import matplotlib.pyplot as plt


def basejump():
	g = 9.81
	m = 72
	h_start = 828
	h_parachute = 100
	dt = 0.01
	k = 0.24

	t_met = [0]
	v_met = [0]
	h_met = [h_start]

	t_zonder = [0]
	v_zonder = [0]
	h_zonder = [h_start]

	tijd_parachute_met = None
	while h_met[-1] > h_parachute:
		v_huidig = v_met[-1]
		a = g - (k * v_huidig ** 2) / m
		v_nieuw = v_huidig + a * dt
		h_nieuw = h_met[-1] - v_nieuw * dt
		t_nieuw = t_met[-1] + dt

		v_met.append(v_nieuw)
		h_met.append(h_nieuw)
		t_met.append(t_nieuw)

	tijd_parachute_met = t_met[-1]

	while h_zonder[-1] > h_parachute:
		v_huidig = v_zonder[-1]
		a = g
		v_nieuw = v_huidig + a * dt
		h_nieuw = h_zonder[-1] - v_nieuw * dt
		t_nieuw = t_zonder[-1] + dt

		v_zonder.append(v_nieuw)
		h_zonder.append(h_nieuw)
		t_zonder.append(t_nieuw)

	tijd_parachute_zonder = t_zonder[-1]

	plt.figure(figsize=(12, 5))

	plt.subplot(1, 2, 1)
	v_met_kmh = [v * 3.6 for v in v_met]
	plt.plot(t_met, v_met_kmh, 'b-', linewidth=2)
	plt.xlabel('tijd (s)')
	plt.ylabel('v (km/u)')
	plt.title('Snelheid als functie van tijd (met luchtweerstand)')
	plt.grid(True, alpha=0.3)

	plt.subplot(1, 2, 2)
	plt.plot(t_zonder, h_zonder, 'g-', linewidth=2, label='zonder luchtweerstand')
	plt.plot(t_met, h_met, 'b-', linewidth=2, label='met luchtweerstand')
	plt.xlabel('tijd (s)')
	plt.ylabel('hoogte (m)')
	plt.title('Hoogte als functie van tijd')
	plt.legend()
	plt.grid(True, alpha=0.3)

	plt.tight_layout()
	plt.savefig('basejump_grafieken.png', dpi=150)
	plt.show()

	print(f"{tijd_parachute_zonder:.2f}")
	print(f"{tijd_parachute_met - tijd_parachute_zonder:.2f}")


basejump()
