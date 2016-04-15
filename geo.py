import json
import requests
from urllib.parse import urlencode
import pprint

base_url="https://maps.googleapis.com/maps/api/geocode/json?"

address=input("Enter location: ")

main_url=base_url + urlencode({"address":address})

r=requests.get(main_url)

json_obj=r.json()

if 'status' not in json_obj or json_obj["status"]!="OK":
	print("fail")
	print(json_obj)
	

lat=json_obj["results"][0]["geometry"]["location"]["lat"]
lng=json_obj["results"][0]["geometry"]["location"]["lng"]
print("Latitudes:" ,lat)
print("Longitudes:", lng)
location=json_obj["results"][0]["formatted_address"]
print("Location:", location)