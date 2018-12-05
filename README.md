# Laser Tools
Programs to help with making cool stuff on a laser cutter. Future code will include a TSP solver, a weighted stippler, and maybe also some basic useful image editing tools.

## Traveling Salesman
This scripts tspart.py, tspbitcity.py, and tspsolution.py were all written by Daniel C. Newman for the Eggbot project. They are all under a GNU GPL 2+ license. For specific documentation see [the Evil Mad Scientist Wiki](https://wiki.evilmadscientist.com/Generating_TSP_art_from_a_stippled_image). These have been deprecated in favor of [StippleGen 2](https://github.com/evil-mad/stipplegen). For more about them, you can also go to https://github.com/evil-mad/stipplegen.


To make this work, you'll also need the Linkern executable from the University of Waterloo's Concorde TSP solver. On Linux (I'm running Ubuntu 18.10), I just downloaded the [Concorde source code](http://www.math.uwaterloo.ca/tsp/concorde/downloads/downloads.htm), and copied the Linkern executable (in LINKERN/) to /usr/local/bin/. I included Linkern here for ease of use. For further installation information, including for Windows and OS X, see [the Evil Mad Scientist Wiki solver page](https://wiki.evilmadscientist.com/Obtaining_a_TSP_solver).

This code has been tested on Ubuntu 18.10 and Windows 10. Note: On Windows 10 everything is much harder to install.


## Weighted Voronoi
The code in the folder weighted-voronoi/ was wrtten by Nicolas P. Rougier under a BSD license. It was published in ReScience in 2017. More information can be found in its [repository](https://github.com/ReScience-Archives/Rougier-2017/).

### Prerequisites

This replication has been written and tested on OSX 10.12 (Sierra) amd Ubuntu 18.10 using the
following packages:

 * Python 3.6.0
 * Numpy 1.12.0
 * Scipy 0.18.1
 * Matplotlib 2.0.0
 * tqdm 4.11.2
 * Pillow 4.0.0


### Usage

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
```

## Image Tools

This folder contains some miscellaneous scripts to help with editing images.

### Get SVG

This program is to take images (tested on jpg's and png's) and convert them to svg file types.

#### Prerequisites

Python Packages:
 * Pillow 5.3.0
 
System Packages:
 * Potrace 1.14
 
#### Usage

```
 get_svg.sh file
 
 positional arguments:
  file                  
 ```
 
Potrace has a number of command line arguments which are available. To read more about those, go to [the Potrace website](http://potrace.sourceforge.net/#usage). In this bash script I'm using the following:

 * -s: output as svg
 * -n: curve optimization off
 * -a: corner threshold parameter
 ** I vary this between 0 and 2. 0 makes all small points triangular. Values in the 1-1.3 range make things nicely smooth. Values above 4/3 lead to the corners getting rounded over.
 * -t: speckle compression size (px)

## Future Work
 This is very much all a work in progress. Below is a list of some new stuff I'm hoping to add in the future.
 
 * Geyscale an image and make the max value a good one for doing a traveling salesman
 * Normalize peak brightness across an iamge
 * Added customization to stippler.py, such as adding a white cutoff, color inversion, etc.
