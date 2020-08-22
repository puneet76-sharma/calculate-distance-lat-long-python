# pip install geopy

# calculate-distance-lat-long-python
geopy is a Python client for several popular geocoding web services.  geopy makes it easy for Python developers to locate the coordinates of addresses, cities, countries, and landmarks across the globe using third-party geocoders and other data sources.

geopy includes geocoder classes for the OpenStreetMap Nominatim, Google Geocoding API (V3), and many other geocoding services. The full list is available on the Geocoders doc section. Geocoder classes are located in geopy.geocoders.

geopy is tested against CPython (versions 3.5, 3.6, 3.7, 3.8) and PyPy3. geopy 1.x line also supported CPython 2.7, 3.4 and PyPy2.


Using great-circle distance:

from geopy.distance import great_circle
newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
print(great_circle(newport_ri, cleveland_oh).miles)
536.997990696
