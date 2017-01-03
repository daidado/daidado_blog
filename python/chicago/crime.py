import numpy
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

if __name__ == '__main__':
    filename = sys.argv[1]
    latLong = numpy.genfromtxt(filename,
                               delimiter=',',
                               dtype=[('lat', numpy.float32),
                                      ('lon', numpy.float32)],
                               usecols=(19, 20))
    fig = plt.figure()

    chicago = Basemap(llcrnrlon=-87.9,
                      llcrnrlat=41.6046,
                      urcrnrlon=-87.4277,
                      urcrnrlat=42,
                      projection='merc',
                      resolution='h')

    chicago.drawcoastlines()
    chicago.drawstates()
    chicago.fillcontinents(color = 'gainsboro')
    chicago.drawmapboundary(fill_color='steelblue')
    chicago.drawmapboundary(fill_color='white')
    chicago.readshapefile('data/chicago/Neighborhoods_2012b',
                          'Neighborhoods')
    x, y = chicago(latLong['lon'], latLong['lat'])
    print len(x)
    chicago.plot(x, y, 'o', markersize='4', color='Red')

    plt.title("Murders in Chicago")
    plt.show()
