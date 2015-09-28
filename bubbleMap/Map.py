'''
Created on Sep 27, 2015

@author: J4ROD2
'''

class Mapper(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def create_latlong(self,count):
        self.count = count
        import random
        return  [(random.uniform(40,42), random.uniform(-122,-120)) for n in range(1,self.count)]
    
    def write(self):
        import folium
        map_osm = folium.Map()
        self.latlong = self.create_latlong(8)
        for point in self.latlong:
            map_osm.circle_marker(location=point, radius=15000,
                                          popup='My Popup Info', line_color='#3186cc',
                                          fill_color='#3186cc', fill_opacity=0.2)
        map_osm.fit_bounds(self.latlong)
        return map_osm.create_map(path='osm.html')