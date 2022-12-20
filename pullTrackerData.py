
import csv

def getTrackerDataEloFunc(csv_file, game_type):
    elo_befores = []
    game_starts = []
    win_loss_str = []
    black_white_src = []
    print('in function call')
    with open(csv_file) as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            if (row[0].startswith(game_type) ):
                elo_befores.append(int(row[4]))
                game_starts.append(str(row[1]) + ' ' + str(row[2]))
                win_loss_str.append(str(row[3]))
                black_white_src.append(str(row[6]))
            
    #print elo summary
    for i in range(0, len(elo_befores)):
        print(str(game_starts[i]) + ', ' + str(elo_befores[i]))

    #Convert wins and losses strings to numbers, no longer needed, can pull from below
    #wins = 0
    #for i in win_loss_str:
    ##    if (i.lower() == 'w'):
    #        wins = wins + 1
    #win_loss = (wins, len(win_loss_str)-wins)

    #should be able to combine the below with above loop
    white_wins = 0
    black_wins = 0
    white_losses = 0
    black_losses = 0
    white_stalemates = 0
    black_stalemates = 0
    for j in range(0, len(black_white_src)):
        if ((black_white_src[j].lower() == 'white')):
            if (win_loss_str[j].lower() == 'w'):
                white_wins = white_wins + 1
            elif (win_loss_str[j].lower() == 'l'):
                white_losses = white_losses + 1
            else:
                white_stalemates = white_stalemates + 1
        elif ((black_white_src[j].lower() == 'black')):
            if (win_loss_str[j].lower() == 'w'):
                black_wins = black_wins + 1
            elif (win_loss_str[j].lower() == 'l'):
                black_losses = black_losses + 1
            else:
                black_stalemates = black_stalemates + 1
        elif ((black_white_src[j].lower() != 'white') or (black_white_src[j].lower() != 'black')):
            print("Error found at row " + str(j) + ", colour not matched as either white or black")

    black_white_score = [white_wins, white_losses, white_stalemates, black_wins, black_stalemates, black_losses]
    win_loss = [white_wins+black_wins, white_stalemates+black_stalemates, white_losses+black_losses]

    return elo_befores, game_starts, win_loss, black_white_score

