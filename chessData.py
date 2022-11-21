
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from pullTrackerData import getTrackerDataEloFunc

#exit()

csv_file = './ChessTracker_11212022.csv'
print('Reading csv :' + csv_file)

game_type = 'Blitz-5'

dt = datetime.now()
current_time = dt.strftime("%Y%m%d%H%M")

current_graph_name = str('./graphs/Elo_chart_' + game_type + current_time + '.png')

elo_befores = []
game_starts = []

plt.ylabel('Elo')
plt.title(game_type + ' Ranking')
plt.xlabel('Game played')

elo_befores, game_starts = getTrackerDataEloFunc(csv_file, game_type)

plt.plot(game_starts, elo_befores)
plt.xticks(rotation=90)
plt.tight_layout()
#plt.ylim([500,1100])
plt.show()

plt.savefig(current_graph_name, dpi=None, facecolor='w', edgecolor='w', orientation='portrait', format=None, transparent=False, bbox_inches=None, pad_inches=0.5, metadata=None)