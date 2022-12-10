
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from pullTrackerData import getTrackerDataEloFunc
from plotCreates import createPieFunc, createPlotFunc

csv_file = './ChessTracker_11302022.csv'
print('Reading csv :' + csv_file)

game_type = 'Blitz-5'

dt = datetime.now()
current_time = dt.strftime("%Y%m%d%H%M")

plot_graph_name = str('./graphs/Elo_plot_' + game_type + '_' + current_time + '.png')
pie_graph_name = str('./graphs/WinLoss_pie_' + game_type + '_' + current_time + '.png')
bw_pie_graph_name = str('./graphs/BW_pie_' + game_type + '_' + current_time + '.png')

elo_befores = []
game_starts = []
win_loss = []
#Array as (white_wins::int , white_losses::int, black_wins::int, black_losses::int)
black_white_score = []

#Pull data from csv into objects
elo_befores, game_starts, win_loss, black_white_score = getTrackerDataEloFunc(csv_file, game_type)
print(str(black_white_score))

#Create plot for overall Elo over time
plot_title = "Overall " + game_type + " Elo"
currentPlotStatus = createPlotFunc(plt, plot_graph_name, plot_title, game_starts, elo_befores, 'Game Dttm', 'Elo')

#Create pie for overall win-loss
pie_title = "Win-Loss Overall " + game_type
pie_labels = ['Wins', 'Losses']
currentPieStatus = createPieFunc(plt, pie_graph_name, pie_title, win_loss, pie_labels)

#Create pie for black-white win loss
bw_pie_title = "Black & White Win-Loss " + game_type
bw_pie_labels = ['White_Wins', 'White_Losses', 'Black_Wins', 'Black_Losses']
currentPieStatus = createPieFunc(plt, bw_pie_graph_name, bw_pie_title, black_white_score, bw_pie_labels)
