'''
This module contains
    - functions to plot 2D geo map with Basemap
    - functions to assist the plot

This module allows users to
    - select year interval with ipywidgets
    - visualize the terror attacks' occurrence density
    - customize map background

@author: Xianzhi Cao (xc965)
'''


from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
import feature as ft
from ipywidgets import *


def plot_2D_density(Year, MapStyle):
    '''
    Parameters
        - Year      : between 1970-2015     | str
        - MapStyle  : style palette         | str
    Return
        A 2D Geo Map: The denser the red marker in a country,
                      the more severe damages had taken place.
    '''
    df = ft.df_sel_btw_years(Year)
    plt.figure(figsize=(18,10))

    m = Basemap('mill')
    m.drawcountries(linewidth=0.5,
                    linestyle='solid',
                    color='w',
                    antialiased=1,
                    ax=None,
                    zorder=None
                    )

    # Background settings
    if MapStyle == 'Blue Marble':
        m.drawcoastlines()
        m.bluemarble()
    elif MapStyle == 'Etopo':
        m.etopo()
    else:
        m.fillcontinents()
        m.drawmapboundary()

    # get latitude and longitude
    lat = ft.make_array(df, 'latitude')
    lon = ft.make_array(df, 'longitude')

    x,y = m(lon, lat)
    m.plot(x, y, 'r.', marker='o', markersize=3, alpha=.8)

    plt.title('Global Attack Density Dot Plot: {}-{}'.format(Year[0], Year[1]), size=16)
    plt.show()


def year_interval_slider():
    '''
    Return a year interval from ipywidgets' IntSlider by users' manual pick
    '''
    yr_interval = IntRangeSlider(value=[1996, 2000],
                                 min=1970,
                                 max=2015,
                                 step=1,
                                 description='Year:',
                                 disabled=False,
                                 continuous_update=False,
                                 orientation='horizontal',
                                 readout=True,
                                 readout_format='i',
                                 slider_color='white',
                                 color='black')
    yr_interval.layout.width = '80%'
    return yr_interval


def map_style_picker():
    '''
    Return a string from ipywidgets' Dropdown box by users' manual pick
    '''
    return Dropdown(options=('Blue Marble', 'Etopo', 'Plain'),
                    value='Blue Marble',
                    description='Map Style:',
                    disabled=False,
                    button_style='info')


def Display_Your_Geo2D_Map():
    '''
    Allow users to interactively explore data information
    and customize the 2D Geo Map
    '''
    interact(plot_2D_density, Year=year_interval_slider(), MapStyle=map_style_picker())
