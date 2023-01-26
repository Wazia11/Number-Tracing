import phonenumbers 

import folium

from Number import number 

from Number import imie

from phonenumbers import geocoder 

Key = 'd90cd77b73964b089559e8448a43aaae'

samNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(samNumber, "en")
print(yourLocation)

from phonenumbers import carrier 

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)

query = str(yourLocation)

results = geocoder.geocode(query)
##print(results)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 9)

folium.Marker([lat, lng],popup = yourLocation).add_to((myMap))

myMap.save(imie)
