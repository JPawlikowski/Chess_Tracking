
def createPlotFunc(plt, plot_graph_name, plot_title, x_data, y_data, x_label, y_label):
    print('Creating plot..')
    fig, ax = plt.subplots()
    ax.set_title(plot_title)
    ax.set_ylabel(y_label)
    plt.xticks(rotation=70)
    try:
        ax.plot(x_data, y_data)
    except:
        print('Issue found plotting : ' + plot_title)
        return 1
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