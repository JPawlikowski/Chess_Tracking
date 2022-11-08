
import csv
import matplotlib.pyplot as plt

csv_file = './ChessTracker_11052022.csv'

print('Reading csv :' + csv_file)

elo_befores = []
elo_afters = []
game_starts = []

plt.ylabel('Elo')
plt.title('Rapid 10 Ranking')
plt.xlabel('Game played')
plt.invert_yaxis()

with open(csv_file) as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        if (row[0].startswith('Rapid 10') ):
            elo_befores.append(row[4])
            elo_afters.append(row[5])
            game_starts.append(row[1])
            #print(row[4] + ', ' + row[5])

for i in range(0, len(elo_befores)):
    print(elo_befores[i] + ', ' + elo_afters[i])

plt.plot(game_starts, elo_befores)
plt.show()