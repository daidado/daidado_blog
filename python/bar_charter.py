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
        percentages[i] = 100 * rawnums[i] / rawnums[4]
        #percentages[i] = 100 * rawnums[i] * nums1967[4] / nums1967[i] / rawnums[4]

    ind = np.arange(5)  # the x locations for the groups
    width = 0.55       # the width of the bars
    fig, ax = pyplot.subplots()
    rects = ax.bar(ind, percentages, width, color='r')

    # add some text for labels, title and axes ticks
    ax.set_ylim([0, 110])
    ax.set_ylabel('Percentage of the Top 5%\'s Cutoff Income')
    ax.set_title('Income Compared to Top 5% in {0}'.format(year),
                 fontweight='bold')
    ax.set_xticks(ind + width*5/8)
    ax.set_xticklabels(('Bottom 20%', 'Second', 'Third', 'Fourth', 'Top 5%'))

    # For the other graph uncomment this, change scale, & use raw #s in plot.
#    ax.get_yaxis().set_visible(False)
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

    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    writeGif('{0}/income.gif'.format(sys.argv[2]), images, .07)
