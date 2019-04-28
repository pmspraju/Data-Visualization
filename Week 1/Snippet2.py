# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:27:55 2019

@author: C830587
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(100000)
plt.hist(x,100)
plt.title('Normal distrubiution with $\mu=0, \sigma 1$')
plt.savefig('matplotlib_histogram_pyplot.png')
plt.show()