import random

import matplotlib.pyplot as plt


def worp_met_twee_dobbelstenen():
	dobbelsteen1 = random.randint(1, 6)
	dobbelsteen2 = random.randint(1, 6)
	return dobbelsteen1 + dobbelsteen2


def simuleer_potje_monopoly(startgeld_speler):
	bord_waardes = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120,
	                0, 140, 150, 140, 160, 200, 180, 0, 180, 200,
	                0, 220, 0, 220, 240, 200, 260, 260, 150, 280,
	                0, 300, 300, 0, 320, 200, 0, 350, 0, 400]

	bezittingen = [0] * 40  # 0 is vrij

	totaal_te_koop = sum(1 for waarde in bord_waardes if waarde > 0)
	aantal_in_bezit = 0

	positie = 0
	aantal_worpen = 0

	geld = startgeld_speler

	while aantal_in_bezit < totaal_te_koop:
		vorige_positie = positie
		worp = worp_met_twee_dobbelstenen()
		aantal_worpen += 1

		positie = (positie + worp) % 40

		if positie < vorige_positie:
			geld += 200

		# als te koop en niet gekocht en genoeg geld koop
		if bord_waardes[positie] > 0 and bezittingen[positie] == 0:
			if geld >= bord_waardes[positie]:
				geld -= bord_waardes[positie]

				bezittingen[positie] = 1
				aantal_in_bezit += 1

	return aantal_worpen


def simuleer_groot_aantal_potjes_monopoly(aantal_potjes, startgeld_speler=None):
	resultaten = []

	if startgeld_speler is None:
		print(f"Monopoly simulator: 1 speler, miljardair-modus")
	else:
		print(f"Monopoly simulator: 1 speler, {startgeld_speler} euro startgeld")
	print(f"We simuleren {aantal_potjes} potjes...")

	for potje in range(aantal_potjes):
		if (potje + 1) % 500 == 0:
			print(f"  Potje {potje + 1} van {aantal_potjes}...")

		aantal_worpen = simuleer_potje_monopoly(startgeld_speler)
		resultaten.append(aantal_worpen)

	gemiddelde = sum(resultaten) / len(resultaten)

	plt.figure(figsize=(10, 6))
	plt.hist(resultaten, bins=50, edgecolor='black', alpha=0.7)
	plt.xlabel('Aantal worpen')
	plt.ylabel('Frequentie')
	if startgeld_speler is None:
		titel = f'Verdeling van aantal worpen in {aantal_potjes} potjes Monopoly (miljardair-modus)'
	else:
		titel = f'Verdeling van aantal worpen in {aantal_potjes} potjes Monopoly ({startgeld_speler} euro startgeld)'
	plt.title(titel)
	plt.axvline(gemiddelde, color='red', linestyle='--', linewidth=2,
	            label=f'Gemiddelde: {gemiddelde:.1f}')
	plt.legend()
	plt.grid(True, alpha=0.3)
	plt.show()
	plt.savefig("monopoly.png")

	if startgeld_speler is None:
		print(f"\nMonopoly simulator: 1 speler, miljardair-modus")
	else:
		print(
			f"\nMonopoly simulator: 1 speler, {startgeld_speler} euro startgeld, {aantal_potjes} potjes")
	print(
		f"Gemiddeld duurde het {gemiddelde:.1f} worpen voor de speler alle straten in zijn bezit had")

	return gemiddelde


simuleer_groot_aantal_potjes_monopoly(10000, 1500)
