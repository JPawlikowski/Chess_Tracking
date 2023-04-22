
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from pullTrackerData import getTrackerDataEloFunc
from plotCreates import createPieFunc, createPlotFunc


csv_file = './ChessTracker_04212023.csv'
print('Reading csv :' + csv_file)

game_type = 'Blitz'

dt = datetime.now()
current_time = dt.strftime("%Y%m%d%H%M")

plot_graph_name = str('./graphs/Elo_plot_' + game_type + '_' + current_time + '.png')
pie_graph_name = str('./graphs/WinLoss_pie_' + game_type + '_' + current_time + '.png')
bw_games_pie_graph_name = str('./graphs/BW_games_pie_' + game_type + '_' + current_time + '.png')
bw_score_pie_graph_name = str('./graphs/BW_score_pie_' + game_type + '_' + current_time + '.png')

#Array as (white_wins::int , white_losses::int, black_wins::int, black_losses::int)
elo_befores = []
game_starts = []
win_loss = []
bw_score = []

#Pull data from csv into objects
game_type_id, elo_befores, game_starts, win_loss, bw_score = getTrackerDataEloFunc(csv_file, game_type)

#Create plot for overall Elo over time
plot_title = "Overall " + game_type + " Elo"
currentPlotStatus = createPlotFunc(plt, game_type_id, plot_graph_name, plot_title, game_starts, elo_befores, 'Game Dttm', 'Elo')

#Create pie for overall win-loss
pie_title = "Win-Loss Overall " + game_type
pie_labels = ['Wins', 'Draws', 'Losses']
currentPieStatus = createPieFunc(plt, pie_graph_name, pie_title, win_loss, pie_labels)

#Create pie for black-white games played
bw_games_pie_title = "Black & White Game Ratio " + game_type
bw_games_pie_labels = ['White_Games', 'Black_Games']
bw_games = [bw_score[0]+bw_score[1]+bw_score[2], bw_score[3]+bw_score[4]+bw_score[5]]
currentPieStatus = createPieFunc(plt, bw_games_pie_graph_name, bw_games_pie_title, bw_games, bw_games_pie_labels)

#Create pie for black-white win loss
bw_score_pie_title = "Black & White Win-Loss " + game_type
bw_score_pie_labels = ['White_Wins', 'White_Losses', 'White_Draws', 'Black_Wins', 'Black_Draws', 'Black_Losses']
currentPieStatus = createPieFunc(plt, bw_score_pie_graph_name, bw_score_pie_title, bw_score, bw_score_pie_labels)
