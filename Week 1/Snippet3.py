# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 16:04:20 2019

@author: C830587
"""
from __future__ import print_function
import numpy as np
import pandas as pd


data = pd.read_excel('Canada.xlsx',
                     sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

print (data.head())