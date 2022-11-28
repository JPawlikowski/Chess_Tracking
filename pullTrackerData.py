
import csv

def getTrackerDataEloFunc(csv_file, game_type):
    elo_befores = []
    game_starts = []
    win_loss_str = []
    print('in function call')
    with open(csv_file) as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            if (row[0].startswith(game_type) ):
                elo_befores.append(int(row[4]))
                game_starts.append(str(row[1]) + ' ' + str(row[2]))
                win_loss_str.append(str(row[3]))
            
    #print elo summary
    for i in range(0, len(elo_befores)):
        print(str(game_starts[i]) + ', ' + str(elo_befores[i]))

    #Convert wins and losses strings to numbers
    wins = 0
    for i in win_loss_str:
        if (i.lower() == 'w'):
            wins = wins + 1
    win_loss = (wins, len(win_loss_str)-wins)

    return elo_befores, game_starts, win_loss

