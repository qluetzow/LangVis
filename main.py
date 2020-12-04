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

__doc__ = """Langvis: A visualizer for world languages."""



import bokeh.plotting as bp
import bokeh.tile_providers as bt
from bokeh.models import ColumnDataSource, Dropdown
from bokeh.models.tools import HoverTool
from bokeh.layouts import row
import pandas as pd
import numpy as np


def data():
    """ Pull data from a local .csv file and format it for plotting. """

    data_frame = pd.read_csv('countries.csv') #read file

    # changing the column names from the andorra location to what each
    # column represents
    new_columns_names = {'42.546245' : 'latitude','1.601554' : 'longitude',
                        'Andorra' : 'country', 'Andorra.1' : 'nativcountry',
                        'Català' : 'nativlang'}
    #renaming said columns
    data_frame = data_frame.rename(columns=new_columns_names)

    # creating a new row to include the Andorra row that was previously removed
    new_row = {'latitude' : 42.546245,'longitude' : 1.601554,
               'country' : 'Andorra', 'nativcountry' : 'Andorra',
               'nativlang' : 'Català'}

    # append to the data frame, keeping the structure of the frame
    data_frame = data_frame.append(new_row, ignore_index=True)

    # convert from lat/long coordinates to Web Mercator coordinates
    wgs84_to_web_mercator(data_frame, 'longitude', 'latitude')

    return ColumnDataSource(data_frame) #source for the data plot


def wgs84_to_web_mercator(data_frame, long, lat):
    """ Convert decimal longitude/latitude to Web Mercator format. """

    earth_radius = 6378137 # earth radius in meters at equator

    # add Web Mercator representations as new columns to the dataframe
    data_frame["x"] = data_frame[long] * (earth_radius * np.pi/180.0)
    data_frame["y"] = np.log(np.tan((90 + data_frame[lat]) * np.pi/360.0)) * earth_radius


def main():
    """ Main function for flow control and management. """

    # set name for output file
    bp.output_file("output.html")

    # get data from csv
    source = data()

    # set up basic plot
    plot = bp.figure(x_range=(-2000000, 6000000), y_range=(-1000000, 7000000),
                     x_axis_type="mercator", y_axis_type="mercator", sizing_mode="fixed", height = 700, width = 700)

    # get background tile and add to plot
    tile_provider = bt.get_provider(bt.Vendors.CARTODBPOSITRON)
    plot.add_tile(tile_provider)


    # set up hover tooltips and add to plot
    hover = HoverTool()
    hover.tooltips = [("Country", "@country"),
                      ("Native name", "@nativcountry"),
                      ("Native Language", "@nativlang")]

    plot.add_tools(hover)


    # define column names for the file that will be accesed
    colnames = ['latitude','longitude','country','nativcountry','nativlang']
    # read the file and go through the file to add the country names to a list
    countrylist = pd.read_csv('countries.csv',names=colnames)
    menu = countrylist.country.tolist()
    
    # make a drodown menu that shows a list of the Countries
    language_finder = Dropdown(label='List of Countries',button_type="warning",menu=menu)
    
    # add datapoints to plot, using circles to mark geographic locations
    plot.circle(x="x", y="y", source=source, size=10, color="red")

    # configuring the display and displaying it
    display_layout = row(language_finder,plot)
    bp.show(display_layout)


if __name__ == "__main__":
    main()
