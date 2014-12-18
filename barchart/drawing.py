#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import sys
import matplotlib.pyplot as plt

menMeans = []

for line in sys.stdin:
    tokens = line[:-1].split()
    menMeans.append(float(tokens[1]))

N = len(menMeans) 

ind = 0.1 + np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width, color='r')

# add some text for labels, title and axes ticks
ax.set_ylabel('Happy Rate')
ax.set_title('Happy Rate vs Time')
ax.set_xticks(ind+width/2)
ax.set_xticklabels( ('Nov 1-10', 'Nov 11-20', 'Nov 21-30') )
ax.set_ylim(0.99, 1)

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1*height, '%f'%height,
                ha='center', va='bottom')

autolabel(rects1)

plt.show()
