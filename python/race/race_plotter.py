#!/usr/bin/env python
# sample use: python pie_charter.py

import string
import sys
import numpy
from matplotlib import pyplot
from StringIO import StringIO

def makeoneyear(outdir, state, data1, data2):
    labels = ["White (Not Hispanic)", "Black or African American", "American Indian or Alaska Native",
              "Asian", "Native Hawaiian or Other Pacific Islander", "Hispanic and Latino"]
    fig, (ax1, ax2) = pyplot.subplots(1, 2, figsize=(10, 5))

    ax1.pie(data1, shadow=False, radius=1.15, center=(0, 0))
    ax1.set_title("65+ {0} Residents".format(state), fontweight="bold", size=20)
    ax1.axis('equal')

    ax2.pie(data2, shadow=False, radius=1.15, center=(0, 0))
    ax2.set_title("<18 {0} Residents".format(state), fontweight="bold", size=20)
    ax2.axis('equal')

    ax2.legend(labels, loc='lower center', bbox_to_anchor=[-0.1, -0.45])
    #pyplot.show()
    pyplot.savefig('{0}/{1}.png'.format(outdir, state)) 
    pyplot.close()
    
if __name__ == '__main__':    
    f = open(sys.argv[1])
    f.readline()
    rows = f.readlines()
    for row in rows:
        data = row.split(',')
        makeoneyear(sys.argv[2], data[0],
          [int(data[13]), int(data[14]), int(data[15]), int(data[16]), int(data[17]), int(data[18])],
          [int(data[1]), int(data[2]), int(data[3]), int(data[4]), int(data[5]), int(data[6])])

