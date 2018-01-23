# This is tNet
tNet is a pathfinding utility for [Starborne](https://www.starborne.com/)

You can download the v0.1 release [here](https://github.com/jzmiller1/tnet/files/1464357/tNet.zip).

## How it Works
tnet reads data from a CSV file you provide.  The CSV contains the coordinates of
the stations in your transportation network, the speed boost provided from any 
stargates to each station and the ownership status. See example_data.csv in this 
repository.

The data is used to create a [directed graph](https://en.wikipedia.org/wiki/Directed_graph)
of your "transportation network".  Using this graph along with 
[Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) you
can find the fastest path between stations.

This tool may be overkill for a single player or the early game but has a lot 
more utility for alliances or confederations with a large number of stations 
that may wish to move ships over greater distances...or players with stations at
the far ends of the galaxy!

### Screenshot of Tool and Results
![Screenshot of Tool](https://raw.githubusercontent.com/jzmiller1/tnet/master/example.JPG)

## Built On
tNet was put together using [wxPython](https://www.wxpython.org/) for the GUI 
and [networkx](https://networkx.github.io/) to handle the directed graph and 
pathfinding.

## References
Thanks to the [Python GUI Cookbook Second Edition](https://www.packtpub.com/application-development/python-gui-programming-cookbook-second-edition)
for the wxPython chapter I used as a guide for this.

## About Support and Updates
This is only intended to run on Windows and is only a fun little project so support
and updates will be limited.

## Specific Movement Examples
The coordinates in the data are hexgonal coordinates you can learn everything you want 
to know about hexagons from the amazing [Red Blob Games](https://www.redblobgames.com/grids/hexagons/).

A quick and useful visualization of the data is to use the hexagonal coordinates of the 
stations in the example data to show the general spatial arrangement of the stations (don't
worry it is using the proper hexagon based calculations in the program):

![Example Data Visualization](https://raw.githubusercontent.com/jzmiller1/tnet/master/example_data_visualization.jpg)

None of the stations flagged as ours, flagged as self in the example data, have a stargate 
bonus to movement.  The friendly station that we don't own, Dev Hacks Palace, is fairly 
centrally located and has the maximum stargate bonus of +10.  While we're mentioning the 
bonus amounts it is a good time to note that the bonus value is not checked in the program 
so if you want to use other values or the bonuses from stargates change you won't need a 
new version of the program.  The large bonus at Dev Hacks Palace combined with its central 
location means that any movement going from one edge of our stations to the other will 
get a large travel time reduction by travelling through Dev Hacks Palace.  One example
might be moving from Grated Gate to Rustic Dairy.  With a fleet speed of 10 the path 
through Dev Hacks Palace takes 177 minutes while the direct path takes 186 minutes.
These types of time savings are amplified if you are travelling larger distances.

Another movement scenario involves station ownership.  As of 1/1/2018 "Foreign to 
Foreign" movements, movements from a station that are not yours to another station that
is not yours, are not allowed.  That means that going directly from "Dev Hacks Palace" to 
"Someone Else's Station" is not allowed.  This restriction has big implications for 
defenders.  Currently tnet avoids these disallowed paths by giving them an extreme travel
time of 99999999 forcing the pathfinder to give you a valid route through one of your 
stations.  

![Example Other to Other Movement](https://raw.githubusercontent.com/jzmiller1/tnet/master/example_other_to_other.JPG)

Changes to this type of movement have been announced so verify the latest 
movement options in the game to ensure that the use of this tool is still valid.

