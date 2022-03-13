import numpy as np
from hilbert import decode
import matplotlib.pyplot as plt

def singlePly(ax, height, width, aspect, bundleSize):
    aspect = aspect/2
    x_starts = np.arange(0, width, bundleSize)
    y_starts = np.arange(0, height, aspect*bundleSize)
    print(x_starts, y_starts)
    skip = False
    for x in  x_starts:
        skip = not skip
        for y in y_starts:
            if not skip:
                xline = np.linspace(x, x+bundleSize, int(height/bundleSize)*10)
                yline = [y] * len(xline)
                ax.plot(xline, yline, c="black", lw=1)
                skip = not skip
            else:
                skip = not skip
    return ax

def crossPly(ax, height, width, aspect, bundleSize):
    aspect = aspect/2
    x_starts = np.arange(0, width, bundleSize)
    y_starts = np.arange(0, height, aspect*bundleSize)
    skip = False
    for x in  x_starts:
        skip = not skip
        for y in y_starts:
            if not skip:
                xline = np.linspace(x, x+bundleSize, int(height/bundleSize)*10)
                yline = [y] * len(xline)
                ax.plot(xline, yline, c="black")
                ax.plot(yline, xline, c="black")
                skip = not skip
            else:
                skip = not skip
    return ax


def draw_curve(ax, num_bits):
    num_dims = 2

    # The maximum Hilbert integer.
    max_h = 2**(num_bits*num_dims)

    # Generate a sequence of Hilbert integers.
    hilberts = np.arange(max_h)

    # Compute the 2-dimensional locations.
    locs = decode(hilberts, num_dims, num_bits)

    # Draw
    ax.plot(locs[:,0], locs[:,1], color="black")

    return ax

bundleSize = .25 # Fiber bundle width in inches
aspect = 6 # Ratio of bundle length to width
dpi = 300 # Resolution
height = 12 # Plaque height in inches
width = 12 # Plaque width in inches
num_bits = 6
modes = ("oneply", "crossply", "hilbert")
mode = modes[2]
fs = (height, width) # Fig Size in inches

spkw = { #Subplot keyword arg dict
    "frameon" : False,
    "aspect" : 'equal',
}
tlkw = { # Tight layour kwarg dict
    "pad" : -height/2.82
}

fig, ax = plt.subplots(subplot_kw=spkw,
                        dpi=300,
                        frameon=False,
                        figsize=fs,
                        tight_layout=tlkw
                        )

ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)

if mode == "oneply":
    ax = singlePly(ax, height, width, aspect, bundleSize)
if mode == "crossply":
    ax = crossPly(ax, height, width, aspect, bundleSize)
if mode == "hilbert":
    ax = draw_curve(ax, num_bits)

plt.savefig("test.svg")
