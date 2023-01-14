
import csv
from datetime import datetime

def getTrackerDataEloFunc(csv_file, game_type):
    elo_befores = []
    game_starts = []
    win_loss_str = []
    black_white_src = []
    game_type_dtl = ""
    game_type_id = []
    print('in function call')
    with open(csv_file) as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            if (row[0].startswith(game_type) ):
                if (row[0] == "Blitz-5"):
                    game_type_id.append(1)
                elif (row[0] == "Blitz-3"):
                    game_type_id.append(2)
                elif (row[0] == "Blitz-3-2"):
                    game_type_id.append(3)
                else:
                    print("Warning: game type id for blitz not found")
                    game_type_id.append(0)

                elo_befores.append(int(row[4]))
                game_starts.append(str(row[1]) + ' ' + str(row[2]))
                #current_game_start_str = str(row[1]) + ' ' + str(row[2])
                #current_game_start = datetime.strptime(current_game_start_str, '%Y-%m-%d %H:%M')
                #game_starts.append(current_game_start)
                #datetime = datetime.strptime(date_string, '%Y-%m-%d %H:%M')
                win_loss_str.append(str(row[3]))
                black_white_src.append(str(row[6]))
            
    #print elo summary
    #for i in range(0, len(elo_befores)):
        #print(str(game_starts[i]) + ', ' + str(elo_befores[i]))

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
    white_draws = 0
    black_draws = 0
    for j in range(0, len(black_white_src)):
        if ((black_white_src[j].lower() == 'white')):
            if (win_loss_str[j].lower() == 'w'):
                white_wins = white_wins + 1
            elif (win_loss_str[j].lower() == 'l'):
                white_losses = white_losses + 1
            else:
                white_draws = white_draws + 1
        elif ((black_white_src[j].lower() == 'black')):
            if (win_loss_str[j].lower() == 'w'):
                black_wins = black_wins + 1
            elif (win_loss_str[j].lower() == 'l'):
                black_losses = black_losses + 1
            else:
                black_draws = black_draws + 1
        elif ((black_white_src[j].lower() != 'white') or (black_white_src[j].lower() != 'black')):
            print("Error found at row " + str(j) + ", colour not matched as either white or black")

    black_white_score = [white_wins, white_losses, white_draws, black_wins, black_draws, black_losses]
    win_loss = [white_wins+black_wins, white_draws+black_draws, white_losses+black_losses]

    return game_type_id, elo_befores, game_starts, win_loss, black_white_score

