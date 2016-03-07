'''
Created on Sep 27, 2015

@author: J4ROD2
'''
from brewer2mpl import qualitative

class mapper(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    # create a fake data set for testing
    def create_latlong_df(self,count):

        self.count = count
        import random
        import pandas as pd
        
	self.latitude = pd.Series([random.uniform(40,42) for n in range(1, self.count)])
	self.longitude = pd.Series([random.uniform(-122,-120) for n in range(1, self.count)])
	self.color_val = pd.Series([random.randint(0,4) for n in range(1,self.count)])
	return pd.DataFrame({'latitude':self.latitude, 'longitude':self.longitude, 'color_val':self.color_val})

    def get_color(self,value):
        self.value = value
        import brewer2mpl
        self.bmap = brewer2mpl.get_map('RdBu', 'diverging', 5)
        return self.bmap.hex_colors[value]

    # convert a df into a geojson file 
    # http://geoffboeing.com/2015/10/exporting-python-data-geojson/

    def df_to_geojson(self, df, properties, lat='lat', lon='long'):

    	geojson = {'type':'FeatureCollection', 'features':[]}

        for _, row in df.iterrows():
            feature = {'type':'Feature',
                'properties':{},
                'geometry':{'type':'Point',
                            'coordinates':[]}}

            feature['geometry']['coordinates'] = [row[lon],row[lat]]

            for prop in properties:
                feature['properties'][prop] = row[prop]
            geojson['features'].append(feature)

        return geojson

    def write(self):
        import folium
        map_osm = folium.Map()
        self.latlong = self.create_latlong_df(18)
        
        import random
        
        map_osm.circle_marker(location=point, radius=8000*(self.color_val+1),
            popup='My Popup Info', line_color=self.get_color(self.color_val),
            fill_color=self.get_color(self.color_val), fill_opacity=0.8)

        map_osm.fit_bounds(self.latlong)

        return map_osm.create_map(path='osm.html')

if __name__ == "__main__":

    from datahandler import setup_ipeds_datasets as ips

    dh = ips.SetupIPEDSData()
    data = dh.get_data()

    m = mapper()
    geoj = m.dif_to_geojson(data, ['zip', 'instname', 'ftretention_rate', 'fall_total_undergrad'],
            lat='lat', lon='long')

    print(geoj)

    with open("unipeds.geojson", "w") as f:
        f.write(geoj)

    f.close()
