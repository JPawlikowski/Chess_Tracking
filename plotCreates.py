from matplotlib.ticker import MultipleLocator

def createPlotFunc(plt, game_type_id, plot_graph_name, plot_title, x_data, y_data, x_label, y_label):
    print('Creating plot..')
    fig, ax = plt.subplots()
    ax.set_title(plot_title)
    ax.set_ylabel(y_label)
    ax.xaxis.set_major_locator(MultipleLocator(5))
    #game id 1 data
    index_1 = []
    index_2 = []
    #index_3 = []
    for i in range(0, len(game_type_id)):
        if game_type_id[i] == 1:
            index_1.append(i)
        elif game_type_id[i] == 2:
            index_2.append(i)
        #elif game_type_id[i] == 3:
            #index_3.append(i)
        else:
            print("Warning, issue with index data split")

    
    x_data_1=list(map(x_data.__getitem__, index_1))
    y_data_1=list(map(y_data.__getitem__, index_1))
    x_data_2=list(map(x_data.__getitem__, index_2))
    y_data_2=list(map(y_data.__getitem__, index_2))
    #x_data_3=list(map(x_data.__getitem__, index_3))

    print(str(x_data_1))
    plt.xticks(rotation=70)
    try:
        #Issue here, need to plot only consistent sets of games per type
        ax.plot(x_data_1, y_data_1, color="blue")
        ax.plot(x_data_2, y_data_2, color="green")
        #ax.plot(x_data_3, y_data, color="red")
    except:
        print('Issue found plotting : ' + plot_title)
        return 1
    ax.legend(["Blitz-5", "Blitz-3"])
    plt.tight_layout()
    try:
        plt.savefig(plot_graph_name, dpi=None, facecolor='w', edgecolor='w', orientation='portrait', format=None, transparent=False, bbox_inches=None, pad_inches=0.5, metadata=None)
    except:
        print('An issue found saving plot graph : ' + pie_graph_name)
        return 1
    
    print('Done.. -> '+ plot_graph_name + '\n')
    return 0


def createPieFunc(plt, pie_graph_name, pie_title, data, pie_labels):
    print('Creating pie..')
    fig, ax = plt.subplots()
    ax.set_title(pie_title)
    
    try:
        ax.pie(data, labels=pie_labels, startangle=90, autopct='%1.1f%%')
    except:
        print('An issue found creating pie : ' + pie_title)
        return 1
    ax.axis('equal')
    try:
        plt.savefig(pie_graph_name, dpi=None, facecolor='w', edgecolor='w', orientation='portrait', format=None, transparent=False, bbox_inches=None, pad_inches=0.5, metadata=None)
    except:
        print('An issue found saving pie graph : ' + pie_graph_name)
        return 1

    print('Done.. -> ' + pie_graph_name + '\n')
    return 0