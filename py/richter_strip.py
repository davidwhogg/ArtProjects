"""
This file is part of the ArtProjects repository.
Copyright 2014 David W. Hogg (NYU)

# usage:
- python richter_strip.py input.jpg output.jpg

# bugs:
- super-slow
"""

from PIL import Image
from PIL import ImageOps
import numpy as np
import sys

def richter_strip_ify(infile, outfile, nbits=4):
    im = Image.open(infile)
    pim = ImageOps.posterize(im, nbits)
    pim.save("foo.png")
    colors = [color for (count, color) in pim.getcolors(im.size[0]*im.size[1])]
    ncolors = len(colors)
    print "found %d colors" % ncolors
    newim = Image.new("RGB", (2, ncolors), "white")
    pix = newim.load()
    indx = np.argsort(np.random.uniform(size=ncolors))
    for ii, color in zip(indx, colors):
        for jj in range(newim.size[0]):
            pix[jj, ii] = color
    yfactor = np.round(float(im.size[1]) / float(ncolors)).astype(int)
    ysize = yfactor * ncolors
    xsize = np.round(float(ysize * im.size[0]) / float(im.size[1])).astype(int)
    newim = newim.resize((xsize, yfactor*ncolors), Image.NEAREST)
    newim.save(outfile)

if __name__ == "__main__":
    richter_strip_ify(sys.argv[1], sys.argv[2])
