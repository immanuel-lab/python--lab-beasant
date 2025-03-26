import geocoder

# Get current GPS coordinates
g = geocoder.ip('me')
coordinates = g.latlng

print(coordinates)