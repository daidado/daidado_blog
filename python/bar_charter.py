#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import sys
from matplotlib import pyplot
from PIL import Image
# https://pypi.python.org/pypi/images2gif
from images2gif import writeGif

def plot(year, rawnums, outpath):
    nums1967 = [ 3000, 5850, 8303, 11840, 19000]
    percentages = [ 0, 0, 0, 0, 0]
    for i in range(0, 5):
        percentages[i] = rawnums[i] * nums1967[4] / nums1967[i] / rawnums[4]

    ind = np.arange(5)  # the x locations for the groups
    width = 0.55       # the width of the bars
    fig, ax = pyplot.subplots()
    rects = ax.bar(ind, percentages, width, color='r')

    # add some text for labels, title and axes ticks
    ax.set_ylim([0, 1.05])
    ax.set_ylabel('Income Cutoff (Adjusted to 1967 inequality ratios)')
    ax.set_title('Change in Wealth Inequality from 1967 to {0}'.format(year),
                 fontweight='bold')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))

    pyplot.tick_params(axis='x', bottom='off', top='off', which='both')
    pyplot.savefig(outpath)
    pyplot.close()

if __name__ == '__main__':
    f = open(sys.argv[1])
    f.readline()
    rows = f.readlines()
    images = []
    for row in rows:
        print row
        data = row.split(',')
        filepath = '{0}/{1}.png'.format(sys.argv[2], data[0])
        plot(data[0], [float(data[1]), float(data[2]), float(data[3]), float(data[4]), float(data[5])], filepath)
        images.append(Image.open(filepath))

    writeGif('{0}/income.gif'.format(sys.argv[2]), images, .07)
