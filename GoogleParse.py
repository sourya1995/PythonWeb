import urllib.request, urllib.parse
import json

serviceurl = "http://py4e-data.dr-chuck.net/json?key=42&"

address_input = input("Enter Location:")
params = {"sensor": "false", "address": address_input}
url = serviceurl + urllib.parse.urlencode(params)
print("Retrieving", url)
data = urllib.request.urlopen(url).read().decode("utf-8")
print("Retrieved", len(data), 'characters')
json_obj = json.loads(data)

place_id = json_obj["results"][0]["place_id"]
print("Place id", place_id)
