
import csv
from datetime import datetime
import matplotlib.pyplot as plt

csv_file = './ChessTracker_11052022.csv'

print('Reading csv :' + csv_file)

elo_befores = []
elo_afters = []
game_starts = []

plt.ylabel('Elo')
plt.title('Rapid 10 Ranking')
plt.xlabel('Game played')


with open(csv_file) as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        if (row[0].startswith('Rapid 10') ):
            elo_befores.append(int(row[4]))
            elo_afters.append(int(row[5]))
            game_starts.append(str(row[1]) + ' ' + str(row[2]))
            #print(row[4] + ', ' + row[5])

for i in range(0, len(elo_befores)):
    print(game_starts[i])
    print(str(elo_befores[i]) + ', ' + str(elo_afters[i]))

plt.plot(game_starts, elo_befores)
#plt.gca().invert_yaxis()
plt.xticks(rotation=90)
plt.tight_layout()
#plt.ylim([500,1100])
#plt.show()

dt = datetime.now()
current_time = dt.strftime("%Y%m%d%H%M")
current_graph_name = str('./graphs/Elo_chart_Rapid-10_' + current_time + '.png')

plt.savefig(current_graph_name, dpi=None, facecolor='w', edgecolor='w', orientation='portrait', format=None, transparent=False, bbox_inches=None, pad_inches=0.5, metadata=None)