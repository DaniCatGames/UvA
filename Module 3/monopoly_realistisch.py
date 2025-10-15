import random

import matplotlib.pyplot as plt


def worp_met_twee_dobbelstenen():
	dobbelsteen1 = random.randint(1, 6)
	dobbelsteen2 = random.randint(1, 6)
	return dobbelsteen1 + dobbelsteen2


def simuleer_potje_monopoly(startgeld_speler_1, startgeld_speler_2):
	# 0 is leeg (hoek etc), >0 is te koop
	bord_waardes = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120,
	                0, 140, 150, 140, 160, 200, 180, 0, 180, 200,
	                0, 220, 0, 220, 240, 200, 260, 260, 150, 280,
	                0, 300, 300, 0, 320, 200, 0, 350, 0, 400]

	bezittingen = [0] * 40  # 0 is vrij, 1 = player1, 2 = player2

	totaal_te_koop = sum(1 for waarde in bord_waardes if waarde > 0)
	aantal_verkocht = 0

	positie_1 = 0
	positie_2 = 0
	geld_1 = startgeld_speler_1
	geld_2 = startgeld_speler_2

	aantal_straten_speler_1 = 0
	aantal_straten_speler_2 = 0

	while aantal_verkocht < totaal_te_koop:
		vorige_positie_1 = positie_1
		worp_1 = worp_met_twee_dobbelstenen()
		positie_1 = (positie_1 + worp_1) % 40

		if positie_1 < vorige_positie_1:
			geld_1 += 200

		# als te koop en niet gekocht en genoeg geld koop
		if bord_waardes[positie_1] > 0 and bezittingen[positie_1] == 0:
			if geld_1 >= bord_waardes[positie_1]:
				geld_1 -= bord_waardes[positie_1]

				bezittingen[positie_1] = 1
				aantal_straten_speler_1 += 1
				aantal_verkocht += 1

				if aantal_verkocht >= totaal_te_koop:
					break  # break is een peak keyword

		vorige_positie_2 = positie_2
		worp_2 = worp_met_twee_dobbelstenen()
		positie_2 = (positie_2 + worp_2) % 40

		if positie_2 < vorige_positie_2:
			geld_2 += 200

		# als te koop en niet gekocht en genoeg geld koop
		if bord_waardes[positie_2] > 0 and bezittingen[positie_2] == 0:
			if geld_2 >= bord_waardes[positie_2]:
				geld_2 -= bord_waardes[positie_2]

				bezittingen[positie_2] = 2
				aantal_straten_speler_2 += 1
				aantal_verkocht += 2

	return aantal_straten_speler_1 - aantal_straten_speler_2


def simuleer_groot_aantal_potjes_monopoly(aantal_potjes, startgeld_speler_1,
                                          startgeld_speler_2):
	resultaten = []

	print(
		f"Monopoly simulator: twee spelers, startgeld [{startgeld_speler_1},{startgeld_speler_2}]")
	print(f"We simuleren {aantal_potjes} potjes...")

	for potje in range(aantal_potjes):
		if (potje + 1) % 500 == 0:
			print(f"  Potje {potje + 1} van {aantal_potjes}...")

		delta = simuleer_potje_monopoly(startgeld_speler_1, startgeld_speler_2)
		resultaten.append(delta)

	gemiddelde_delta = sum(resultaten) / len(resultaten)

	plt.figure(figsize=(10, 6))
	plt.hist(resultaten, bins=range(min(resultaten) - 1, max(resultaten) + 2),
	         edgecolor='black', alpha=0.7, align='left')
	plt.xlabel('Verschil in aantal straten (speler 1 - speler 2)')
	plt.ylabel('Frequentie')
	plt.title(
		f'Verdeling verschil straten in {aantal_potjes} potjes\nStartgeld: [{startgeld_speler_1}, {startgeld_speler_2}]')
	plt.axvline(gemiddelde_delta, color='red', linestyle='--', linewidth=2,
	            label=f'Gemiddelde: {gemiddelde_delta:.2f}')
	plt.legend()
	plt.grid(True, alpha=0.3)
	plt.show()
	plt.savefig('monopoly.png')

	return gemiddelde_delta


def evenwicht():
	startgeld_speler_1 = 1500
	aantal_potjes = 10000

	extra_waardes = [0, 50, 100, 150, 200]
	resultaten = { }

	for extra in extra_waardes:
		startgeld_speler_2 = startgeld_speler_1 + extra
		gemiddelde_delta = simuleer_groot_aantal_potjes_monopoly(
			aantal_potjes, startgeld_speler_1, startgeld_speler_2
		)
		resultaten[extra] = gemiddelde_delta

		print(f"Startgeld [{startgeld_speler_1},{startgeld_speler_2}]: "
		      f"speler 1 gemiddeld {gemiddelde_delta:.2f} meer straten "
		      f"(speler 2 heeft {extra} euro extra)")
		print()

	evenwicht_schatting = None
	for i in range(len(extra_waardes) - 1):
		extra_laag = extra_waardes[i]
		extra_hoog = extra_waardes[i + 1]
		delta_laag = resultaten[extra_laag]
		delta_hoog = resultaten[extra_hoog]

		# zoek welke om 0 zitten
		if delta_laag > 0 > delta_hoog:
			evenwicht_schatting = (extra_laag + extra_hoog) // 2
			break  # break is fucking peak

	print(f"Monopoly simulator: 2 spelers")
	print(f"Als we speler 2 {evenwicht_schatting} euro meer startgeld meegeven "
	      f"hebben beide spelers gemiddeld evenveel straten in bezit")

	return evenwicht_schatting


evenwicht()
