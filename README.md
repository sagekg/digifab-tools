# Laser Tools
Programs to help with making cool stuff on a laser cutter. Future code will include a TSP solver, a weighted stippler, and maybe also some basic useful image editing tools.

# Instructions
## Traveling Salesman
This scripts tspart.py, tspbitcity.py, and tspsolution.py were all written by Daniel C. Newman for the Eggbot project. They are all under a GNU GPL 2+ license. For specific documentation see [the Evil Mad Scientist Wiki](https://wiki.evilmadscientist.com/Generating_TSP_art_from_a_stippled_image). These have been deprecated in favor of [StippleGen 2](https://github.com/evil-mad/stipplegen). For more about them, you can also go to https://github.com/evil-mad/stipplegen.


To make this work, you'll also need the Linkern executable from the University of Waterloo's Concorde TSP solver. On Linux (I'm running Ubuntu 18.10), I just downloaded the [Concorde source code](http://www.math.uwaterloo.ca/tsp/concorde/downloads/downloads.htm), and copied the Linkern executable (in LINKERN/) to /usr/local/bin/. I included Linkern here for ease of use. For further installation information, including for Windows and OS X, see [the Evil Mad Scientist Wiki solver page](https://wiki.evilmadscientist.com/Obtaining_a_TSP_solver).
