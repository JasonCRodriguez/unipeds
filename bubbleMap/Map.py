'''
Created on Sep 27, 2015

@author: J4ROD2
'''
from brewer2mpl import qualitative
from pandas import read_csv


class Mapper(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def create_latlong_df(self,count):
        self.count = count
        import random
        return  [(random.uniform(40,42), random.uniform(-122,-120)) for n in range(1,self.count)]
    
    def get_color(self,value):
        self.value = value
        import brewer2mpl
        self.bmap = brewer2mpl.get_map('RdBu', 'diverging', 5)
        return self.bmap.hex_colors[value]

    def get_universities(self,csv):


        # read the csv into a dataframe
        self.df = read_csv(csv, sep=",")

        # strip out extra columns leaving only lat, long, and size 
    
    def write(self):
        import folium
        map_osm = folium.Map()
        self.latlong = self.create_latlong_df(18)
        
        import random
        
        for point in self.latlong:
            self.color_val = random.randint(0,4)
            map_osm.circle_marker(location=point, radius=8000*(self.color_val+1),
                popup='My Popup Info', line_color=self.get_color(self.color_val),
                fill_color=self.get_color(self.color_val), fill_opacity=0.8)
            map_osm.fit_bounds(self.latlong)
        return map_osm.create_map(path='osm.html')
