import requests

session = requests.Session()
session.get("http://example.com")
print("Connection made")
session.get("http://example.com")
print("Connection reused")