#! /usr/bin/env python3

import numpy as np
from PIL import Image
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('filename', metavar='image filename', type=str,
                    help='Density image filename ')
filename = parser.parse_args().filename

im = Image.open(filename)

# im = Image.fromarray(data)
# im.show()

# im = im.convert('RGB')

im.save("out.bmp")
