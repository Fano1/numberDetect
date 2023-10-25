import phonenumbers 
from phonenumbers import geocoder
from phonenumbers import carrier
import folium
from number import number
from opencage.geocoder import OpenCageGeocode

api_key = "3a53ddf2fcc74455ba7b57a4420a9d34"

parsed_number = phonenumbers.parse(number)
geocoderr = OpenCageGeocode(api_key)

location = geocoder.description_for_number(parsed_number, "en")
service_provider = carrier.name_for_number(parsed_number, "en")

query = str(location)
result = geocoderr.geocode(query)
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(number)
print(location)
print(service_provider)
print(result)
print(lat, lng)
