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
import pandas as pd
import bokeh
import pandas_bokeh

df = pd.read_csv('countries.csv')

new_column_names = {'42.546245':'latitude','1.601554':'longitude','Andorra':'country','Andorra.1':'nativcountry','Català':'nativlang'}
df = df.rename(columns=new_columns_names)
new_row = {'latitude':42.546245,'longitude':1.601554,'country':'Andorra','nativcountry':'Andorra','nativlang':'Català'}
df = df.append(new_row, ignore_index=True)

df2 = pd.DataFrame(columns=['latitude','longitude'])
df3 = pd.DataFrame(columns=['countrynames','nativcountry','nativlang'])
frames = [df2,df3]
combined_df = pd.concat(frames,axis=1)

latitude, longitude = [], []
countrynames = []
nativcountry = []
nativlang = []
latitude.append(df['latitude'])
longitude.append(df['longitude'])
countrynames.append(df['country'])
nativcountry.append(df['nativcountry'])
nativlang.append(df['nativelanguage'])
