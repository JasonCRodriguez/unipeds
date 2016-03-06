Takahiro Doi
2016-02-28

[Create a csv file that includes geolocation data]
create_geoloc_csv.py
 - Google GeoCoder API
 - Output file: GoogleGeolocData2.csv

- I used Google GeoCoder API with region parameter set to 'us'
- Most of the university zip codes were properly transformed into geo locations within the US, except 7. For these 7 (none or clearly wrong locations such as Europe), I manually input the correct geolocations obtained from manual GoogleMap search.    

========================================================================
[plot the location data inside GoogleGeolocData2.csv]
plot_GoogleGeolocData2.py
 - output file: GoogleGeolocData2.html, GoogleGeolocData2.geojson
 - (only within US locations are plotted)


========================================================================
[Reverse geocoding to check if a geolocation is within the US]
reverse_GoogleGeolocData.py
 - reverse geocoder, Nominatim
 - output: US column in the GoogleGeolocData2.csv

