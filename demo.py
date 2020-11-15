import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

def read_data(file_name):
    data = open(file_name)
    results = []
    data.readline()
    for row in data.readlines():
        row = row.split(',')
        results.append(tuple([row[0], int(row[1]), row[2].strip()]))
    data.close()
    return results


def Draw_pie(results):
    r = 0
    b = 0
    p = 0
    for result in results:
        if result[2] == 'R':
            r = r + result[1]
        if result[2] == 'B':
            b = b + result[1]
        if result[2] == 'P':
            p = p + result[1]
    print(results)
    print(r, b, p)
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Republican', 'Democrat', 'Swing States'
    sizes = [r, b, p]
    explode = (0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Democrat')
    colors = ["red", "blue", "purple"]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90, colors=colors)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


def Draw_bar(results):
    states = []
    numbers = []
    colors = []
    for result in results:
        states.append(result[0])
        numbers.append(result[1])
        if result[2] == 'R':
            colors.append('red')
        elif result[2] == 'B':
            colors.append('blue')
        elif result[2] == 'P':
            colors.append('purple')

    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot(111)
    ax.bar(np.arange(len(states)), numbers, log=0,color=colors)
    ax.set_xticks(np.arange(len(states)))
    ax.set_xticklabels(states, rotation=90, zorder=100)

if __name__ == '__main__':
    results = read_data('electoral_data.csv')
    Draw_pie(results)
    Draw_bar(results)
    plt.show()