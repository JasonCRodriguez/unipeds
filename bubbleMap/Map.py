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
    def create_latlong(self):
        import
        
    def write(self):
        import folium
        map_osm = folium.Map(location=[45.5236, -122.6750])
        map_osm.circle_marker(location=(45.5215, -122.6261), radius=1500,
                  popup='My Popup Info', line_color='#3186cc',
                  fill_color='#3186cc', fill_opacity=0.2)
        return map_osm.create_map(path='osm.html')