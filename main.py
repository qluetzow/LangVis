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


def main():
    pass


if __name__ = "__main__":
    main()
import pandas as pd #import of everything that could be used may not be all though
import bokeh
import pandas_bokeh
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.layouts import layout
from bokeh.palettes import Spectral3
from bokeh.tile_providers import CARTODBPOSITRON
from pyproj import Proj, transform

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

output_file('file') #stand in, if used
latitude_points = [*range(-90.000000,90.000000,1)] #horizontal lines
longitude_points = [*range(-180.000000,180.000000,1)] #veritcal lines

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
#range of the graph in values, may conflict with lat long, was a little confused between the usage of e and N as well as its relation to the data with the below
left = -2150000
right = 18000000
bottom = -5300000
top = 11000000
#making graph
p = figure(x_range+Range1d(left, right), y_range+Range1d(bottom,top))
p.add_tile(CARTODBPOSITRON)
p.circle(x='E', y='N', source=source, line_color='grey', fill_color='yellow')

p.axis.visible = False
#showing graph
show(p)
#hover tool for the usage of interactive
hover = HoverTool() #fill in holder for eventual placement of other columns


#above code based on the visualizing Data with Bokeh and Pandas from the programming Historian, as well as some tutorials on Pandas itself
#needs hover tool appliction to be added
#could be proofed for errors or modified to our use better/as seen fit

