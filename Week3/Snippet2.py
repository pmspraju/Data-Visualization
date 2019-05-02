# -*- coding: utf-8 -*-
"""
Created on Wed May  1 00:09:12 2019

@author: C830587
"""
import os
import pandas as pd
import folium

data = 'C:\Users\c830587\Installed\Data-Visualization\Data'
state_geo = os.path.join(data, 'us-states.json')
print (state_geo)
state_unemployment = os.path.join(data, 'US_Unemployment_Oct2012.csv')
state_data = pd.read_csv(state_unemployment)

m = folium.Map(location=[48, -102], zoom_start=3)

folium.Choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=['State', 'Unemployment'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Unemployment Rate (%)'
).add_to(m)

folium.LayerControl().add_to(m)
