#! /usr/bin/env python3

import numpy as np
from PIL import Image
import argparse
from tqdm import tqdm, trange
from  os import getcwd, makedirs

def find_min(colordict, color):
    dist = color_dist(list(colordict.items())[0][1], color)
    minkey = list(colordict.keys())[0]
    # tqdm.write(str(list(colordict.keys())[0]))
    for key, val in colordict.items():
        newdist = color_dist(val, color)
        if newdist < dist:
            dist = newdist
            minkey = key

    return minkey

def color_dist(c1, c2):
    return ((c1[0]- c2[0])**2 + (c1[1] - c2[1])**2 + (c1[2] - c2[2])**2)

parser = argparse.ArgumentParser()

parser.add_argument('filename', metavar='image filename', type=str,
                    help='Density image filename ')
filename = parser.parse_args().filename

im = Image.open(filename)
rgb = im.convert('RGB')
height, width = im.size

colors = {
    "010 white": (255, 255, 255),
    "030 dark red": (144, 14, 22),
    "041 pink": (194, 43, 107),
    "045 soft pink": (237, 132, 182),
    "050 dark blue": (27, 46, 93),
    "056 ice blue": (61, 161, 210),
    "060 dark green": (0, 64, 40),
    "063 lime-tree green": (106, 167, 45),
    "070 black": (13, 14, 17),
    "080 brown": (67, 47, 30),
    "081 light brown": (168, 136, 92),
    "082 beige": (206, 192, 159)
}

colorized_dict = {
    "010 white": Image.new("RGB", (height, width)),
    "030 dark red":  Image.new("RGB", (height, width)),
    "041 pink":  Image.new("RGB", (height, width)),
    "045 soft pink":  Image.new("RGB", (height, width)),
    "050 dark blue":  Image.new("RGB", (height, width)),
    "056 ice blue":   Image.new("RGB", (height, width)),
    "060 dark green":   Image.new("RGB", (height, width)),
    "063 lime-tree green":  Image.new("RGB", (height, width)),
    "070 black":   Image.new("RGB", (height, width)),
    "080 brown":   Image.new("RGB", (height, width)),
    "081 light brown":   Image.new("RGB", (height, width)),
    "082 beige":   Image.new("RGB", (height, width)),
}

imarr = Image.new("RGB", (height, width))
pixarr = imarr.load()

for i in trange(height):
    for j in range(width):
        colorkey = find_min(colors, rgb.getpixel((i, j)))
        # tqdm.write(str(colors[colorkey]))
        colorized_dict[colorkey].load()[i, j] = colors[colorkey]
        pixarr[i, j] = colors[colorkey]
        # tqdm.write(colorkey)


makedirs(getcwd() + "/vinylIms", exist_ok=True)
imarr.save(getcwd() + "/vinylIms/colorized.jpg")

for key, item in colorized_dict.items():
    # img = Image.frombuffer(item, mode = "RGB")
    item.save(getcwd() + "/vinylIms/" + key + ".jpg")
