#!/usr/bin/env python
# sample use: python pie_charter.py

from PIL import Image
# https://pypi.python.org/pypi/images2gif
from images2gif import writeGif
import string
import sys
import numpy
from matplotlib import pyplot
from StringIO import StringIO

def makeoneyear(labels, values, title, outpath):
    pyplot.figure(1, figsize=(8,8))
    pyplot.axes([.15, .25, .7, .7])

    legend =
        ['{0}: {1:05.2f}%'.format(i,float(j)) for i,j in zip(labels, values)]

    # Plot
    pyplot.pie(values, shadow=False)
    pyplot.legend(legend,
                  loc='center',
                  bbox_to_anchor=[0.5, -.125],
                  fontsize=10)
    pyplot.title(title, fontsize=20, fontweight='bold')
    pyplot.savefig(outpath)

if __name__ == '__main__':    
    data = StringIO(sys.stdin.read())
    title = data.readline().split(",")[0].replace("\n", "")
    labels = [s.replace("\n", "") for s in data.readline().split(",")[1:]]
    
    images = []
    for l in data:
        yearCsv = l.split(',')
        newTitle = '{0}: {1}'.format(title, yearCsv[0])
        filepath = "{0}/{1}.png".format(sys.argv[1], yearCsv[0])
        makeoneyear(labels,
                    yearCsv[1:],
                    newTitle,
                    filepath)
        images.append(Image.open(filepath))

    writeGif('{0}/{1}.gif'.format(sys.argv[1], title),
             images,
             float(sys.argv[2]))

