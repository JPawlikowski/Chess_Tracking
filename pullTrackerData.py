
import csv

def getTrackerDataEloFunc(csv_file, game_type):
    elo_befores = []
    game_starts = []
    print('in function call')
    with open(csv_file) as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            if (row[0].startswith(game_type) ):
                elo_befores.append(int(row[4]))
                game_starts.append(str(row[1]) + ' ' + str(row[2]))
            

    for i in range(0, len(elo_befores)):
        print(str(game_starts[i]) + ', ' + str(elo_befores[i]))

    return elo_befores, game_starts

