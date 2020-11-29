# Langvis: A visualizer for world languages' locations.

# Copyright (C) 2020 Quinn Luetzow,  Angelique Bernik, Dakota Bond,
# Joseph Marchetti, Josh Kizilos.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


__author__ = ["Quinn Luetzow", "Angelique Bernik", "Dakota Bond",
              "Joseph Marchetti", "Josh Kizilos"]


import bokeh.plotting as bp
import bokeh.tile_providers as bt
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
import pandas as pd
import numpy as np


def data():
    """ Pull data from a local .csv file and format it for plotting. """

    df = pd.read_csv('countries.csv') #read file
  
    # changing the column names from the andorra location to what each
    # column represents
    new_columns_names = {'42.546245' : 'latitude','1.601554' : 'longitude',
                        'Andorra' : 'country', 'Andorra.1' : 'nativcountry',
                        'Català' : 'nativlang'}
    #renaming said columns
    df = df.rename(columns=new_columns_names)
  
    # creating a new row to include the Andorra row that was previously removed
    new_row = {'latitude' : 42.546245,'longitude' : 1.601554,
               'country' : 'Andorra', 'nativcountry' : 'Andorra',
               'nativlang' : 'Català'}
  
    # append to the data frame, keeping the structure of the frame
    df = df.append(new_row, ignore_index=True)

    # convert from lat/long coordinates to Web Mercator coordinates
    wgs84_to_web_mercator(df, 'longitude', 'latitude')

    source = ColumnDataSource(df) #source for the data plot

    return source


def wgs84_to_web_mercator(df, long, lat):
  """ Convert decimal longitude/latitude to Web Mercator format. """
  
  earth_radius = 6378137 # earth radius in meters at equator

  # add Web Mercator representations as new columns to the dataframe
  df["x"] = df[long] * (earth_radius * np.pi/180.0)
  df["y"] = np.log(np.tan((90 + df[lat]) * np.pi/360.0)) * earth_radius


def main():
    """ Main function for flow control and management. """

    # set name for output file
    bp.output_file("output.html")

    # get data from csv
    source = data()

    # set up basic plot
    plot = bp.figure(x_range=(-2000000, 6000000), y_range=(-1000000, 7000000),
                     x_axis_type="mercator", y_axis_type="mercator")

    # get background tile and add to plot
    tile_provider = bt.get_provider(bt.Vendors.CARTODBPOSITRON)
    plot.add_tile(tile_provider)    


    # set up hover tooltips and add to plot
    hover = HoverTool()
    hover.tooltips = [("Country", "@country"),
                      ("Native name", "@nativcountry"),
                      ("Native Language", "@nativlang")]
    
    plot.add_tools(hover)

    # add datapoints to plot, using circles to mark geographic locations
    plot.circle(x="x", y="y", source=source, size=10, color="red")
    

    # display
    bp.show(plot)


if __name__ == "__main__":
    main()
