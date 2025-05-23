from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapi")


def get_location(lat, long):
    location = geolocator.reverse((lat, long), language = "en")
    if location:
        return location
    else:
        return "Unkown"