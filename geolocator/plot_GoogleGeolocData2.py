# -*- coding: utf-8 -*-
"""
plot the location data inside GoogleGeolocData2.csv
output file: GoogleGeolocData2.html, GoogleGeolocData2.geojson
(only within US locations are plotted)

Created on Sun 1/31/2016
@author: takahirodoi

don't use geojson.MultiPoint(coordinates), as somehow this hangs up Spyder.
create a geojson file myself

"""

# two ways to pass geojson info to folium
# - string containing geojson infomation (this info will be embedded in the html file)
# - create a geojson file
# - I will use the second option


#from geojson import MultiPoint
import geojson
import folium
import pandas as pd
import numpy as np

# us option off
"""
outgeoj = "GoogleGeolocData1.geojson"
outhtml = "GoogleGeolocData1.html" 
filepath = "../GoogleGeolocData.csv"
"""
# us option on
outgeoj = "GoogleGeolocData2.geojson"
outhtml = "GoogleGeolocData2.html" 
filepath = "GoogleGeolocData2.csv"

df = pd.read_csv(filepath)
coordinates = []
isUS        = []

for index in df.index:
    lt = df.loc[index,'lat']
    lg = df.loc[index,'long']
    us = df.loc[index,'US']
    coordinates.append((lg,lt))
    isUS.append(us)


"""
# for google geoloc 2 something goes wrong with geojson.multipoint()
# check coordinates's value one by one
# this worked wihout a problem. so values inside coordinates are fine...
for val1, val2 in coordinates:
    tmp = (val1,val2)
    x    = geojson.MultiPoint(tmp)
    print val1,val2, " clear"
"""
    
# output coordinates into dump myself in the MultiPoint format    
dump = "{\"coordinates\": ["
for idx, val in  enumerate(coordinates):
    val0 = val[0]
    val1 = val[1]
    if isUS[idx] and not np.isnan(val1):
        dump = dump+"["+str(val0)+", "+str(val1)+"], "

dump = dump[:-2]
dump = dump+"], \"type\": \"MultiPoint\"}"

# geojson.MultiPoint doesn't work for the data in GoogleGeolocData2.csv
# x    = geojson.MultiPoint(coordinates)
# dump = geojson.dumps(x, sort_keys=True)
print(dump)

with open(outgeoj, "w") as outfile:
    outfile.write(dump)


# dump = geojson.dumps(x, sort_keys=True) # to get just a string ouput
# file.close() # no need because of with/as syntax


map = folium.Map(location=[19.61, -155.52],  width=1500, height =1300)
# map.geo_json(geo_str=dump)
map.geo_json(geo_path=outgeoj)
map.create_map(path=outhtml)





