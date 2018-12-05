# Laser Tools
Programs to help with making cool stuff on a laser cutter. Future code will include a TSP solver, a weighted stippler, and maybe also some basic useful image editing tools.

# Traveling Salesman
This scripts tspart.py, tspbitcity.py, and tspsolution.py were all written by Daniel C. Newman for the Eggbot project. They are all under a GNU GPL 2+ license. For specific documentation see [the Evil Mad Scientist Wiki](https://wiki.evilmadscientist.com/Generating_TSP_art_from_a_stippled_image). These have been deprecated in favor of [StippleGen 2](https://github.com/evil-mad/stipplegen). For more about them, you can also go to https://github.com/evil-mad/stipplegen.


To make this work, you'll also need the Linkern executable from the University of Waterloo's Concorde TSP solver. On Linux (I'm running Ubuntu 18.10), I just downloaded the [Concorde source code](http://www.math.uwaterloo.ca/tsp/concorde/downloads/downloads.htm), and copied the Linkern executable (in LINKERN/) to /usr/local/bin/. I included Linkern here for ease of use. For further installation information, including for Windows and OS X, see [the Evil Mad Scientist Wiki solver page](https://wiki.evilmadscientist.com/Obtaining_a_TSP_solver).

# Weighted Voronoi
The code in the folder weighted-voronoi/ was wrtten by Nicolas P. Rougier under a BSD license. It was published in ReScience in 2017.

## Pre-requisites

This replication has been written and tested on OSX 10.12 (Sierra) using the
following packages:

 * Python 3.6.0
 * Numpy 1.12.0
 * Scipy 0.18.1
 * Matplotlib 2.0.0
 * tqdm 4.11.2
 * Pillow 4.0.0

Original data is in the data directory and you can also obtain it from
[Adrian Secord homepage](http://cs.nyu.edu/~ajsecord/npar2002/StipplingOriginals.zip).

## Usage

```
 usage: stippler.py [--n_iter n] [--n_point n] [--save] [--force]
                    [--pointsize min,max] [--figsize w,h]
                    [--display] [--interactive] file

 Weighted Vororonoi Stippler

 positional arguments:
   file                  Density image filename

 optional arguments:
   -h, --help            show this help message and exit
   --n_iter n            Maximum number of iterations
   --n_point n           Number of points
   --pointsize (min,max) (min,max)
                         Point mix/max size for final display
   --figsize w,h         Figure size
   --force               Force recomputation
   --save                Save computed points
   --display             Display final result
   --interactive         Display intermediate results (slower)
