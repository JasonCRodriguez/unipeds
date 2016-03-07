from univperformance import bySector as bs

from datahandler import setup_ipeds_datasets as ips
from bubbleMap import Map as bm
import json

dh = ips.SetupIPEDSData()
data = dh.get_data()

m = bm.mapper()

geoj = m.df_to_geojson(df=data, properties=['zip', 'instname', 'ftretention_rate', 'fall_total_undergrad'], lat='lat', lon='long')

print(geoj)


with open("unipeds.geojson", "w") as f:
    f.write(json.dumps(geoj, ensure_ascii=False))

f.close()
