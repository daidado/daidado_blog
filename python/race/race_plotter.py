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
        # Gross but I'm lazy; print how many fewer white people are by percentage. Run sort on cmdline output.
        print "{0:5.2f}: {1}".format(
            100*(float(data[13])/(float(data[13])+float(data[14])+float(data[15])+float(data[16])+float(data[17])+float(data[18])))
            - 100*(float(data[1])/(float(data[1])+float(data[2])+float(data[3])+float(data[4])+float(data[5])+float(data[6]))),
            data[0])
        makeoneyear(sys.argv[2], data[0],
                    [float(data[13]), float(data[14]), float(data[15]), float(data[16]), float(data[17]), float(data[18])],
                    [float(data[1]), float(data[2]), float(data[3]), float(data[4]), float(data[5]), float(data[6])])

