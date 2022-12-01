
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from pullTrackerData import getTrackerDataEloFunc

csv_file = './ChessTracker_11302022.csv'
print('Reading csv :' + csv_file)

game_type = 'Blitz-5'

dt = datetime.now()
current_time = dt.strftime("%Y%m%d%H%M")

plot_graph_name = str('./graphs/Elo_plot_' + game_type + '_' + current_time + '.png')
pie_graph_name = str('./graphs/Elo_pie_' + game_type + '_' + current_time + '.png')

elo_befores = []
game_starts = []
win_loss = []

fig, ax = plt.subplots()
ax.set_title("Overall " + game_type + " Elo")

#Pull data from csv
elo_befores, game_starts, win_loss = getTrackerDataEloFunc(csv_file, game_type)
ax.set_ylabel('Elo')
ax.plot(game_starts, elo_befores)
plt.xticks(rotation=70)
plt.tight_layout()

plt.savefig(plot_graph_name, dpi=None, facecolor='w', edgecolor='w', orientation='portrait', format=None, transparent=False, bbox_inches=None, pad_inches=0.5, metadata=None)

fig1, ax1 = plt.subplots()
ax1.set_title("Win-Loss Overall " + game_type)
pie_labels = ('Wins', 'Losses')
ax1.pie(win_loss, labels=pie_labels, startangle=90, autopct='%1.1f%%')
ax1.axis('equal')

plt.savefig(pie_graph_name, dpi=None, facecolor='w', edgecolor='w', orientation='portrait', format=None, transparent=False, bbox_inches=None, pad_inches=0.5, metadata=None)