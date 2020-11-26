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
