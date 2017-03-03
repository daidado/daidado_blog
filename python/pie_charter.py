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
    newvalues = [int(values[0]) + int(values[1]), int(values[2]), int(values[3]) + int(values[4])]
    newlabels = ["Democrats (w/ leans)", "Independents", "Republicans (w/ leans)"]
    print values
    pyplot.figure(1, figsize=(8,8))
    pyplot.axes([.15, .25, .7, .7])

    legend = ['{0}: {1:02d}%'.format(i,int(j)) for i,j in zip(newlabels, newvalues)]

    # Plot
    colors = ['blue', 'lightgrey', 'red']
    pyplot.pie(newvalues, shadow=False, colors=colors)
    pyplot.legend(legend,
                  loc='center',
                  bbox_to_anchor=[0.5, -.125],
                  fontsize=10)
    pyplot.title(title, fontsize=16, fontweight='bold')
    pyplot.savefig(outpath)

if __name__ == '__main__':    
    data = StringIO(sys.stdin.read())
    title = data.readline().split(",")[0].replace("\n", "")
    labels = [s.replace("\n", "") for s in data.readline().split(",")[1:]]
    
    images = []
    filepath = ""
    derr = True
    for l in data:
        yearCsv = l.split(',')
        newTitle = '{0}: {1}'.format(title, yearCsv[0])
        filepath = "{0}/{1}.png".format(sys.argv[1], yearCsv[0])
        makeoneyear(labels,
                    yearCsv[1:],
                    newTitle,
                    filepath)
        images.append(Image.open(filepath))
        if derr:
            images.append(Image.open(filepath))
            images.append(Image.open(filepath))
            images.append(Image.open(filepath))
            images.append(Image.open(filepath))
            derr = False
        
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    images.append(Image.open(filepath))
    writeGif('{0}/{1}.gif'.format(sys.argv[1], title),
             images,
             float(sys.argv[2]))

