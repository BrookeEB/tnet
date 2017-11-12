# This is tNet
tNet is a pathfinding utility for [Starborne](https://www.starborne.com/)

You can download the v0.1 release [here](https://github.com/jzmiller1/tnet/files/1464357/tNet.zip).

## How it Works
tnet reads data from a CSV file you provide.  The CSV contains the coordinates of
your stations and the speed boost provided from any stargates at that station. 
See example_data.csv in this repository.

The data is used to create a [directed graph](https://en.wikipedia.org/wiki/Directed_graph)
of your "transportation network".  Using this graph along with 
[Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) you
can find the fastest path between stations.

This tool may be overkill for a single player or the early game but has a lot 
more utility for alliances or confederations with a large number of stations 
that may wish to move ships over greater distances...or players with stations at
the far ends of the galaxy!

### Screenshot of Tool and Results
![Image of Yaktocat](https://raw.githubusercontent.com/jzmiller1/tnet/master/example.JPG)

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
