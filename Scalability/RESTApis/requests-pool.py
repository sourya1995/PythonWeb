import requests
session = requests.Session()
adapter = requests.adapters.HTTPAdapter(
    pool_connections = 100,
    pool_maxsize = 100
)
session.mount('http://', adapter)
response = session.get("http://example.org")
print(response)