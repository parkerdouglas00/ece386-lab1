from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my_386_hw")
location = geolocator.geocode("United States Military Academy")
print(location.latitude, location.longitude)
