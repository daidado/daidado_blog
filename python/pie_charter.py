#!/usr/bin/env python
# sample use: python pie_charter.py

import string
import sys
from matplotlib import pyplot
from StringIO import StringIO

def makeoneyear(labels, values, title, outpath):
    pyplot.figure(1, figsize=(8,8))
    pyplot.axes([.15, .25, .7, .7])

    legend = ['{0}: {1:1.2f}%'.format(i,float(j)) for i,j in zip(labels, values)]

    # Plot
    pyplot.pie(values, shadow=False)
    pyplot.legend(legend, bbox_to_anchor=(.90, 0.05), fontsize=10)
    pyplot.title(title, fontsize=20, fontweight='bold')
    pyplot.savefig(outpath)

if __name__ == '__main__':    
    data = StringIO(sys.stdin.read())
    title = data.readline().split(",")[0].replace("\n", "")
    labels = [s.replace("\n", "") for s in data.readline().split(",")[1:]]
    for l in data:
        yearCsv = l.split(',')
        newTitle = '{0}: {1}'.format(title, yearCsv[0])
        makeoneyear(labels, yearCsv[1:], newTitle, "data/veterans_estimates/race_gif/pics/{0}.png".format(yearCsv[0]))
