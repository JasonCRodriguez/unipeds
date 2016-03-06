# -*- coding: utf-8 -*-
"""
Check if google geolocation data is correctly within the US using Geocoder Nominatim
Before using this file, you have to add the column "US" manually to the geoloc csv file.

Created on Sun Dec 13 19:44:07 2015

@author: takahirodoi
"""

import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
geolocator = Nominatim(timeout=10)
'''
from geopy.geocoders import GoogleV3
geolocator = GoogleV3()
'''

filename = '../GoogleGeolocData2.csv'
# filename = '../GeoNamesGeolocData.csv'

df = pd.read_csv(filename)


c = 0
thre = 1800
for index in df.index:
    if np.isnan(df.loc[index,'US']):
        lg = df.loc[index,'long']
        lt = df.loc[index,'lat']
        print index, df.loc[index,'instname']
        
        if not np.isnan(lt):
            coord = (lt,lg)
            
            #   strcoord = '%.6f' % lg + ', ' + '%.6f' % lt
            #   strloc = geolocator.reverse(strcoord)
            location = geolocator.reverse(coord)
            if "United States of America" in location.address:
                df.loc[index,'US'] = 1
            else:
                df.loc[index,'US'] = 0       
            
            c = c+1
            print c
    
            if c%100 == 0:
                df.to_csv(filename,index=False)
    
            if c>thre:
                break

df.to_csv(filename,index=False)

# location = geolocator.reverse("52.509669, 13.376294")






