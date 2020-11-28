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
import pandas as pd 
import bokeh
import pandas_bokeh
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.layouts import layout
from bokeh.palettes import Spectral3
from bokeh.tile_providers import CARTODBPOSITRON
from pyproj import Proj, transform
import numpy as np
from bokeh.io import *

def data():
  df = pd.read_csv('countries.csv') #read file
  #changing the column names from the andorra location to what each column represents
  new_column_names = {'42.546245':'latitude','1.601554':'longitude','Andorra':'country','Andorra.1':'nativcountry','Català':'nativlang'}
  df = df.rename(columns=new_columns_names) #renaming said columns
  #creating a new row to include the Andorra row that was previously removed
  new_row = {'latitude':42.546245,'longitude':1.601554,'country':'Andorra','nativcountry':'Andorra','nativlang':'Català'}
  df = df.append(new_row, ignore_index=True) #append to the data frame, keeping the structure of the framw
  #separating the columns if need to be used in such a way
  df2 = pd.DataFrame(columns=['latitude','longitude']) 
  df3 = pd.DataFrame(columns=['countrynames','nativcountry','nativlang'])
  frames = [df2,df3] #grouping
  combined_df = pd.concat(frames,axis=1) #re combining
  lat = df['latitude'].astype('float') #column as float 
  long = df['longitude'].astype('float') #column as float
  def wgs84_to_web_mercator(df, long, lat): #Converts decimal longitude/latitude to Web Mercator format
    k = 6378137
    df["x"] = df[long] * (k * np.pi/180.0)
    df["y"] = np.log(np.tan((90 + df[lat]) * np.pi/360.0)) * k
    return df

df=wgs84_to_web_mercator(df,'longitude','latitude')
#below if needed
latitude_points = [*range(-90.000000,90.000000,1)] #horizontal lines if needed
longitude_points = [*range(-180.000000,180.000000,1)] #veritcal lines if needed
#below function if needed
def LongLat_to_EN(long, lat): #function to change the latitude values and the longitude values to east and north axis
  try:
    easting, northing = transform(Proj(init='epsg:4326'), Proj(init='epsg:3857'), long, lat)
    return easting, northing
  except:
    return None, None
# goal of previous is make sure there are not overlapping values thus wonking up the layout
#using e and n for the application of the range of points, there are probably already a range that could be used
df['E'], df['N'] = zip(*df.apply(lambda x: LongLat_to_EN(x['longitude_points'],x['latitude_points']), axis=1))
grouped = df.groupby(['E','N'])['latitude','longitude'].sum().reset_index() #grouping the range to the data
source = ColumnDataSource(grouped) #source for the data plot
#above could be reomved if you don't need
def main():
    # set name for output file
    bp.output_file("output.html")

    # get background tile
    tile_provider = bt.get_provider(bt.Vendors.CARTODBPOSITRON)

    # set up basic plot
    plot = bp.figure(x_range=(-2000000, 6000000), y_range=(-1000000, 7000000),
                     x_axis_type="mercator", y_axis_type="mercator")

    # add tile
    plot.add_tile(tile_provider)

    # display
    bp.show(plot)


    # Still have to get data and put it into the plot, but can't really do that
    # very well until we know how it's formatted


if __name__ == "__main__":
    main()
