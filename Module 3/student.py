import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('QtAgg')

n_stappen = 500
R = 1
pause_tijd = 0.01

x1, y1 = 0, 0
x2, y2 = 0, 0

x1_pos = [x1]
y1_pos = [y1]
x2_pos = [x2]
y2_pos = [y2]

for i in range(n_stappen):
	alpha1 = np.random.uniform(0, 2 * np.pi)
	x1 += R * np.cos(alpha1)
	y1 += R * np.sin(alpha1)
	x1_pos.append(x1)
	y1_pos.append(y1)

	alpha2 = np.random.uniform(0, 2 * np.pi)
	x2 += R * np.cos(alpha2)
	y2 += R * np.sin(alpha2)
	x2_pos.append(x2)
	y2_pos.append(y2)

alle_x = x1_pos + x2_pos
alle_y = y1_pos + y2_pos
marge = 5
x_min, x_max = min(alle_x) - marge, max(alle_x) + marge
y_min, y_max = min(alle_y) - marge, max(alle_y) + marge

plt.ion()
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_xlabel('x-positie')
ax.set_ylabel('y-positie')
ax.set_title('Random Walk van Twee Dronken Studenten')

ax.plot([0], [0], 'k*', markersize=15, label='Start')

lijn_student1, = ax.plot([], [], 'b-', alpha=0.3, linewidth=0.5, label='Student 1 traject')
lijn_student2, = ax.plot([], [], 'r-', alpha=0.3, linewidth=0.5, label='Student 2 traject')
punt_student1, = ax.plot([], [], 'bo', markersize=10, label='Student 1')
punt_student2, = ax.plot([], [], 'ro', markersize=10, label='Student 2')
verbindingslijn, = ax.plot([], [], 'g--', linewidth=2, label='Verbinding')

ax.legend(loc='upper right')

info_text = ax.text(0.02, 0.98, '', transform=ax.transAxes,
                    verticalalignment='top', fontsize=10,
                    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

for i in range(len(x1_pos)):
	lijn_student1.set_data(x1_pos[:i + 1], y1_pos[:i + 1])
	lijn_student2.set_data(x2_pos[:i + 1], y2_pos[:i + 1])

	punt_student1.set_data([x1_pos[i]], [y1_pos[i]])
	punt_student2.set_data([x2_pos[i]], [y2_pos[i]])

	verbindingslijn.set_data([x1_pos[i], x2_pos[i]], [y1_pos[i], y2_pos[i]])

	afstand = np.sqrt((x1_pos[i] - x2_pos[i]) ** 2 + (y1_pos[i] - y2_pos[i]) ** 2)

	stappen_over = n_stappen - i
	tijd_over = stappen_over * pause_tijd

	info_text.set_text(f'Stap: {i}/{n_stappen}\n'
	                   f'Afstand tussen studenten: {afstand:.2f}\n'
	                   f'Resterende tijd: {tijd_over:.1f}s')

	plt.draw()
	plt.pause(pause_tijd)

plt.ioff()
plt.show()
