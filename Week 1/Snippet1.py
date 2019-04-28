# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:05:42 2019

@author: C830587
"""
#import figure canvas
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

#import artust figure object
from matplotlib.figure import Figure 
fig = Figure()

#attach figure artist to Figure canvas
canvas = FigureCanvas (fig)

#import numpy to generate 10000 random numbers
import numpy as np
x = np.random.randn(10000)

#create axes by adding a subplot to the figure artist.
#111 - deonotes First cell of First row and first column 
ax = fig.add_subplot(111) 

#draw histogram from axes with 100 bins
ax.hist(x,100)

#add a title to the axes
ax.set_title('Normal distrubiution with $\mu=0, \sigma 1$')

#save the figure
fig.savefig('matplotlib_histogram.png')
