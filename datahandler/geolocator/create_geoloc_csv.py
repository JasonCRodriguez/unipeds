# -*- coding: utf-8 -*-
"""
Create a csv file that includes gelocation data. 
This script uses GoogleV3 geocoders.

Created on Sun Nov 22 20:30:49 2015
@author: takahirodoi
"""
import sys
import numpy as np
import os.path
import time
import pandas as pd
import setup_ipeds_datasets as sid
from geopy.geocoders import GoogleV3
geolocator = GoogleV3(timeout=100)
filename   = 'GoogleGeolocData2.csv'
# import time
# •	2,500 free requests per day
# •	10 requests per second


# load Google Geolocation data file. If it doesn't exist, create it with empty lat/long columns. 
if os.path.isfile(filename):
    # be careful, the saved file's 
    df2 = pd.read_csv(filename)
else: 
    x  = sid.SetupIPEDSData()
    df = x.get_data()
    df2 = pd.DataFrame(index=df.index, columns=['unitid','instname','zip','lat','long'])
    df2['unitid']   = df['unitid']
    df2['instname'] = df['instname']
    df2['zip']      = df['zip']
    df2.to_csv(filename)
    print "data is saved to "+filename
    print "run this code again to populate lat/long data"
    sys.exit()


# Empty lat, long data
# query Google GeoLocation only 500 times per day
c    = 0
thre = 300;
# for i in df2['zip']:
for index in df2.index:
    if np.isnan(df2.loc[index,'lat']):
        loc = geolocator.geocode(df2.loc[index,'zip'],region='us')
        time.sleep(0.11) #110ms dely to evaid google usage limitatio
        # None was returne for Uni Guam 
        if loc != None:
            df2.loc[index,'lat']  = loc.latitude
            df2.loc[index,'long'] = loc.longitude
            c  = c + 1
            print "geolocation is retrieved and saved. index="+str(index)
            
    if c%100 == 0:
        df2.to_csv(filename,index=False)

    if c>thre:
        break

df2.to_csv(filename,index=False)



'''
# timestr = time.strftime("%Y%m%d-%H%M%S")
# df2.to_csv('GoogleGeolocData'+timestr+'.csv')
df2.to_csv(filename)
# often it's safer to use index=df.index.copy()
'''




'''
c = 0
for i in df["zip"]:
    loc = geolocator.geocode(i)
    print((loc.latitude, loc.longitude))
    c = c+1
'''

    
    