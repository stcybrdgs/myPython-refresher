# widgetPlacement

# The TK Geometry Manager takes instructions from the program and does
# its best to place the widgets in their intended locations.
# It uses the concept of master and slave widgets to do that.
# the master widget will use a Geometry Manager to control the
# placement of the slave widget.

# There are three Geometry Managers in Tk, each of which provides a different
# way for the program to describe widget locations.
# Pack Geometry Manager -
#     simple scenarios for side-by-side or stack placement
# Grid Geometry Manager -
#     divides master widget into a 2D table and places slave widgets into cells
#     by indexing rows and columns
# Place Geometry Manager-
#     allows program to explicitly set the position of a widget using
#     relative or absolute terms in a the X and Y directions
#
# You can use whichever geometry manager makes since for your needs, but be
# careful about using more than one manager within the same master because
# using multiple managers in the same master can cause conflicts within Tk that
# can cause unintended results.