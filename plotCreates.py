from matplotlib.ticker import MultipleLocator

def createPlotFunc(plt, game_type_id, plot_graph_name, plot_title, x_data, y_data, x_label, y_label):
    print('Creating plot..')
    fig, ax = plt.subplots()
    ax.set_title(plot_title)
    ax.set_ylabel(y_label)
    ax.xaxis.set_major_locator(MultipleLocator(5))
    #game id 1 data
    index_1_start = 0
    index_1_end = 0
    index_1_pairs = []
    index_2 = []
    #index_3 = []
    """
    for i in range(0, len(game_type_id)-1):
        if game_type_id[i] == 1:
            index_1_start = i
            index_1_end = i
            while game_type_id[i] == 1:
                index_1_end = i
                i = i+1
            ax.plot(x_data[index_1_start:index_1_end], y_data[index_1_start:index_1_end], color="blue")
            print(index_1_start)
            print(index_1_end)
            
        elif game_type_id[i] == 2:
            index_2.append(i)
        #elif game_type_id[i] == 3:
            #index_3.append(i)
        else:
            print("Warning, issue with index data split")
    """
    print('game type id length : ' + str(len(game_type_id)))
    i = 0
    print(str(game_type_id[len(game_type_id)-1]))
    while i < len(game_type_id)-1:
        if game_type_id[i] == 1:
            index_1_start = i
            index_1_end = i
            while game_type_id[i] == 1:
                print(i)
                if (i == len(game_type_id)-1):
                    break
                else:
                    i = i + 1
                    index_1_end = i
            print("Plotting 1s: ")
            print(index_1_start)
            print(index_1_end)
            try:
                ax.plot(x_data[index_1_start:index_1_end], y_data[index_1_start:index_1_end], color="blue")
            except:
                print('Issue found plotting : ' + plot_title)
                return 1
            if (i < len(game_type_id)-1):
                i = i + 1
            else:
                break
            print("end of first loop i :" + str(i))
        elif game_type_id[i] == 2:
            index_2_start = i
            index_2_end = i
            while game_type_id[i] == 2:
                if (i == len(game_type_id)-1):
                    break
                else:
                    i = i + 1
                    index_2_end = i
            print("Plotting 2s: ")
            print(index_2_start)
            print(index_2_end)
            try:
                ax.plot(x_data[index_2_start:index_2_end], y_data[index_2_start:index_2_end], color="green")
            except:
                print('Issue found plotting : ' + plot_title)
                return 1
            if (i < len(game_type_id)-1):
                i = i + 1
            else:
                break
        else:
            print("loop bottom")

    plt.xticks(rotation=70)
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