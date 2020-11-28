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
